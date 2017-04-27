spotify\_dl
===========

Downloads songs from any Spotify playlist or from your "My Music"
collection.

Tell me more!
=============

I wanted an easy way to grab the songs present in my library so I can
download it & use it offline(Spotify still hasn't launched here. Y U NO
COME?). `spotify\_to\_mp3 <https://github.com/frosas/spotify-to-mp3>`__
worked well but it relied on grooveshark, which unfortunately is no
more.

So I wrote this script which mimics that library, but instead of
downloading from grooveshark, it provides you with a file of youtube
URLs which you can then plug into
`youtube-dl <https://rg3.github.io/youtube-dl/>`__

How do I get this thing running?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Pre-requisite: You need Python 3+

1. Install using pip ``sudo pip3 install spotify_dl`` (use ``pip`` if
   your distro natively provides Python 3)

2. Create your Spotify app & fetch the client id and client secret from
   `Spotify Developer
   Console <https://developer.spotify.com/my-applications/#!/applications>`__.
   These keys then need to be assigned as ``SPOTIPY_CLIENT_ID``,
   ``SPOTIPY_CLIENT_SECRET`` and ``SPOTIPY_REDIRECT_URI`` environment
   variables.

   You can set environment variables in Linux like so:

   ::

           export SPOTIPY_CLIENT_ID='your-spotify-client-id'
           export SPOTIPY_CLIENT_SECRET='your-spotify-client-secret'
           export SPOTIPY_REDIRECT_URI='your-app-redirect-url'

   Windows users, check for `this
   question <http://superuser.com/a/284351/4377>`__ for details on how
   you can set environment variables.

   Note the redirect URL can be a valid URL, just ensure it matches with
   what you have entered in the developer console & in the environment
   variable above.

3. Create your YouTube API key & fetch the keys from `Google Developer
   Console <https://console.developers.google.com/apis/api/youtube/overview>`__.
   Set the key as ``YOUTUBE_DEV_KEY`` environment variable as mentioned
   above.
4. Run the script using ``spotify_dl``. spotify\_dl accepts different
   parameters, for more details run ``spotify_dl -h``.

For most users
``spotify_dl -l spotify_playlist_link -o download_directory`` should do
where

-  ``spotify_playlist_link`` is a link to Spotify's playlist. You can
   get it from the 3-dot menu.

.. figure:: https://cloud.githubusercontent.com/assets/25424/25472453/f256c94a-2b48-11e7-8f91-7bfa1ce232c2.png
   :alt: image

   image

If the Spotify playlist link is skipped then it will download songs from
your "My Music" collection - ``download_directory`` is the location
where the songs must be downloaded to. If you give a ``.`` then it will
download to the current directory.

Alternatively,
``spotify_dl -p playlist_id -u user_name -o download_directory`` will
also work

-  ``playlist_id`` is the id of the playlist where songs need to be
   downloaded. If this is skipped then it will download songs ftom your
   "My Music" collection
-  ``user_name`` is the user name who created the playlist.
-  ``download_directory`` is the location where the songs must be
   downloaded to.

5. A first time run will require authentication; you will need to click
   on the URL prompted to authenticate. Once logged in, paste the URL
   back in.
6. To retrieve download songs as MP3, you will need to install ffmpeg.
   If you prefer to skip MP3 conversion, pass ``-m`` or ``--skip_mp3``
   as a parameter when running the script

-  Linux users can get them by installing libav-tools by using apt-get
   (``sudo apt-get install -y libav-tools``) or a package manager which
   comes with your distro
-  Windows users can download FFMPEG pre-built binaries from
   `here <http://ffmpeg.zeranoe.com/builds/>`__. Extract the file using
   `7-zip <http://7-zip.org/>`__ to a foldrer and `add the folder to
   your PATH environment
   variable <http://www.wikihow.com/Install-FFmpeg-on-Windows>`__

Credits
~~~~~~~

-  `rhnvrm <https://github.com/rhnvrm>`__ for `adding in
   youtube-dl <https://github.com/SathyaBhat/spotify-dl/pull/1>`__
-  `mr-karan <https://github.com/mr-karan>`__ for `adding save to
   directory <https://github.com/SathyaBhat/spotify-dl/pull/6>`__
-  `shantanugoel <https://github.com/shantanugoel>`__ for adding in
   `User playlist <https://github.com/SathyaBhat/spotify-dl/pull/7>`__,
   `skip MP3
   conversion <https://github.com/SathyaBhat/spotify-dl/pull/34>`__ and
   `Ability to use custom format string
   support <https://github.com/SathyaBhat/spotify-dl/pull/34>`__
-  `sildur <https://github.com/sildur>`__ for adding any `user playlist
   support and other
   fixes <https://github.com/SathyaBhat/spotify-dl/pulls?q=is%3Apr+author%3Asildur+is%3Aclosed>`__
-  `avinassh <https://github.com/avinassh>`__ for being a
   `Rockstar <https://github.com/avinassh/rockstar>`__ and not
   teleporting over to my house to kill me when I innundated him with
   questions
-  `doulwyi <https://github.com/doulwyi>`__ for adding id3 tagging and
   ability to parse Spotify URI
-  `Gowtham <https://github.com/HackToHell>`__ for `create playlist in
   download <https://github.com/SathyaBhat/spotify-dl/pull/23>`__
   directory

Issues, Feedback, Contact details
---------------------------------

Feel free to raise any bugs/issues under Github issues. Pull requests
are also more than welcome. You can reach me on twitter at
[@sathyabhat](https://twitter.com/sathyabhat) or drop an email
sathya@sathyasays.com
