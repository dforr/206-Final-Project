import os
import sys
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json
import spotipy.util as util
import pandas as pd
from pandas.io import sql
import sqlite3
from sqlite3 import Error

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
                                   album_name, 
                                   ):
        values = (iD, name, pop, dur, an, alb)
        table_values(conn, sql_value, values)
        conn.commit()

#def Q(input_string, db = conn):
    #return pd.read_sql(input_string, db)

def main():
    results = spo.search("TOP 100 Songs of 2020 (Best Hit Music Playlist)", limit = 1, type='playlist')
    playID =  results['playlists']['items'][0]['id']
    owner = results['playlists']['items'][0]['owner']['id']
    db = 'dbspo.sqlite'
    #conn = sqlite3.connect(db)
    table = 'CREATE TABLE IF NOT EXISTS tracks(track_id CHAR(20) PRIMARY KEY, name TEXT, popularity INTEGER, duration_ms INTEGER, artist_name TEXT, album TEXT);'
    sql_value = 'INSERT INTO tracks VALUES (?,?,?,?,?,?)'
    transfer_to_database(playID, owner, db, table, sql_value)

    #Q('SELECT COUNT(*) FROM tracks')
   

    

if __name__ == '__main__':
    main()