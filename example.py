from spotipy.oauth2 import SpotifyClientCredentials
import spotipy

sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id="eacd478467a4479ab95ce3266ecd883f", client_secret="39965161aaa34305b5258d45ee088908" ))

pl_id = 'spotify:playlist:37i9dQZEVXbLRQDuF5jeBp'
offset = 0

while True:
    response = sp.playlist_items(pl_id,
                                 offset=offset,
                                 fields='items.track.name,total', limit = 100,
                                 additional_types=['track'])
    
    if len(response['items']) == 0:
        break
    
    print(response['items'])
    offset = offset + len(response['items'])
    print(offset, "/", response['total'])