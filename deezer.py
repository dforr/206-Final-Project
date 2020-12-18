#Deezer Info 
import requests
import json
import sqlite3 
import os
import matplotlib 
import matplotlib.pyplot as plt 



# Create Database
def setUpDatabase(db_name):
    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path+'/'+db_name)
    cur = conn.cursor()
    return cur, conn

def music(cur, conn, Pname, playlist):
    url = "https://api.deezer.com/playlist/" + str(playlist)
    headers = {    
    'x-rapidapi-key': "e8987c562amsh78b1a8d73318a6fp16a5aajsn465e38986a0e",    
    'x-rapidapi-host': "deezerdevs-deezer.p.rapidapi.com"    
    }
    response = requests.get(url, headers = headers)    
    cur.execute("CREATE TABLE IF NOT EXISTS DeezerData(id TEXT, artistName TEXT, ranking FLOAT, trackTimeMillis FLOAT)")
    text = json.loads(response.text) 
    tracks = text.get('tracks')
    data = tracks.get('data')
    cur.execute('SELECT id FROM DeezerData')
    id_list = cur.fetchall() #selecting all id from table, and saving them to a list
    index = len(id_list) #first thing in the id_list is 0, but the second time you'd run thru is 25
    count = 0 #limiting to 25 
    for info in data: 
        if count < 25:
            id_num = info['id']
            if id_num not in id_list: #if id num is already in the id list, it would loop through again and wouldn't add the count
                name = info['artist']['name']
                rank = info['rank']
                duration = info['duration']
                #playlist = 
                cur.execute('INSERT INTO DeezerData(id, artistName, ranking, trackTimeMillis) VALUES (?,?,?,?)', (id_num, name, rank, duration))
                count += 1
    conn.commit()


#Calculating the average time of song in playlist  
    cur.execute("SELECT trackTimeMillis from DeezerData")
    total = 0
    avg_length = 0
    count = 0
    for row in cur:
        time = row[-1] #change row, index at a different
        total += time
        count += 1
    avg_milli = total/count
    avg = avg_milli / 60
    avg_min = round(avg, 2)
    #conn = sqlite3.connect('DeezerCalculations.sqlite')
    #cur = conn.cursor()
    #cur.execute('CREATE TABLE IF NOT EXISTS DeezerCalc( avg_min FLOAT)')
    #cur.execute('INSERT INTO DeezerCalc(avg_min) VALUES (?)', (avg_min))
    conn.commit()
    #counter = 0
    f = open("DeezerSummary.txt", 'w')
    f.write("Average duration for a song in the" + Pname + " is: " + str(avg_min) + " minutes" + "\n")
    f.close()
    

#music(cur, conn,"Hip-Hop Hits", 1677006641)
#music(cur, conn, "Rap Bangers", 1996494362)
#music(cur, conn, "Best of Hip-Hop 2020",5171651864)
#music("Global 2020", 3185085222)
#music("Hip-Hop Hits", 1677006641)
#music("Rap Bangers", 1996494362)
#music("Best of Hip-Hop 2020", 5171651864)


def createvisual():
    conn = sqlite3.connect("testtest.sqlite")
    cur = conn.cursor()
    durations = []
    cur.execute("SELECT trackTimeMillis from DeezerData")
    for row in cur: 
        print(row[0])
        durations.append(float(row[0]))
    plt.figure(1, figsize = (8.5,11))
    xbar = ["song1", "song2", "song3", "song4", "song5", "song6"]
    ybar = [durations[0], durations[1], durations[2], durations[3], durations[4], durations[5]]
    plt.bar(xbar,ybar, align = "center", color = "blue")
    plt.title("Average Length of Song by Popular")
    plt.xlabel("Artist")
    plt.ylabel("Duration (Min)")
    plt.ylim(2,5)
    plt.savefig("DeezerBargraph.png")
    plt.show()

def main():
    cur,conn = setUpDatabase('testtest.sqlite')
    music(cur, conn,"Global 2020", 3185085222)
    test = createvisual()


if __name__ == '__main__':
    main()
