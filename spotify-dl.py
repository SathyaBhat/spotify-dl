from scaffold import *
from spotify import authenticate
from spotify import fetch_saved_tracks
from spotify import save_songs_to_file
from youtube import fetch_youtube_url
import spotipy


if __name__ == '__main__':
    log.info('Starting spotify-dl')
    token = authenticate()
    sp = spotipy.Spotify(auth=token)
    songs = fetch_saved_tracks(sp)
    url = []
    for s in songs:
        url.append(fetch_youtube_url(s))
    save_songs_to_file(url)