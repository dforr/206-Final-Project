import os
import sys
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import json
import spotipy.util as util

Spotify = spotipy.Spotify

base_url = 'https://api.spotify.com'
sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id="eacd478467a4479ab95ce3266ecd883f", client_secret="39965161aaa34305b5258d45ee088908" ))



import sqlite3
from sqlite3 import Error

## write some functions to create batabase table and insert values
def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return conn


## Creating table function
def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

## function to insert values        
def insert_values(conn, sql_statement, values):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(sql_statement, values)
    except Error as e:
        pass

def getting_playlist_data_to_database(playlist_id, playlist_owner, db, sql_table_statement, sql_value_statement):
    
    ## Getting a bit cleaned up. 
    results = sp.user_playlist(playlist_owner, playlist_id)
    results = results['tracks']['items']
    
    
    ## initializing some lists.
    track_name = []
    track_popularity = []
    duration_ms = []
    artist_name = []
    track_id = []
    album_name = []
    release_date = []
    
    ## just going through the spotify object and retriving data. 
    for result in results:
        track_name.append(result['track']['name'])
        duration_ms.append(result['track']['duration_ms'])
        track_popularity.append(result['track']['popularity'])
        artist_name.append(result['track']['artists'][0]['name'])
        track_id.append(result['track']['id'])
        album_name.append(result['track']['album']['name'])
        release_date.append(result['track']['album']['release_date'])
        
    ## creating a connection with database
    conn = create_connection(db)
    create_table(conn, sql_table_statement)
    
    ## looping through all the lists and inserting values. 
    for i, n, p, d, at, alb, dt in zip(track_id, 
                                   track_name, 
                                   track_popularity, 
                                   duration_ms, 
                                   artist_name, 
                                   album_name, 
                                   release_date):
        values = (i, n, p, d, at, alb, dt)
        insert_values(conn, sql_value_statement, values)
        conn.commit()




results = sp.search("TOP 100 Songs of 2020 (Best Hit Music Playlist)", limit = 1, type='playlist')



playlist_id =  results['playlists']['items'][0]['id']
playlist_owner = results['playlists']['items'][0]['owner']['id']
sqlite_db = '260.sqlite'
sql_table = 'CREATE TABLE IF NOT EXISTS tracks(track_id CHAR(20) PRIMARY KEY, name TEXT, popularity INTEGER, duration_ms INTEGER, artist_name TEXT, album TEXT, release_date TEXT);'
value_statement = 'INSERT INTO tracks VALUES (?,?,?,?,?,?,?)'

getting_playlist_data_to_database(playlist_id, playlist_owner, sqlite_db, sql_table, value_statement)