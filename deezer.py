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
    cur.execute("CREATE TABLE IF NOT EXISTS DeezerData(id TEXT, artistName TEXT, ranking FLOAT, trackTimeMillis FLOAT, title TEXT)")
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
                title = info["title_short"]
                #playlist = 
                cur.execute('INSERT INTO DeezerData(id, artistName, ranking, trackTimeMillis, title) VALUES (?,?,?,?,?)', (id_num, name, rank, duration, title))
                count += 1
    conn.commit()


#Calculating the average time of song in playlist  
    cur.execute("SELECT trackTimeMillis from DeezerData")
    total = 0
    avg_length = 0
    count = 0
    for row in cur:
        time = row[-1] 
        total += time
        count += 1
    avg_milli = total/count
    avg = avg_milli / 60
    avg_min = round(avg, 2)
    conn.commit()
    f = open("DeezerSummary.txt", 'w')
    f.write("Average duration for a song in the Global 2020 Hits Playlist is: " + str(avg_min) + " minutes" + "\n")
    f.close()
    
def createvisual():
    conn = sqlite3.connect("DeezerDB.sqlite")
    cur = conn.cursor()
    durations = []
    titles = []
    cur.execute("SELECT trackTimeMillis, title from DeezerData")
    count = 0
    for row in cur: 
        durations.append(float(row[0])/60)
        titles.append(row[1])
        count += 1
        if count == 30:
            break
    plt.figure(1, figsize = (30,11))
    xbar = titles
    ybar = durations
    plt.bar(xbar,ybar, width =.8, align = "center", color = ["#f72585", '#480ca8', '#4cc9f0'])
    plt.title("Durations of Songs from Global 2020 Hits Playlist")
    plt.xlabel("Song Title")
    plt.ylabel("Duration (Min)")
    plt.ylim(2,5)
    plt.tick_params(axis='x', rotation=70)
    plt.savefig("DeezerBargraph.png")
    plt.show()

def main():
    cur,conn = setUpDatabase('DeezerDB.sqlite')
    music(cur, conn,"Global 2020", 3185085222)
    music(cur, conn, "Best of Hip-Hop 2020",5171651864)
    test = createvisual()


if __name__ == '__main__':
    main()
