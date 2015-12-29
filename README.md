# spotify-dl
Downloads songs from your Spotify My Music collection(well, almost...)


#Tell me more!
I wanted an easy way to grab the songs present in my library so I can download it & use it offline(Spotify still hasn't launched here. Y U NO COME?). [spotify_to_mp3](https://github.com/frosas/spotify-to-mp3) worked well but it relied on grooveshark, which unfortunately is no more.

So I wrote this script which mimics that library, but instead of downloading from grooveshark, it provides you with a file of youtube URLs which you can then plug into [youtube-dl](https://rg3.github.io/youtube-dl/)

###How do I get this thing running?

Pre-requisite: You need Python 3+

1. Clone [this repo](https://github.com/SathyaBhat/spotify-dl.git)
2. Install dependencies using `pip install -r requirements.txt`
3. Enter your spotify userid in tokens.py
4. Create your Spotify app & fetch the keys from [Spotify Developer Console](https://developer.spotify.com/my-applications/#!/applications). Paste the client id, secret, redirect URL in tokens.py. Note the redirect URL can be a valid URL, just ensure it matches with what you have entered in the developer console & in the script.
5. Create your YouTube api & fetch the keys from [Google Developer Console](https://console.developers.google.com/apis/api/youtube/overview). Paste the keys in tokens.py.
6. Run the script using `python spotify-dl`
7. Click on the URL prompted to authenticate. Once logged in, paste the URL back in
8. Once done, songs.txt should have list of YouTube URLs. Pass them to youtube-dl to have them downloaded. Please check [youtube-dl](https://rg3.github.io/youtube-dl/) documentation for more details. You also need ffmpeg or avconv installed. (`sudo apt-get install -y libav-tools`)

##To Do

- Integrate youtube-dl in script
- Skip songs already downloaded

##Issues, Feedback, Contact details
Feel free to raise any bugs/issues under Github issues. Pull requests are also more than welcome. You can reach me on twitter at [@sathyabhat](https://twitter.com/sathyabhat)
