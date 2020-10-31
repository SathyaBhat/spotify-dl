from spotipy.oauth2 import SpotifyClientCredentials
from spotify_dl.spotify import fetch_tracks
import spotipy


def spotify_auth():
    client = spotipy.Spotify(auth_manager=SpotifyClientCredentials())
    return client

def test_spotify_playlist_fetch():
    sp = spotify_auth()
    url = "https://open.spotify.com/playlist/1EqaIF6DswCUE0I6gAzQQv?si=9BzJyGNRSGOZ-nsL66WmmA"
    item_type = "playlist"
    songs = fetch_tracks(sp, item_type, url)
    assert {'Hotel California - Live On MTV, 1994':'Eagles'} == songs

def test_spotify_track_fetch():
    sp = spotify_auth()
    url = "https://open.spotify.com/track/2GpBrAoCwt48fxjgjlzMd4?si=xzZIHC5hSGuSEAXXkxgKiw"
    item_type = "track"
    songs = fetch_tracks(sp, item_type, url)
    assert {'Hotel California - Live On MTV, 1994':'Eagles'} == songs

def test_spotify_album_fetch():
    sp = spotify_auth()
    url = "https://open.spotify.com/album/1IVEQdX6Y37za9PMB0afPX?si=Hz8CMaYpTx2O0PeuDglKaA"
    item_type = "album"
    songs = fetch_tracks(sp, item_type, url)
    assert {'Simple Song':'The Shins'} == songs
