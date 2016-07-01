# spotify_dl
Downloads songs from your Spotify My Music collection or any Spotify playlist


#Tell me more!
I wanted an easy way to grab the songs present in my library so I can download it & use it offline(Spotify still hasn't launched here. Y U NO COME?). [spotify_to_mp3](https://github.com/frosas/spotify-to-mp3) worked well but it relied on grooveshark, which unfortunately is no more.

So I wrote this script which mimics that library, but instead of downloading from grooveshark, it provides you with a file of youtube URLs which you can then plug into [youtube-dl](https://rg3.github.io/youtube-dl/)

###How do I get this thing running?

Pre-requisite: You need Python 3+

1. Install using pip 
      `pip install spotify_dl`
2. Create your Spotify app & fetch the client id and client secret from [Spotify Developer Console](https://developer.spotify.com/my-applications/#!/applications). These keys then need to be assigned as `SPOTIPY_CLIENT_ID`, `SPOTIPY_CLIENT_SECRET` and `SPOTIPY_REDIRECT_URI` environment variables. 

    You can set environment variables in Linux like so:

            export SPOTIPY_CLIENT_ID='your-spotify-client-id'
            export SPOTIPY_CLIENT_SECRET='your-spotify-client-secret'
            export SPOTIPY_REDIRECT_URI='your-app-redirect-url'

    Windows users, check for [this question](http://superuser.com/a/284351/4377) for details on how you can set environment variables.

    Note the redirect URL can be a valid URL, just ensure it matches with what you have entered in the developer console & in the environment variable above.

3. Create you YouTube API key & fetch the keys from [Google Developer Console](https://console.developers.google.com/apis/api/youtube/overview). Set the key as `YOUTUBE_DEV_KEY` environment variable as mentioned above.
4. Run the script using `spotify_dl`. spotify_dl accepts different parameters, for more details run `spotify_dl -h`. 
   For most users `spotify_dl -d -p playlist_id -u user_name -o download_directory` should do where
   
   - `playlist_id` is the id of the playlist where songs need to be downloaded. If this is skipped then it will download songs ftom your "My Music" collection
   - `user_name` is the user name who created the playlist. 
   - `download_directory` is the location where the songs must be downloaded to. 
5. A first time run will require authentication; you will need to click on the URL prompted to authenticate. Once logged in, paste the URL back in
6. To retrieve download songs as MP3, you will need to install ffmpeg. 
  - Linux users can get them by installing libav-tools by using apt-get (`sudo apt-get install -y libav-tools`) or a package manager which comes with your distro
  - Windows users can download FFMPEG pre-built binaries from [here](http://ffmpeg.zeranoe.com/builds/). Extract the file using [7-zip](http://7-zip.org/) to a foldrer and [add the folder to your PATH environment variable](http://www.wikihow.com/Install-FFmpeg-on-Windows) 

###Credits
 - [rhnvrm](https://github.com/rhnvrm) for [adding in youtube-dl](https://github.com/SathyaBhat/spotify-dl/pull/1)
 - [mr-karan](https://github.com/mr-karan) for [adding save to directory](https://github.com/SathyaBhat/spotify-dl/pull/6)
 - [shantanugoel](https://github.com/SathyaBhat/spotify-dl/issues?q=is%3Apr+is%3Aopen+author%3Ashantanugoel) for adding in [User playlist support](https://github.com/SathyaBhat/spotify-dl/pull/7)
 - [sildur](https://github.com/sildur) for adding any [user playlist support and other fixes](https://github.com/SathyaBhat/spotify-dl/pulls?q=is%3Apr+author%3Asildur+is%3Aclosed)
 - [avinassh](https://github.com/avinassh) for being a [Rockstar](https://github.com/avinassh/rockstar) and not teleporting over to my house to kill me when I innundated him with questions

##Issues, Feedback, Contact details
Feel free to raise any bugs/issues under Github issues. Pull requests are also more than welcome. You can reach me on twitter at [@sathyabhat](https://twitter.com/sathyabhat) or drop a mail sathya at sathyasays dot com
