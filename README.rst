spotify\_dl
===========

Downloads songs from any Spotify playlist or from your “My Music”
collection.

Tell me more!
=============

I wanted an easy way to grab the songs present in my library so I can
download it & use it offline(Spotify still hasn’t launched here. Y U NO
COME?). `spotify\_to\_mp3`_ worked well but it relied on grooveshark,
which unfortunately is no more.

So I wrote this script which mimics that library, but instead of
downloading from grooveshark, it provides you with a file of youtube
URLs which you can then plug into `youtube-dl`_

How do I get this thing running?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Pre-requisite: You need Python 3+

1. Install using pip ``sudo pip3 install spotify_dl`` (use ``pip`` if
   your distro natively provides Python 3)

2. Create your Spotify app & fetch the client id and client secret from
   `Spotify Developer Console`_. These keys then need to be assigned as
   ``SPOTIPY_CLIENT_ID``, ``SPOTIPY_CLIENT_SECRET`` and
   ``SPOTIPY_REDIRECT_URI`` environment variables.

   You can set environment variables in Linux like so:

   ::

           export SPOTIPY_CLIENT_ID='your-spotify-client-id'
           export SPOTIPY_CLIENT_SECRET='your-spotify-client-secret'
           export SPOTIPY_REDIRECT_URI='your-app-redirect-url'

   Windows users, check for `this question`_ for details on how you can
   set environment variables.

   Note the redirect URL can be a valid URL, just ensure it matches with
   what you have entered in the developer console & in the environment
   variable above.

3. Create your YouTube API key & fetch the keys from `Google Developer
   Console`_. Set the key as ``YOUTUBE_DEV_KEY`` environment variable as
   mentioned above.
4. Run the script using ``spotify_dl``. spotify\_dl accepts different
   parameters, for more details run ``spotify_dl -h``. For most users
   ``spotify_dl -d -p playlist_id -u user_name -o download_directory``
   should do where

-  ``playlist_id`` is the id of the playlist where songs need to be
   downloaded. If this is skipped then it will download songs ftom your
   “My Music” collection
-  ``user_name`` is the user name who created the playlist.
-  ``download_directory`` is the location where the songs must be
   downloaded to.

5. A first time run will require authentication; you will need to click
   on the URL prompted to authenticate. Once logged in, paste the URL
   back in.
6. To retrieve download songs as MP3, you will need to install ffmpeg.

-  Linux users can get them by installing libav-tools by using apt-get
   (``sudo apt-get install -y libav-tools``) or a package manager which
   comes with your distro
-  Windows users can download FFMPEG pre-built binaries from `here`_.
   Extract the file using `7-zip`_ to a foldrer and [add the folder to
   your PATH environment variable](http

.. _spotify\_to\_mp3: https://github.com/frosas/spotify-to-mp3
.. _youtube-dl: https://rg3.github.io/youtube-dl/
.. _Spotify Developer Console: https://developer.spotify.com/my-applications/#!/applications
.. _this question: http://superuser.com/a/284351/4377
.. _Google Developer Console: https://console.developers.google.com/apis/api/youtube/overview
.. _here: http://ffmpeg.zeranoe.com/builds/
.. _7-zip: http://7-zip.org/
