import os
from pathlib import Path

__all__ = ["VERSION"]

VERSION = "8.4.0"

if os.getenv("XDG_CACHE_HOME") is not None:
    SAVE_PATH = os.getenv("XDG_CACHE_HOME") + "/spotifydl"
else:
    SAVE_PATH = str(Path.home()) + "/.cache/spotifydl"

DOWNLOAD_LIST = "download_list.log"
