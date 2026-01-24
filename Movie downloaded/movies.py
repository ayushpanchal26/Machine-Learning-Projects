import m3u8
import requests
from urllib.parse import urljoin

m3u8_url = "https://s14.freecdn2.top/files/0IMQLIS5J8EC6OLJBZAIAWY0XF/720p/720p.m3u8?in=..."

playlist = m3u8.load(m3u8_url)

with open("video.ts", "ab") as f:
    for segment in playlist.segments:
        segment_url = urljoin(m3u8_url, segment.uri)
        r = requests.get(segment_url, stream=True)
        f.write(r.content)

print("Download finished as video.ts")

