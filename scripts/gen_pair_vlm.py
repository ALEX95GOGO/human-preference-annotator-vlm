import os
import json

VIDEO_DIR = "videos/front_cam_video"
OUTPUT_FILE = "pairs.json"

pairs = []
pair_id = 1

for filename in sorted(os.listdir(os.path.join("../frontend", VIDEO_DIR))):
    if not filename.lower().endswith(".mp4"):
        continue

    entry = {
        "pair_id": f"{pair_id:06d}",
        "left_clip": f"{VIDEO_DIR}/{filename}",
        "right_clip": f"{VIDEO_DIR}/{filename}",
        "description": "clips"
    }

    pairs.append(entry)
    pair_id += 1

with open(OUTPUT_FILE, "w") as f:
    json.dump(pairs, f, indent=2)

print(f"Wrote {len(pairs)} entries to {OUTPUT_FILE}")

