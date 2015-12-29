from spotify import *
import argparse

x = ['https://www.youtube.com/watch?v=5n4hlzrjWv4','https://www.youtube.com/watch?v=2YD7t4EOVfs']


parser = argparse.ArgumentParser(prog='spotify-dl')
parser.add_argument('-d', '--download', action='store_true', help='Download using youtube-dl')
args = parser.parse_args()

if(args.download == True): 
    	download_songs(x)