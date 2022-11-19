import logging
from os import getenv
import sentry_sdk
from rich.logging import RichHandler
from rich.console import Console

__all__ = ["log", "get_tokens", "console"]

logging.basicConfig(
    level=logging.INFO,
    format="%(message)s",
    datefmt="[%X]",
    handlers=[RichHandler(show_level=False, show_time=False)],
)
console = Console()
log = logging.getLogger("sdl")
sentry_sdk.init(
    "https://fc66a23d79634b9bba1690ea13e289f0@o321064.ingest.sentry.io/2383261"
)


def get_tokens():
    """
    Checks if the required API keys for Spotify has been set.
    :param name: Name to be cleaned up
    :return string containing the cleaned name
    """
    log.debug("Checking for tokens")
    CLIENT_ID = getenv("SPOTIPY_CLIENT_ID")
    CLIENT_SECRET = getenv("SPOTIPY_CLIENT_SECRET")
    log.debug("Tokens fetched : %s %s ", CLIENT_ID, CLIENT_SECRET)

    if CLIENT_ID is None or CLIENT_SECRET is None:
        print(
            """
            You need to set your Spotify API credentials. You can do this by
            setting environment variables like so:
            Linux:
            export SPOTIPY_CLIENT_ID='your-spotify-client-id'
            export SPOTIPY_CLIENT_SECRET='your-spotify-client-secret'

            Windows Powershell:
            $env:SPOTIPY_CLIENT_ID='your-spotify-client-id'
            $env:SPOTIPY_CLIENT_SECRET='your-spotify-client-secret'

            Windows CMD:
            set SPOTIPY_CLIENT_ID=your-spotify-client-id
            set SPOTIPY_CLIENT_SECRET=your-spotify-client-secret

            Get your credentials at
                https://developer.spotify.com/my-applications
        """
        )
        return None
    return CLIENT_ID, CLIENT_SECRET
