#!/bin/sh

# Information: The docker image has to be previously built and tagged with spotify_dl[:latest]
# Use 'docker build -t spotify_dl .' inside the project directory to build the Docker container

# Specify download location, use pwd for current directory
location="`pwd`"

# Declare list with playlists to download
declare -a playlists=( \
	"https://open.spotify.com/PLAYLIST_LINK" "Playlist Name" \
	"https://open.spotify.com/PLAYLIST_LINK" "Playlist Name" \
)

# Set client ID and secret
client_id=sampleid123
client_secret=samplesecret123

arraylength=${#playlists[@]}

for (( i=1; i<${arraylength}+1; i=i+2 ));
do
	echo "Downloading playlist: ${playlists[$i-1]}"
	path="$location/${playlists[$i]}"
	echo "Creating dir: $path"
	mkdir -p "$path"
	echo "Starting container: " $(echo "spotify_dl-${playlists[$i]//[^[:alnum:]]/}" | sed 's/ä/ae/;s/ö/oe/;s/ü/ue/;s/ß/ss/g')
	docker run -d --rm --name $(echo "spotify_dl-${playlists[$i]//[^[:alnum:]]/}" | sed 's/ä/ae/;s/ö/oe/;s/ü/ue/;s/ß/ss/g') \
		   -e SPOTIPY_CLIENT_ID=$client_id \
		   -e SPOTIPY_CLIENT_SECRET=$client_secret \
		   -v "$location":/download \
		   spotify_dl \
		   spotify_dl -l "${playlists[$i-1]}" -o /download &
done
