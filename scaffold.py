import logging

logging.basicConfig(level=logging.INFO,
                    format='%(levelname)s: %(asctime)s - %(funcName)s - %(message)s')

log = logging.getLogger('sdl')