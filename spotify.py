import os
import sys
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json
import spotipy.util as util
import sqlite3
from sqlite3 import Error
import matplotlib
import matplotlib.pyplot as plt

Spotify = spotipy.Spotify

base_url = 'https://api.spotify.com'
spo = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id="eacd478467a4479ab95ce3266ecd883f", client_secret="39965161aaa34305b5258d45ee088908" ))

def create_conn(file):
    conn = None
    try:
        conn = sqlite3.connect(file)
        return conn
    except Error as e:
        print(e)
    return conn


def table_db(conn, table):
    try:
        c = conn.cursor()
        c.execute(table)
    except Error as e:
        print(e)
       
def table_values(conn, sql, vals):
    try:
        c = conn.cursor()
        c.execute(sql, vals)
    except Error as e:
        pass

def transfer_to_database(playID, owner, db, table, sql_value):
    
    results = spo.user_playlist(owner, playID)
    results = results['tracks']['items']
    
    song_name = []
    popularity = []
    duration = []
    artist_name = []
    trackID = []
    album_name = []
    
   
    for result in results:
        song_name.append(result['track']['name'])
        duration.append(result['track']['duration_ms'])
        popularity.append(result['track']['popularity'])
        artist_name.append(result['track']['artists'][0]['name'])
        trackID.append(result['track']['id'])
        album_name.append(result['track']['album']['name'])
        
        
    conn = create_conn(db)
    table_db(conn, table)
    
    for iD, name, pop, dur, an, alb in zip(trackID, 
                                   song_name, 
                                   popularity, 
                                   duration, 
                                   artist_name, 
                                   album_name):
        values = (iD, name, pop, dur, an, alb)
        table_values(conn, sql_value, values)
        conn.commit()

results = spo.search("TOP 100 Songs of 2020 (Best Hit Music Playlist)", limit = 1, type='playlist')
playID =  results['playlists']['items'][0]['id']
owner = results['playlists']['items'][0]['owner']['id']
db = 'spotify_database.sqlite'
table = 'CREATE TABLE IF NOT EXISTS tracks(track_id CHAR(20) PRIMARY KEY, name TEXT, popularity INTEGER, duration_ms INTEGER, artist_name TEXT, album TEXT);'
sql_value = 'INSERT INTO tracks VALUES (?,?,?,?,?,?)'
transfer_to_database(playID, owner, db, table, sql_value)



conn = sqlite3.connect(db)
cur= conn.cursor()

cur.execute("SELECT name, duration_ms from tracks")
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
conn = sqlite3.connect('SpotifyCalculations.sqlite')
cur = conn.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS PythonCalc(name TEXT, avg_min FLOAT)')
cur.execute('INSERT INTO PythonCalc(name, avg_min) VALUES (?,?)', ("TOP 100 Songs of 2020",avg_min,))
conn.commit()

cur.execute('SELECT * FROM PythonCalc')
counter = 0
f = open("PythonSummary.txt", 'w')
for row in cur:
    counter += 1
    f.write("The average duration for songs in " + str(row[0]) + " is: " + str(row[1]) + " minutes" + "\n")
f.close()


def createvisual():
    conn = sqlite3.connect(db) 
    cur = conn.cursor()
    dur = []
    cur.execute("SELECT * from tracks")
    for row in cur:
        dur.append(float(row[3]))
    
    x = range(100)
    plt.scatter(x, dur, color='#0000ff', alpha=0.5)
    plt.title('Scatter Plot for Top 100 Duration')
    plt.xlabel('Top 100 song placement')
    plt.ylabel('Duration (ms)')
    plt.show()

createvisual()