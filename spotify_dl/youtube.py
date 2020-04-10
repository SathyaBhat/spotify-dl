from os import getenv


from spotify_dl.constants import YOUTUBE_API_SERVICE_NAME
from spotify_dl.constants import YOUTUBE_API_VERSION
from spotify_dl.constants import VIDEO
from spotify_dl.constants import YOUTUBE_VIDEO_URL
from spotify_dl.scaffold import log
import requests

from click import secho
headers = {
  'x-youtube-ad-signals': 'dt=1586550729813&flash=0&frm&u_tz=270&u_his=4&u_java&u_h=1080&u_w=1920&u_ah=1053&u_aw=1920&u_cd=24&u_nplug=2&u_nmime=2&bc=31&bih=953&biw=1105&brdim=0%2C59%2C0%2C59%2C1920%2C27%2C1920%2C1021%2C1120%2C953&vis=1&wgl=true&ca_type=image',
  'x-youtube-client-name': '1',
  'x-youtube-page-label': 'youtube.ytfe.desktop_20200405_6_RC2',
  'x-youtube-page-cl': '305312232',
  'x-youtube-variants-checksum': 'be75f5f350742e06b11e18727c7bdd45',
  'x-youtube-sts': '18359',
  'x-youtube-device': 'cbr=Chrome&cbrver=80.0.3987.116&ceng=WebKit&cengver=537.36&cos=X11',
  'x-youtube-client-version': '2.20200406.06.02',
  'Cookie': 'VISITOR_INFO1_LIVE=M_Zf0Pgjif0; YSC=R-lEqjAg97w; GPS=1'
}
def fetch_youtube_url(search_term):
    """For each song name/artist name combo, fetch the YouTube URL
        and return the list of URLs"""

    log.info(u"Searching for {}".format(search_term))
    try:
        r = requests.get("https://www.youtube.com/results?search_query={}&pbj=1".format(search_term), headers=headers)
        resp = r.json()
        c1=next(filter(lambda x: x.get("response",None), resp))["response"]["contents"]["twoColumnSearchResultsRenderer"]["primaryContents"]["sectionListRenderer"]["contents"]
        c2=next(filter(lambda x: x.get("itemSectionRenderer",None),c1))["itemSectionRenderer"]["contents"]
        video_id=next(filter(lambda x: x.get("videoRenderer",None), c2))["videoRenderer"]["videoId"]
        return YOUTUBE_VIDEO_URL + video_id
    except StopIteration:
        log.error("Could not found any youtube video corresponding to {}".format(" ".join(search_term.split("+"))))
