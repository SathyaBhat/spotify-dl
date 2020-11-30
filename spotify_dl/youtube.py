from spotify_dl.scaffold import log
import youtube_dl
from os import path


def download_songs(songs, download_directory, format_string, skip_mp3):
    """
    Downloads songs from the YouTube URL passed to either current directory or download_directory, is it is passed.
    :param songs: Dictionary of songs and associated artist
    :param download_directory: Location where to save
    :param format_string: format string for the file conversion
    :param skip_mp3: Whether to skip conversion to MP3
    """
    log.debug(f"Downloading to {download_directory}")
    for song, artist in songs.items():
        query = f"{artist} - {song}".replace(":", "").replace("\"", "")
        download_archive = path.join(download_directory, 'downloaded_songs.txt')
        outtmpl = path.join(download_directory, '%(title)s.%(ext)s')
        ydl_opts = {
            'format': format_string,
            'download_archive': download_archive,
            'outtmpl': outtmpl,
            'default_search': 'ytsearch',
            'noplaylist': True,
            'postprocessor_args': ['-metadata', 'title=' + song,
                                   '-metadata', 'artist=' + artist]
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
                ydl.download([query])
            except Exception as e:
                log.debug(e)
                print('Failed to download: {}, please ensure YouTubeDL is up-to-date. '.format(query))
                continue
