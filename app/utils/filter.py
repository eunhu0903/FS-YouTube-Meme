def filter_videos(videos):
    KEYWORDS = ["웃김", "ㅋㅋ", "레전드", "챌린지", "공감", "웃긴"]
    MIN_VIEWS = 10000

    filtered = []

    for v in videos:
        title = v.get("title", "")
        views = v.get("views", 0)

        if views < MIN_VIEWS:
            continue
        
        if not any(k in title for k in KEYWORDS):
            continue

        filtered.append(v)

    # 🔥 좋아요 기준 정렬 (핵심 변경)
    filtered.sort(key=lambda x: x["likes"], reverse=True)

    return filtered