# spotify-dl
Downloads songs from your Spotify My Music collection(well, almost...)


#Tell me more!
I wanted an easy way to grab the songs present in my library so I can download it & use it offline(Spotify still hasn't launched here. Y U NO COME?). [spotify_to_mp3](https://github.com/frosas/spotify-to-mp3) worked well but it relied on grooveshark, which unfortunately is no more.

So I wrote this script which mimics that library, but instead of downloading from grooveshark, it provides you with a file of youtube URLs which you can then plug into [youtube-dl](https://rg3.github.io/youtube-dl/)

###How do I get this thing running?

Pre-requisite: You need Python 3+

1. Clone [this repo](https://github.com/SathyaBhat/spotify-dl.git)
2. Install dependencies using `pip install -r requirements.txt`
 -  *Optional* (Using Virtualenv) 
     - `pip install virtualenv`
     - `cd my_project_folder` 
     - `virtualenv venv`
     - `source venv/bin/activate`
3. Enter your spotify userid in tokens.py
4. Create your Spotify app & fetch the keys from [Spotify Developer Console](https://developer.spotify.com/my-applications/#!/applications). Paste the client id, secret, redirect URL in tokens.py. Note the redirect URL can be a valid URL, just ensure it matches with what you have entered in the developer console & in the script.
5. Create your YouTube api & fetch the keys from [Google Developer Console](https://console.developers.google.com/apis/api/youtube/overview). Paste the keys in tokens.py.
6. Run the script using `python spotify-dl.py`. 
   - Note by default, this doesn't download the songs. To download, pass `-d` as well. Ex: `python spotify-dl.py -d`
   - To download to a specific directory, pass the directory along with `-o`. Ex: `python spotify-dl.py -d -o c:\music`
   - To make the script act on a specific playlist of yours instead of saved tracks, use '-p' option along with playlist id. Ex: `python spotify-dl.py -p 18NLt215Rh58uE30QNLOiX`
7. Click on the URL prompted to authenticate. Once logged in, paste the URL back in
8. To retrieve download songs as MP3, you will need to install ffmpeg. 
  - Linux users can get them by installing libav-tools by using apt-get (`sudo apt-get install -y libav-tools`) or a package manager which comes with your distro
  - Windows users can download FFMPEG pre-built binaries from [here](http://ffmpeg.zeranoe.com/builds/). Extract the file using [7-zip](http://7-zip.org/) to a foldrer and [add the folder to your PATH environment variable](http://www.wikihow.com/Install-FFmpeg-on-Windows) 

###Credits
 - [rhnvrm](https://github.com/rhnvrm) for [adding in youtube-dl](https://github.com/SathyaBhat/spotify-dl/pull/1)
 - [mr-karan](https://github.com/mr-karan) for [adding save to directory](https://github.com/SathyaBhat/spotify-dl/pull/6)

##Issues, Feedback, Contact details
Feel free to raise any bugs/issues under Github issues. Pull requests are also more than welcome. You can reach me on twitter at [@sathyabhat](https://twitter.com/sathyabhat) or drop a mail sathya at sathyasays dot com
