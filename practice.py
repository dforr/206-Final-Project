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
