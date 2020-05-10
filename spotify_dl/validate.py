
def validate_spotify_playlist_url(playlist_url):
    url_match = playlist_url_pattern.match(args.url)
    if args.url and url_match and len(url_match.groups()) > 0:
        uri = "spotify:" + url_match.groups()[0].replace('/', ':')
        args.uri = [uri]
    else:
        raise Exception('Invalid playlist URL ')