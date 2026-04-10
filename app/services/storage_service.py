import json
from datetime import datetime


def safe(obj):
    if isinstance(obj, (datetime,)):
        return obj.isoformat()
    return obj


def save_videos(videos):
    date_str = datetime.now().strftime("%Y-%m-%d")
    filename = f"videos_{date_str}.json"

    data = {
        "date": date_str,
        "count": len(videos),
        "videos": videos
    }

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2, default=safe)

    print(f"💾 저장 완료: {filename} | 개수: {len(videos)}")
    return filename