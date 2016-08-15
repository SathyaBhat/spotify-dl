from googleapiclient.discovery import build
from spotify_dl.constants import YOUTUBE_API_SERVICE_NAME
from spotify_dl.constants import YOUTUBE_API_VERSION
from spotify_dl.constants import VIDEO
from spotify_dl.constants import YOUTUBE_VIDEO_URL
from spotify_dl.scaffold import log
from os import getenv


def fetch_youtube_url(search_term):
    """For each song name/artist name combo, fetch the YouTube URL
        and return the list of URLs"""
    YOUTUBE_DEV_KEY = getenv('YOUTUBE_DEV_KEY')
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                    developerKey=YOUTUBE_DEV_KEY)
    log.info(u"Searching for {}".format(search_term))
    search_response = youtube.search().list(q=search_term,
                                            part='id, snippet').execute()
    for v in search_response['items']:
        if v['id']['kind'] == VIDEO:
            log.debug("Adding Video id {}".format(v['id']['videoId']))
            return YOUTUBE_VIDEO_URL + v['id']['videoId']
