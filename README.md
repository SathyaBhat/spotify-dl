# spotify_dl
Downloads songs from any Spotify playlist or from your "My Music" collection.

[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)
[![PyPI download month](https://img.shields.io/pypi/dm/spotify_dl.svg)](https://pypi.python.org/pypi/spotify_dl/)
[![PyPI license](https://img.shields.io/pypi/l/spotify_dl.svg)](https://pypi.python.org/pypi/spotify_dl/)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/spotify_dl.svg)](https://pypi.python.org/pypi/spotify_dl/)
[![GitHub release](https://img.shields.io/github/release/SathyaBhat/spotify-dl.svg)](https://GitHub.com/SathyaBhat/spotify-dl/releases/)
[![GitHub stars](https://img.shields.io/github/stars/SathyaBhat/spotify-dl.svg?style=social&label=Star&maxAge=2592000)](https://GitHub.com/SathyaBhat/spotify-dl/stargazers/)
[![GitHub contributors](https://img.shields.io/github/contributors/SathyaBhat/spotify-dl.svg)](https://GitHub.com/SathyaBhat/spotify-dl/graphs/contributors/)

[![Awesome Badges](https://img.shields.io/badge/badges-awesome-green.svg)](https://github.com/Naereen/badges)


# Tell me more!
I wanted an easy way to grab the songs present in my library so I can download it & use it offline(Spotify still hasn't launched here. Y U NO COME?). [spotify_to_mp3](https://github.com/frosas/spotify-to-mp3) worked well but it relied on grooveshark, which unfortunately is no more.

So I wrote this script which mimics that library, but instead of downloading from grooveshark, it provides you with a file of youtube URLs which you can then plug into [youtube-dl](https://rg3.github.io/youtube-dl/)

### How do I get this thing running?

Pre-requisite: You need Python 3+

1. Install using pip 
      `sudo pip3 install spotify_dl` 
  (use `pip` if your distro natively provides Python 3)

2. Create your Spotify app & fetch the client id and client secret from [Spotify Developer Console](https://developer.spotify.com/my-applications/#!/applications). These keys then need to be assigned as `SPOTIPY_CLIENT_ID`, `SPOTIPY_CLIENT_SECRET` and `SPOTIPY_REDIRECT_URI` environment variables. 

    You can set environment variables in Linux like so:

            export SPOTIPY_CLIENT_ID='your-spotify-client-id'
            export SPOTIPY_CLIENT_SECRET='your-spotify-client-secret'
            export SPOTIPY_REDIRECT_URI='your-app-redirect-url'

    Windows users, check for [this question](http://superuser.com/a/284351/4377) for details on how you can set environment variables.

    Note the redirect URL can be a valid URL, just ensure it matches with what you have entered in the developer console & in the environment variable above.

3. Create your YouTube API key & fetch the keys from [Google Developer Console](https://console.developers.google.com/apis/api/youtube/overview). Set the key as `YOUTUBE_DEV_KEY` environment variable as mentioned above.
4. Run the script using `spotify_dl`. spotify_dl accepts different parameters, for more details run `spotify_dl -h`. 

   For most users `spotify_dl -l spotify_playlist_link -o download_directory` should do where
   
   - `spotify_playlist_link` is a link to Spotify's playlist. You can get it from the 3-dot menu. 

   ![image](images/spotify-playlist.png)

   If the Spotify playlist link is skipped then it will download songs from your "My Music" collection 
   - `download_directory` is the location where the songs must be downloaded to. If you give a `.` then it will download to the current directory.
   
   Alternatively, `spotify_dl -p playlist_id -u user_name -o download_directory` will also work
   
   - `playlist_id` is the id of the playlist where songs need to be downloaded. If this is skipped then it will download songs ftom your "My Music" collection
   - `user_name` is the user name who created the playlist. 
   - `download_directory` is the location where the songs must be downloaded to. 
5. A first time run will require authentication; you will need to click on the URL prompted to authenticate. Once logged in, paste the URL back in.
6. To retrieve download songs as MP3, you will need to install ffmpeg. If you prefer to skip MP3 conversion, pass `-m` or `--skip_mp3` as a parameter when running the script
  - Linux users can get them by installing libav-tools by using apt-get (`sudo apt-get install -y libav-tools`) or a package manager which comes with your distro
  - Windows users can download FFMPEG pre-built binaries from [here](http://ffmpeg.zeranoe.com/builds/). Extract the file using [7-zip](http://7-zip.org/) to a foldrer and [add the folder to your PATH environment variable](http://www.wikihow.com/Install-FFmpeg-on-Windows) 
  
### How do I set defaults?

You can set defaults per user by creating a file at `~/.spotify_dl_settings`. Create a key with value for every argument you want a default for. Example:
``` json
{
      "output" : "/home/foo/spotify-dl-output"
      , "verbose" : "true"
      , "skip_mp3" : "t"
}
```

### Credits

 - [rhnvrm](https://github.com/rhnvrm) for [adding in youtube-dl](https://github.com/SathyaBhat/spotify-dl/pull/1)
 - [mr-karan](https://github.com/mr-karan) for [adding save to directory](https://github.com/SathyaBhat/spotify-dl/pull/6)
 - [shantanugoel](https://github.com/shantanugoel) for adding in [User playlist](https://github.com/SathyaBhat/spotify-dl/pull/7), [skip MP3 conversion](https://github.com/SathyaBhat/spotify-dl/pull/34) and [Ability to use custom format string support](https://github.com/SathyaBhat/spotify-dl/pull/34)
 - [sildur](https://github.com/sildur) for adding any [user playlist support and other fixes](https://github.com/SathyaBhat/spotify-dl/pulls?q=is%3Apr+author%3Asildur+is%3Aclosed)
 - [avinassh](https://github.com/avinassh) for being a [Rockstar](https://github.com/avinassh/rockstar) and not teleporting over to my house to kill me when I innundated him with questions
 - [doulwyi](https://github.com/doulwyi) for adding id3 tagging and ability to parse Spotify URI
 - [Gowtham](https://github.com/HackToHell) for [create playlist in download](https://github.com/SathyaBhat/spotify-dl/pull/23) directory
 - [alvierahman90](https://github.com/alvierahman90) for [config file support](https://github.com/SathyaBhat/spotify-dl/pull/42) and [Spotify playlist URL support](https://github.com/SathyaBhat/spotify-dl/pull/41)
 - [Bibhas](https://github.com/iambibhas) for fixing [can only concatenate list (not "str") to list error](https://github.com/SathyaBhat/spotify-dl/issues/44)
 - [Nikhil Nagaraju](https://github.com/nikhilnagaraju) for fixing support for playlist url with or without userid #58

## Issues, Feedback, Contact details
Feel free to raise any bugs/issues under Github issues. Pull requests are also more than welcome. You can reach me on twitter at [@sathyabhat](https://twitter.com/sathyabhat) or drop an email [sathya@sathyasays.com](mailto:sathya@sathyasays.com)
