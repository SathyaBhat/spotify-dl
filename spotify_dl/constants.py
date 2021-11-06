import os

__all__ = ['VERSION']

VERSION = '7.6.0'

if os.getenv("XDG_CACHE_HOME") is not None:
    SAVE_PATH = os.getenv("XDG_CACHE_HOME") + "/spotifydl"
else:
    SAVE_PATH = os.getenv("HOME") + ".cache/spotifydl"
