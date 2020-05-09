import logging
from os import getenv
import sentry_sdk

__all__ = ['log', 'check_for_tokens']

logging.basicConfig(level=logging.INFO,
                    format='%(message)s')

log = logging.getLogger('sdl')
sentry_sdk.init("https://7d74a39472c9449dac51eb24bb33bdc3@sentry.io/2383261")


def check_for_tokens():
    log.debug('Checking for tokens')
    CLIENT_ID = getenv('SPOTIPY_CLIENT_ID')
    CLIENT_SECRET = getenv('SPOTIPY_CLIENT_SECRET')
    REDIRECT_URL = getenv('SPOTIPY_REDIRECT_URI')
    log.debug("Tokens fetched: {} {} {}".format(CLIENT_ID, CLIENT_SECRET,
                                                REDIRECT_URL))

    if CLIENT_ID is None or CLIENT_SECRET is None or REDIRECT_URL is None:
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

    YOUTUBE_DEV_KEY = getenv('YOUTUBE_DEV_KEY')
    log.debug("YouTube dev key: {}".format(YOUTUBE_DEV_KEY))
    if YOUTUBE_DEV_KEY is None:
        print('''
            Youtube Data API token has not been setup. You can do this by
            setting environment variables like so:

            export YOUTUBE_DEV_KEY='your-youtube-dev-key'

            Generate the key from
            https://console.developers.google.com/apis/api/youtube/overview
            
            Using HTML Scraper as a fallback.
            ''')
    return True
