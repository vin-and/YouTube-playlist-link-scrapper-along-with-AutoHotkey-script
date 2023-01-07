import logging

logging.basicConfig(filename="links.txt",
                level=logging.DEBUG,
                format='%(message)s',
                datefmt='%m/%d/%Y %I:%M:%S')

playlist = "link"

try:
    from pytube import Playlist

except:
    import os
    os.system("pip install pytube")

pl = Playlist(playlist)

for url in pl:
    logging.info(url)