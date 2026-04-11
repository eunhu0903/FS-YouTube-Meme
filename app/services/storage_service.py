import os
import json
from datetime import datetime, timedelta


def safe(obj):
    if isinstance(obj, (datetime,)):
        return obj.isoformat()
    return obj

def get_kst_now():
    return datetime.utcnow() + timedelta(hours=9)


def save_videos(videos):
    date_str = get_kst_now().strftime("%Y-%m-%d")
    filename = f"data/videos_{date_str}.json"

    os.makedirs("data", exist_ok=True)

    data = {
        "date": date_str,
        "count": len(videos),
        "videos": videos
    }

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2, default=safe)

    print(f"💾 저장 완료: {filename} | 개수: {len(videos)}")
    return filename