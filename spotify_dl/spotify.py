import sys
from spotify_dl.scaffold import log
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
        while True:
            items = sp.playlist_items(playlist_id=url, fields='items.track.name,items.track.artists(name),items.track.album(name),total,next,offset', additional_types=['track'], offset=offset)
            total_songs = items.get('total')
            for item in items['items']:
                track_name = item['track']['name']
                track_artist = ", ".join([artist['name'] for artist in item['track']['artists']])
                songs_dict.update({track_name: track_artist})
                offset += 1
            
            log.info(f"Fetched {offset}/{total_songs} songs in the playlist")                
            if total_songs == offset:
                log.info('All pages fetched, time to leave. Added %s songs in total', offset)
                break

    elif item_type == 'album':
        while True:
            items = sp.album_tracks(album_id=url)
            total_songs = items.get('total')
            for item in items['items']:
                track_name = item['name']
                track_artist = " ".join([artist['name'] for artist in item['artists']])
                songs_dict.update({track_name: track_artist})
                offset += 1

            log.info(f"Fetched {offset}/{total_songs} songs in the album")                
            if total_songs == offset:
                log.info('All pages fetched, time to leave. Added %s songs in total', offset)
                break

    elif item_type == 'track':
        items = sp.track(track_id=url)
        track_name = items['name']
        track_artist = " ".join([artist['name'] for artist in items['artists']])
        songs_dict.update({track_name: track_artist})
    return songs_dict


def parse_spotify_url(url):
    """
    Parse the provided Spotify playlist URL and determine if it is a playlist, track or album.
    :param url: URL to be parsed
    :param download_directory: Location where to save
    :param format_string: format string for the file conversion
    :return tuple indicating the type and id of the item
    """
    if url.startswith("spotify:"):
        log.error("Spotify URI was provided instead of a playlist/album/track URL.")
        sys.exit(1)
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
