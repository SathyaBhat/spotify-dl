import spotipy.util as util
from scaffold import *
from tokens import *


def authenticate():
    return util.prompt_for_user_token(username,scope, CLIENT_ID, CLIENT_SECRET, REDIRECT_URL)


def fetch_saved_tracks(sp):
    offset = 0
    songs = []
    while True:
        results = sp.current_user_saved_tracks(limit=50, offset=offset)
        log.info('Got result json {}'.format(results))
        for item in results['items']:
            track = item['track']
            log.info('Appending {} to songs list'.format(track['name'] + ' - ' + track['artists'][0]['name']))
            songs.append(track['name'] + ' - ' + track['artists'][0]['name'])
            offset += 1

        if results.get('next') is None:
            log.info('All pages fetched, time to leave')
            break
    return songs


def save_songs_to_file(songs):
    with open('songs.txt', 'a') as f:
        f.write('\n'.join(songs))
    f.close()