import requests
import pprint
import json
import sqlite3

def getItunes(base_url):
    offset=0
    b = requests.get(base_url).json()
    return b


def getData(c):
    
    conn = sqlite3.connect("fifth.sqlite") 
    cur = conn.cursor()
    #Also do it here
    cur.execute("CREATE TABLE IF NOT EXISTS ItunesData(id TEXT UNIQUE, artistName TEXT, trackTimeMillis FLOAT, trackName TEXT)")
    counter = 0
    for x in c['results']:
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
        print(_id)
        print(_artistName)
        print(_trackTimeMillis)
        print(_trackName)
        print('\n')
        #offset += 1
        #INSERT OR IGNORE INTO ... These are the column names. 
        # Add a column name in the orange
        # You must also add the underscored columnname in the white, also add question mark
        cur.execute('INSERT OR IGNORE INTO ItunesData(id, artistName, trackTimeMillis, trackName) VALUES (?,?,?,?)', (_id, _artistName, _trackTimeMillis, _trackName))
        conn.commit()


data2 = getItunes("https://itunes.apple.com/search?term=taylor+swift&limit=25&offset=offset")
getData(data2)


#data = getItunes("https://itunes.apple.com/search?term=justin+bieber")
#data1 = getItunes("https://itunes.apple.com/search?term=halsey")
##data2 = getItunes("https://itunes.apple.com/search?term=taylor+swift&limit=25&offset=")
#print(data)
#getData(data)
#getData(data1)
#getData(data2)