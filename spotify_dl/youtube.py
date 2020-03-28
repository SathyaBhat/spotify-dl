from os import getenv

from googleapiclient.discovery import build
from googleapiclient.http import HttpError


from spotify_dl.constants import YOUTUBE_API_SERVICE_NAME
from spotify_dl.constants import YOUTUBE_API_VERSION
from spotify_dl.constants import VIDEO
from spotify_dl.constants import YOUTUBE_VIDEO_URL
from spotify_dl.scaffold import log
from json import loads

from click import secho

def fetch_youtube_url(search_term, dev_key):
    """For each song name/artist name combo, fetch the YouTube URL
        and return the list of URLs"""
    YOUTUBE_DEV_KEY = dev_key
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                    developerKey=YOUTUBE_DEV_KEY,
                    cache_discovery=False)
    log.info(u"Searching for {}".format(search_term))
    try:
        search_response = youtube.search().list(q=search_term,
                                                part='id, snippet').execute()
        for v in search_response['items']:
            if v['id']['kind'] == VIDEO:
                log.debug("Adding Video id {}".format(v['id']['videoId']))
                return YOUTUBE_VIDEO_URL + v['id']['videoId']
    except HttpError as err: 
        err_details = loads(err.content.decode('utf-8')).get('error').get('errors')
        secho("Couldn't complete search due to following errors: ", fg='red')
        for e in err_details:
            error_reason = e.get('reason')
            error_domain = e.get('domain')
            error_message = e.get('message')

            if error_reason == 'quotaExceeded' or error_reason == 'dailyLimitExceeded':
                secho(f"\tYou're over daily allowed quota. Unfortunately, YouTube restricts API keys to a max of 10,000 requests per day which translates to a maximum of 100 searches.", fg='red')
                secho(f"\tThe quota will be reset at midnight Pacific Time (PT)." ,fg='red')
                secho(f"\tYou can request for Quota increase from https://console.developers.google.com/apis/api/youtube.googleapis.com/quotas.", fg='red')
            else:
                secho(f"\t Search failed due to {error_domain}:{error_reason}, message: {error_message}")
        return None
    
def get_youtube_dev_key():
    return getenv('YOUTUBE_DEV_KEY')
