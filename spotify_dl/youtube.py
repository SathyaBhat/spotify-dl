import urllib.request
from os import path

import youtube_dl
from mutagen.easyid3 import EasyID3
from mutagen.id3 import APIC, ID3
from mutagen.mp3 import MP3

from spotify_dl.scaffold import log


def download_songs(songs, download_directory, format_string, skip_mp3):
    """
    Downloads songs from the YouTube URL passed to either current directory or download_directory, is it is passed.
    :param songs: Dictionary of songs and associated artist
    :param download_directory: Location where to save
    :param format_string: format string for the file conversion
    :param skip_mp3: Whether to skip conversion to MP3
    """
    log.debug(f"Downloading to {download_directory}")
    for song in songs:
        query = f"{song.get('artist')} - {song.get('name')} Lyrics".replace(":", "").replace("\"", "")
        download_archive = path.join(download_directory, 'downloaded_songs.txt')
        outtmpl = path.join(download_directory, f"{song.get('artist')} - {song.get('name')}.%(ext)s")
        ydl_opts = {
            'format': format_string,
            'download_archive': download_archive,
            'outtmpl': outtmpl,
            'default_search': 'ytsearch',
            'noplaylist': True,
            'postprocessor_args': ['-metadata', 'title=' + song.get('name'),
                                   '-metadata', 'artist=' + song.get('artist'),
                                   '-metadata', 'album=' + song.get('album')]
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

        if not skip_mp3:
            song_file = MP3(path.join(download_directory, f"{song.get('artist')} - {song.get('name')}.mp3"),
                            ID3=EasyID3)
            song_file['date'] = song.get('year')
            song_file['tracknumber'] = str(song.get('num')) + '/' + str(song.get('num_tracks'))
            song_file['genre'] = song.get('genre')
            song_file.save()
            song_file = MP3(path.join(download_directory, f"{song.get('artist')} - {song.get('name')}.mp3"),
                            ID3=ID3)
            song_file.tags['APIC'] = APIC(
                encoding=3,
                mime='image/jpeg',
                type=3, desc=u'Cover',
                data=urllib.request.urlopen(song.get('cover')).read()
            )
            song_file.save()
            
