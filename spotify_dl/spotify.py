import youtube_dl
from spotify_dl.scaffold import *
from spotify_dl.utils import sanitize


def fetch_tracks(sp, item_type, url):
    """
    Fetches tracks from the provided URL.
    :param sp: Spotify client
    :param type: Type of item being requested for: album/playlist/track
    :param url: URL of the item
    :return Dictionary of song and artist
    """
    songs_dict = {}
    offset = 0

    if item_type == 'playlist':
        items = sp.playlist_items(playlist_id=url, fields='items.track.name,items.track.artists(name),items.track.album(name),total,next,offset', additional_types=['track'])
        while True:
            for item in items['items']:
                track_name = item['track']['name']
                track_artist = " ".join([artist['name'] for artist in item['track']['artists']])
                songs_dict.update({track_name: track_artist})
                offset += 1

            if items.get('next') is None:
                log.info('All pages fetched, time to leave. Added %s songs in total', offset)
                break

    elif item_type == 'album':
        items = sp.album_tracks(album_id=url)
        while True:
            for item in items['items']:
                track_name = item['name']
                track_artist = " ".join([artist['name'] for artist in item['artists']])
                songs_dict.update({track_name: track_artist})
                offset += 1

            if items.get('next') is None:
                log.info('All pages fetched, time to leave. Added %s songs in total', offset)
                break

    elif item_type == 'track':
        items = sp.track(track_id=url)
        track_name = items['name']
        track_artist = " ".join([artist['name'] for artist in items['artists']])
        songs_dict.update({track_name: track_artist})
    return songs_dict


def download_songs(songs_dict, download_directory, format_string, skip_mp3):
    """
    Downloads songs from the YouTube URL passed to either current directory or download_directory, is it is passed.
    :param songs_dict: Dictionary of songs and associated artist
    :param download_directory: Location where to save
    :param format_string: format string for the file conversion
    :param skip_mp3: Whether to skip conversion to MP3
    """
    download_directory = f"{download_directory}\\"
    log.debug(f"Downloading to {download_directory}")
    for number, item in enumerate(songs_dict):
        log.debug('Songs to download: %s', item)
        
        url_, track_, artist_ = item
        download_archive = download_directory + 'downloaded_songs.txt'
        outtmpl = download_directory + '%(title)s.%(ext)s'
        ydl_opts = {
            'format': format_string,
            'download_archive': download_archive,
            'outtmpl': outtmpl,
            'noplaylist': True,
            'postprocessor_args': ['-metadata', 'title=' + str(track_),
                                   '-metadata', 'artist=' + str(artist_),
                                   '-metadata', 'track=' + str(number + 1)]
        }
        if not skip_mp3:
            mp3_postprocess_opts = {
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }
            ydl_opts['postprocessors'] = [mp3_postprocess_opts.copy()]

        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            try:
                log.debug(ydl.download([url_]))
            except Exception as e:
                log.debug(e)
                print('Failed to download: {}'.format(url_))
                continue


def parse_spotify_url(url):
    """
    Parse the provided Spotify playlist URL and determine if it is a playlist, track or album.
    :param url: URL to be parsed
    :param download_directory: Location where to save
    :param format_string: format string for the file conversion
    :return tuple indicating the type and id of the item
    """
    parsed_url = url.replace("https://open.spotify.com/", "")
    item_type = parsed_url.split("/")[0]
    item_id = parsed_url.split("/")[1]
    return item_type, item_id


def get_item_name(sp, item_type, item_id):
    """
    Fetch the name of the item.
    :param sp: Spotify Client
    :param item_type: Type of the item
    :param item_id: id of the item
    :return String indicating the name of the item
    """
    if item_type == 'playlist':
        name = sp.playlist(playlist_id=item_id, fields='name').get('name')
    elif item_type == 'album':
        name = sp.album(album_id=item_id).get('name')
    elif item_type == 'track':
        name = sp.track(track_id=item_id).get('name')
    return sanitize(name)


def validate_spotify_url(url):
    """
    Validate the URL and determine if the item type is supported.
    :return Boolean indicating whether or not item is supported
    """
    item_type, item_id = parse_spotify_url(url)
    log.debug(f"Got item type {item_type} and item_id {item_id}")
    if item_type not in ['album', 'track', 'playlist']:
        log.error("Only albums/tracks/playlists are supported")
        return False
    if item_id is None:
        log.error("Couldn't get a valid id")
        return False
    return True
