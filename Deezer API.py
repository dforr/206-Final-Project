#Deezer Info 
import requests
import json
import sqlite3 
import os
import matplotlib 
import matplotlib.pyplot as plt 

url = "https://api.deezer.com/playlist/3185085222"
headers = {    
    'x-rapidapi-key': "e8987c562amsh78b1a8d73318a6fp16a5aajsn465e38986a0e",    
    'x-rapidapi-host': "deezerdevs-deezer.p.rapidapi.com"    
    }
response = requests.get(url, headers = headers)      

# Create Database
def setUpDatabase(db_name):
    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path+'/'+db_name)
    cur = conn.cursor()
    return cur, conn

def music(cur, conn):
    cur.execute("CREATE TABLE IF NOT EXISTS DeezerData(id TEXT, artistName TEXT, ranking FLOAT, trackTimeMillis FLOAT)")
    print(response.json())
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
                cur.execute('INSERT INTO DeezerData(id, artistName, ranking, trackTimeMillis) VALUES (?,?,?,?)', (id_num, name, rank, duration))
                count += 1
        print(id_num)
        print(name)
        print(rank)
        print(duration)
    conn.commit()

#Calculating the average time of song in playlist  
    cur.execute("SELECT trackTimeMillis from DeezerData")
    total = 0
    avg_length = 0
    count = 0
    for row in cur:
        time = row[-1] #change row, index at a different
        print(time) 
        total += time
        count += 1
    avg_milli = total/count
    avg = avg_milli / 60
    avg_min = round(avg, 2)
    conn = sqlite3.connect('DeezerCalculations.sqlite')
    #counter = 0
    f = open("DeezerSummary.txt", 'w')
    f.write("Average duration for a song in the Global 2020 playlist is:" + str(avg_min) + " minutes" + "\n")
    f.close()
    print(avg_min)
cur,conn = setUpDatabase('fifth.sqlite')
music(cur, conn)

#Information for Hip-Hop Hits Playlist
url = "https://api.deezer.com/playlist/1677006641"
headers = {    
    'x-rapidapi-key': "e8987c562amsh78b1a8d73318a6fp16a5aajsn465e38986a0e",    
    'x-rapidapi-host': "deezerdevs-deezer.p.rapidapi.com"    
    }
response = requests.get(url, headers = headers)      

def music(cur, conn):
    cur.execute("CREATE TABLE IF NOT EXISTS DeezerData(id TEXT, artistName TEXT, ranking FLOAT, trackTimeMillis FLOAT)")
    print(response.json())
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
                cur.execute('INSERT INTO DeezerData(id, artistName, ranking, trackTimeMillis) VALUES (?,?,?,?)', (id_num, name, rank, duration))
                count += 1
        print(id_num)
        print(name)
        print(rank)
        print(duration)
    conn.commit()

#Calculating the average time of song in playlist  
    cur.execute("SELECT trackTimeMillis from DeezerData")
    total = 0
    avg_length = 0
    count = 0
    for row in cur:
        time = row[-1] #change row, index at a different
        print(time) 
        total += time
        count += 1
    avg_milli = total/count
    avg = avg_milli / 60
    avg_min = round(avg, 2)
    conn = sqlite3.connect('DeezerCalculations.sqlite')
    #counter = 0
    f = open("DeezerSummary.txt", 'w')
    f.write("Average duration for a song in the Hip-Hop playlist is:" + str(avg_min) + " minutes" + "\n")
    f.close()
    print(avg_min)
cur,conn = setUpDatabase('fifth.sqlite')
music(cur, conn)

#Rap Bangers Playlist------------------------------------------------------------------------------------------------------------------------
url = "https://api.deezer.com/playlist/1996494362"
headers = {    
    'x-rapidapi-key': "e8987c562amsh78b1a8d73318a6fp16a5aajsn465e38986a0e",    
    'x-rapidapi-host': "deezerdevs-deezer.p.rapidapi.com"    
    }
response = requests.get(url, headers = headers)      

def music(cur, conn):
    cur.execute("CREATE TABLE IF NOT EXISTS DeezerData(id TEXT, artistName TEXT, ranking FLOAT, trackTimeMillis FLOAT)")
    print(response.json())
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
                cur.execute('INSERT INTO DeezerData(id, artistName, ranking, trackTimeMillis) VALUES (?,?,?,?)', (id_num, name, rank, duration))
                count += 1
        print(id_num)
        print(name)
        print(rank)
        print(duration)
    conn.commit()

#Calculating the average time of song in playlist  
    cur.execute("SELECT trackTimeMillis from DeezerData")
    total = 0
    avg_length = 0
    count = 0
    for row in cur:
        time = row[-1] #change row, index at a different
        print(time) 
        total += time
        count += 1
    avg_milli = total/count
    avg = avg_milli / 60
    avg_min = round(avg, 2)
    conn = sqlite3.connect('DeezerCalculations.sqlite')
    #counter = 0
    f = open("DeezerSummary.txt", 'w')
    f.write("Average duration for a song in the Rap Banger playlist is:" + str(avg_min) + " minutes" + "\n")
    f.close()
    print(avg_min)
cur,conn = setUpDatabase('fifth.sqlite')
music(cur, conn)

#Best of Hip-Hop 2020 
url = "https://api.deezer.com/playlist/5171651864"
headers = {    
    'x-rapidapi-key': "e8987c562amsh78b1a8d73318a6fp16a5aajsn465e38986a0e",    
    'x-rapidapi-host': "deezerdevs-deezer.p.rapidapi.com"    
    }
response = requests.get(url, headers = headers)      

def music(cur, conn):
    cur.execute("CREATE TABLE IF NOT EXISTS DeezerData(id TEXT, artistName TEXT, ranking FLOAT, trackTimeMillis FLOAT)")
    print(response.json())
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
                cur.execute('INSERT INTO DeezerData(id, artistName, ranking, trackTimeMillis) VALUES (?,?,?,?)', (id_num, name, rank, duration))
                count += 1
        print(id_num)
        print(name)
        print(rank)
        print(duration)
    conn.commit()

#Calculating the average time of song in playlist  
    cur.execute("SELECT trackTimeMillis from DeezerData")
    total = 0
    avg_length = 0
    count = 0
    for row in cur:
        time = row[-1] #change row, index at a different
        print(time) 
        total += time
        count += 1
    avg_milli = total/count
    avg = avg_milli / 60
    avg_min = round(avg, 2)
    conn = sqlite3.connect('DeezerCalculations.sqlite')
    #counter = 0
    f = open("DeezerSummary.txt", 'w')
    f.write("Average duration for a song in the Best of Rap 2020 playlist is:" + str(avg_min) + " minutes" + "\n")
    f.close()
    print(avg_min)
cur,conn = setUpDatabase('fifth.sqlite')
music(cur, conn)

def createvisual():
    conn = sqlite3.connect("DeezerCalculations.sqlite")
    cur = conn.cursor()
    avg_dur = []
    cur.execute("SELECT * from DeezerCalc")
    for row in cur: 
        avg_dur.append(float(row[1]))
    plt.figure(1, figsize = (8.5,11))
    x = ["Global Hits 2020", "Hip-Hop Playlist", "Rap Bangers", "Best of Rap 2020"]
    y = [avg_dur[0], avg_dur[1], avg_dur[2], avg_dur[3], avg_dur[4], avg_dur[5]]
    plt.bar(x,y, width = .8, align = "center", color = ["#1C3144", "#FF206E", "FBFF12"])
    plt.title("Average Length of Song by Popular")
    plt.xlabel("Artist")
    plt.ylabel("Duration (Min)")
    plt.ylim(3.5,4)
    plt.savefig("DeezerBargraph.png")
    plt.show()
createvisual()