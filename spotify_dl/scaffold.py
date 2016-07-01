import logging
import os
import spotify_dl.tokens as tokens

__all__ = ['log', 'check_for_tokens']

logging.basicConfig(level=logging.INFO,
               format='%(levelname)s: %(asctime)s - %(funcName)s - %(message)s')

log = logging.getLogger('sdl')


def check_for_tokens():
    log.debug('Checking for tokens')
    tokens.client_id = os.getenv('SPOTIPY_CLIENT_ID')
    tokens.client_secret = os.getenv('SPOTIPY_CLIENT_SECRET')
    tokens.redirect_url = os.getenv('SPOTIPY_REDIRECT_URI')
    log.debug("Tokens fetched: {} {} {}".format(tokens.CLIENT_ID, tokens.CLIENT_SECRET, tokens.REDIRECT_URL))

    if tokens.client_id is None or tokens.client_secret is None or tokens.redirect_url is None:
        print('''
            You need to set your Spotify API credentials. You can do this by
            setting environment variables like so:

            export SPOTIPY_CLIENT_ID='your-spotify-client-id'
            export SPOTIPY_CLIENT_SECRET='your-spotify-client-secret'
            export SPOTIPY_REDIRECT_URI='your-app-redirect-url'

            Get your credentials at
                https://developer.spotify.com/my-applications
        ''')
        return False

    tokens.youtube_dev_key = os.getenv('YOUTUBE_DEV_KEY')

    if tokens.youtube_dev_key is None:
        print('''
            You need to setup Youtube Data API token. You cna do this by
            setting environment variables like so:

            export YOUTUBE_DEV_KEY='your-youtube-dev-key'

            Generate the key from https://console.developers.google.com/apis/api/youtube/overview
            ''')
        return False
    return True
