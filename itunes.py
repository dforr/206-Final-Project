import requests
import pprint
import json
import sqlite3
import matplotlib
import matplotlib.pyplot as plt

def getItunes(artist, offset):
    offset=0
    param = {"limit":25, "offset": offset}
    base_url = "https://itunes.apple.com/search?term=t" + artist
    b = requests.get(base_url, params = param).json()
    return b


def getData(data, artistName):
    
    conn = sqlite3.connect("itunesdatabase.sqlite") 
    cur = conn.cursor()
    #Also do it here
    cur.execute("CREATE TABLE IF NOT EXISTS ItunesData(id TEXT UNIQUE, artistName TEXT, trackTimeMillis INTEGER, trackName TEXT)")
    counter = 0
    #start = cur.fetchone()
    #start = start[0]
    for x in data['results']:
        #offset = 0
        #counter += 1
        #if counter == 26:
        #    break
        # For every column name just add a _ in front of it.
        # Left hand = column name
        # Right hand = API fetched dictionary
        _id = x['trackId']
        _artistName = x['artistName']
        _trackTimeMillis = x['trackTimeMillis'] 
        _trackName = x['trackName']
        print(_trackName)
        #offset += 1
        # Add a column name in the orange
        # You must also add the underscored columnname in the white, also add question mark
        cur.execute('INSERT OR IGNORE INTO ItunesData(id, artistName, trackTimeMillis, trackName) VALUES (?,?,?,?)', (_id, _artistName, _trackTimeMillis, _trackName))
        counter += 1
        conn.commit()
    

    cur.execute("SELECT artistName, trackTimeMillis from ItunesData")
    total = 0
    avg_length = 0
    count = 0
    for row in cur:
        time = row[-1]
        if time < 600000:
            total += time
            count += 1
    avg_milli = total/count
    avg = avg_milli / 60000
    avg_min = round(avg, 2)
    conn = sqlite3.connect('ItunesCalculations.sqlite')
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS ItunesCalc(artistName TEXT, avg_min FLOAT)')
    cur.execute('INSERT INTO ItunesCalc(artistName, avg_min) VALUES (?,?)', (artistName,avg_min,))
    conn.commit()

    cur.execute('SELECT * FROM ItunesCalc')
    counter = 0
    f = open("ItunesSummary.txt", 'w')
    for row in cur:
            counter += 1
            f.write("Average duration for a " + str(row[0]) + " song is: " + str(row[1]) + " minutes" + "\n")
    f.close()

def createvisual():
    conn = sqlite3.connect("ItunesCalculations.sqlite") 
    cur = conn.cursor()
    avg_dur = []
    cur.execute("SELECT * from ItunesCalc")
    for row in cur:
        avg_dur.append(float(row[1]))
    plt.figure(1, figsize = (8.5,11))
    x = ["Taylor Swift", "Drake", "Justin Bieber", "One Direction", "Frank Ocean", "Ariana Grande"]
    y = [avg_dur[0], avg_dur[1], avg_dur[2], avg_dur[3], avg_dur[4], avg_dur[5]]
    plt.bar(x, y, width = .8, align = "center", color = ["#1C3144", "#FF206E", "#FBFF12", "#41EAD4", "#3F88C5","#1C7C54" ] )
    plt.title("Average Length of Song by Popular Artists")
    plt.xlabel("Artist")
    plt.ylabel("Duration (Min)")
    plt.ylim(3.5,4)
    plt.savefig("ItunesBargraph.png")
    plt.show()


def main():
    conn = sqlite3.connect("itunesdatabase.sqlite") 
    cur = conn.cursor()
    try:
        cur.execute("SELECT * from ItunesData")
        rowcount = cur.fetchone()[0]
    except:
        rowcount = 0
    #conn = sqlite3.connect("fifth.sqlite") 
    #cur = conn.cursor()
    #start = cur.fetchone()
    #start = start[0]
    data2 = getItunes("taylor+swift", rowcount)
    data3 = getItunes("drake", rowcount)
    data4 = getItunes("justin+bieber", rowcount)
    data5 = getItunes("one+direction", rowcount)
    data6 = getItunes("frank+ocean", rowcount)
    data8 = getItunes("ariana+grande", rowcount)
    getData(data2, "Taylor Swift")
    getData(data3, "Drake")
    getData(data4, "Justin Bieber")
    getData(data5, "One Direction")
    getData(data6, "Frank Ocean")
    getData(data8, "Ariana Grande")

    visual = createvisual()

   #if rowcount >= 25:
    #    data2 = getItunes("https://itunes.apple.com/search?term=taylor+swift", 25)
     #   getData(data2)
    #elif rowcount >= 50:
    #    data2 = getItunes("https://itunes.apple.com/search?term=taylor+swift", 50)
    #    getData(data2)
    #elif rowcount >= 75:
     #   data2 = getItunes("https://itunes.apple.com/search?term=taylor+swift", 75)
    #    getData(data2)
    #else:
    #    data2 = getItunes("https://itunes.apple.com/search?term=taylor+swift", 100)
    #    getData(data2)

   
    
if __name__ == '__main__':
    main()


#data = getItunes("https://itunes.apple.com/search?term=justin+bieber")
#data1 = getItunes("https://itunes.apple.com/search?term=halsey")
##data2 = getItunes("https://itunes.apple.com/search?term=taylor+swift&limit=25&offset=")
#print(data)
#getData(data)
#getData(data1)
#getData(data2)