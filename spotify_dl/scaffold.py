import logging
from os import getenv
import sentry_sdk

__all__ = ['log', 'check_for_tokens']

logging.basicConfig(level=logging.INFO,
                    format='%(message)s')

log = logging.getLogger('sdl')
sentry_sdk.init("https://7d74a39472c9449dac51eb24bb33bdc3@sentry.io/2383261")


def check_for_tokens():
    """
    Checks if the required API keys for Spotify has been set.
    :param name: Name to be cleaned up
    :return string containing the cleaned name
    """
    log.debug('Checking for tokens')
    CLIENT_ID = getenv('SPOTIPY_CLIENT_ID')
    CLIENT_SECRET = getenv('SPOTIPY_CLIENT_SECRET')
    log.debug("Tokens fetched: {} {}".format(CLIENT_ID, CLIENT_SECRET))

    if CLIENT_ID is None or CLIENT_SECRET is None:
        print('''
            You need to set your Spotify API credentials. You can do this by
            setting environment variables like so:

            export SPOTIPY_CLIENT_ID='your-spotify-client-id'
            export SPOTIPY_CLIENT_SECRET='your-spotify-client-secret'
            Get your credentials at
                https://developer.spotify.com/my-applications
        ''')
        return False
    return True
