import os
from datetime import datetime
from pytapo import Tapo

IP = "192.168.176.37"
USER = "smartiotlabs"
PASSWORD = "cam4Werni"
SAVE_DIR = "/data/tapo_videos"

os.makedirs(SAVE_DIR, exist_ok=True)

tapo = Tapo(IP, USER, PASSWORD)

filename = os.path.join(SAVE_DIR, f"clip_{datetime.now().strftime('%Y%m%d_%H%M%S')}.mp4")

print(f"Lade Video herunter nach {filename}")
with open(filename, "wb") as f:
    stream = tapo.getMediaStream()
    for chunk in stream.iter_content(chunk_size=8192):
        f.write(chunk)
