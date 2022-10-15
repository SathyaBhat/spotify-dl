## spotify_dl

Downloads songs from any Spotify playlist, album or track.

[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)
[![PyPI download month](https://img.shields.io/pypi/dm/spotify_dl.svg)](https://pypi.python.org/pypi/spotify_dl/)
[![PyPI license](https://img.shields.io/pypi/l/spotify_dl.svg)](https://pypi.python.org/pypi/spotify_dl/)
[![PyPI pyversions](https://img.shields.io/pypi/pyversions/spotify_dl.svg)](https://pypi.python.org/pypi/spotify_dl/)
[![GitHub release](https://img.shields.io/github/release/SathyaBhat/spotify-dl.svg)](https://GitHub.com/SathyaBhat/spotify-dl/releases/)
[![GitHub stars](https://img.shields.io/github/stars/SathyaBhat/spotify-dl.svg?style=social&label=Star&maxAge=2592000)](https://GitHub.com/SathyaBhat/spotify-dl/stargazers/)
[![GitHub contributors](https://img.shields.io/github/contributors/SathyaBhat/spotify-dl.svg)](https://GitHub.com/SathyaBhat/spotify-dl/graphs/contributors/)

[![Awesome Badges](https://img.shields.io/badge/badges-awesome-green.svg)](https://github.com/Naereen/badges)

### Tell me more!

I wanted an easy way to grab the songs present in my library so I can download it & use it offline. I no longer use this, but continue to maintain this. spotify-dl doesn't download anything from Spotify. It picks up the metadata from Spotify API and then uses [yt-dlp](https://github.com/yt-dlp/yt-dlp) to download the song.

### How do I get this thing running?

Install using pip

    pip3 install spotify_dl

Run the program

    spotify_dl -l spotify_playlist_link_1 spotify_playlist_link_2

If you want to make use of parallel download, pass `-mc <number>`, where `<number>` refers to number of cores. If this is too high, spotify-dl will set it to one lesser than max number of cores that you have.

    spotify_dl -mc 4 -l spotify_playlist_link_1 spotify_playlist_link_2

For running in verbose mode, append `-V`

    spotify_dl -V -l spotify_playlist_link -o download_directory

For more details and other arguments, issue `-h`

    spotify_dl -h

See [the getting started guide](https://github.com/SathyaBhat/spotify-dl/blob/master/GETTING_STARTED.md) for more details.

### Demo

[![asciicast](https://asciinema.org/a/488558.svg)](https://asciinema.org/a/488558)

### Contributing and Local development

Pull requests and any contributions are always welcome. Please open an issue with your proposal before you start with something.

#### Running tests

At the moment, there are barely any tests but PRs always welcome to improve this. Tests are setup and run with pytest, run

    make tests

to run the tests with [Make](https://www.gnu.org/software/make/)

### Thanks and Credits

Take a look at [CONTRIBUTORS](https://github.com/SathyaBhat/spotify-dl/graphs/contributors) for a list of all people who have helped and contributed to the project.

### Issues, Feedback, Contact details

Feel free to raise any bugs/issues under Github issues. Pull requests are also more than welcome.
