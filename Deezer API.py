#Deezer Info 
import requests
import json
import sqlite3 
url = "https://deezerdevs-deezer.p.rapidapi.com/search"
querystring = {"q":"eminem"}
headers = {
    'x-rapidapi-key': "e8987c562amsh78b1a8d73318a6fp16a5aajsn465e38986a0e",
    'x-rapidapi-host': "deezerdevs-deezer.p.rapidapi.com"
    }
response = requests.request("GET", url, headers=headers, params = querystring)
def music():
    conn = sqlite3.connect("fifth.sqlite")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS DeezerData(id TEXT, artistName TEXT, ranking FLOAT, trackTimeMillis FLOAT)")
    print(response.json())
    text = json.loads(response.text) 
    data = text.get('data')
    #data = text.get('data')
    print(data)
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
music()


'''def getData(d):
    conn = sqlite3.connect("fifth.sqlite")
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS DeezerData(id TEXT UNIQUE, artistName TEXT, ranking FLOAT, trackTimeMillis FLOAT)")
'''

    
    
    
    
    
    
    
    
'''
#Deezer API
import requests 
import json 
#base_url = 'https://api.deezer.com/version/service/id/method/?parameters'
response = requests.get("https://api.deezer.com/chart/artists") #go get info from URL and package info and put it into response object
print(response.json()) #print(response.status_code) #get status code classdeezer.client.Client(app_id=None, app_secret=None, access_token=None, headers=None, **kwargs)
text = json.loads(response.text) #convert to dictionary 
artists = text.get('artists')
data = artists.get('data')
print(data)
for info in data: 
    id_num = info['id']
    name = info['name']
    rank = info['position']
    id_num = info['id']
    print(id_num)
    print(name)
    print(rank)
    
'''


    