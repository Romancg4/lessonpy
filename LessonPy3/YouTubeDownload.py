import pytube
from pytube import Playlist, YouTube, Stream
import re
from pathlib import Path


PLAYLIST_URL = 'https://www.youtube.com/watch?v=nYTC4pYN59Y&list=PLpjaNRKtZxPNjKD6jCktOq3EbNjv0K-8k'
SAVE_PATH = Path('~/yt').expanduser()


skip_chars = r"""!"#$%&'()*+,./:;<=>?@[\]^`{|}~"""
playlist = Playlist(PLAYLIST_URL)
total = len(playlist.video_urls)
print('Number of videos in playlist: %s' % total)
for i, v in enumerate(playlist.videos_generator()):
    filename = re.sub(r"[%s]" % skip_chars, "", v.title.replace('|', '-')) + '.mp4'
    print(f'Download {i}/{total}: "{filename}"...')
    try:
        v.streams.get_highest_resolution().download(output_path=SAVE_PATH,
                                                    filename=filename,
                                                    skip_existing=True)
    except Exception as e:
        print(f'>>> ERROR: {e}')