from googleapiclient.discovery import build
from tokens import YOUTUBE_DEV_KEY
from constants import YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, VIDEO, YOUTUBE_VIDEO_URL
from scaffold import log

def fetch_youtube_url(search_term):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION, developerKey=YOUTUBE_DEV_KEY)
    log.info(u"Searching for {}".format(search_term))
    search_response = youtube.search().list(q=search_term, part='id, snippet').execute()
    for v in search_response['items']:
        if v['id']['kind'] == VIDEO:
            log.debug("Adding Video id {}".format(v['id']['videoId']))
            return YOUTUBE_VIDEO_URL + v['id']['videoId']
