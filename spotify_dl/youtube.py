from os import getenv

from googleapiclient.discovery import build
from googleapiclient.http import HttpError
from sentry_sdk import capture_exception


from spotify_dl.constants import YOUTUBE_API_SERVICE_NAME
from spotify_dl.constants import YOUTUBE_API_VERSION
from spotify_dl.constants import VIDEO
from spotify_dl.constants import YOUTUBE_VIDEO_URL
from spotify_dl.scaffold import log
from json import loads
import requests
from lxml import html
import re


from click import secho

def fetch_youtube_url(search_term, dev_key=None, scrape=False):
    """For each song name/artist name combo, fetch the YouTube URL
        and return the list of URLs"""
    log.info(f"Searching for {search_term}")
    if scrape or not dev_key:
        YOUTUBE_SEARCH_BASE = "https://www.youtube.com/results?search_query="
        try:
            response = requests.get(YOUTUBE_SEARCH_BASE + search_term).content
            html_response = html.fromstring(response)
            video = html_response.xpath("//a[contains(@class, 'yt-uix-tile-link')]/@href")
            video_id = re.search("((\?v=)[a-zA-Z0-9_-]{4,15})", video[0]).group(0)[3:]
            log.debug(f"Found video id {video_id} for search term {search_term}")
            return YOUTUBE_VIDEO_URL + video_id
        except AttributeError as e:
            log.warn(f"Could not find scrape details for {search_term}")
            capture_exception(e)
            return None
        except IndexError as e:
            log.warn(f"Could not perform scrape search for {search_term}, diff HTML")
            capture_exception(e)
            return None
    else:
        YOUTUBE_DEV_KEY = dev_key
        youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                        developerKey=YOUTUBE_DEV_KEY,
                        cache_discovery=False)
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