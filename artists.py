import requests
import json
import unittest
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

#eacd478467a4479ab95ce3266ecd883f




base_url = 'spotify:artist:1dfeR4HaWDbWqFHLkxsg1d'
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id="eacd478467a4479ab95ce3266ecd883f", client_secret="39965161aaa34305b5258d45ee088908" ))

test = spotify.new_releases(country=None, limit=5, offset=0)
print(test)

import requests
import json
import unittest
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

#eacd478467a4479ab95ce3266ecd883f

base_url = 'spotify:artist:1dfeR4HaWDbWqFHLkxsg1d'
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id="eacd478467a4479ab95ce3266ecd883f", client_secret="39965161aaa34305b5258d45ee088908" ))

test = spotify.new_releases(country=None, limit=5, offset=0)
print(test)

def find_artists(name_of_artist):
    artist_lst = []

    if "Featuring" in name_of_artist: 
        newname = name_of_artist.split("Featuring")
        artist_list.append(newname[0].strip())
    elif "DJ" in name_of_artist:
        newname = name_of_artist.split("DJ")
        artist_lst.append(name_name[1].strip()) 
    elif "&" in name_of_artist: 
        list_of_and = []
        newname = name_of_artist.split("&")
        list_of_and.append(newname[1].strip())
        if "," in newname[0]:
            add = new_name[0].split(",")
            for s in range(len(add)):
                artist_lst.append(add[s].strip())
                artist_lst.append(list_of_and[0].strip())
        else: 
            artist_lst.append(newname[0].strip())
            artist_lst.append(list_of_and[0].strip())
    elif " X " in artists_name: 
        newname = name_of_artist.split("X")
        artist_lst.append(newname[1].strip())
        artist_lst.append(newname[0].strip())
    elif " x " in artists_name: 
        newname = artists_name.split("x")
        artist_lst.append(newname[0].strip())
        artist_lst.append(newname[1].strip())
    elif "Duet With" in name_of_artist:
        newname = name_of_artist.split("Duet With")
        artist_lst.append(newname[0].strip())
        artist_lst.append(newname[1].strip())
    elif "Presents" in name_of_artist: 
        newname = name_of_artist.split("Presents")
        artist_lst.append(newname[0].strip())
    else: 
        artist_lst.append(name_of_artist)
    return artist_lst

def set_up_spotify_table(cur, conn): 
    cur.execute("CREATE TABLE IF NOT EXISTS Spotify_Data (name TEXT)")
    tup_list = join_tables(cur, conn)
    for tup in tup_list: 
        if_discovered = False 
        artists_name = tup[1]
        artist_name = find_artists(artists_name)
    
#results = spotify.artist_top_tracks(base_url, country= "US")
#test = tracks["album"]["name"]
#print(test)


#results = spotify.artist_albums(base_url, album_type='album')
#albums = results['items']
#while results['next']:
    #results = spotify.next(results)
    #albums.extend(results['items'])

#for album in albums:
    #print(album['name'])
    


#base_url = 'https://api.spotify.com'

#def get_data(top_artists):
    #base_url = 'https://api.spotify.com'
    #request = reguests.get(base.url).text
    #return json.loads(request)
