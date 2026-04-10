def filter_videos(videos):
    KEYWORDS = ["웃김", "ㅋㅋ", "레전드", "챌린지", "공감", "웃긴"]
    MIN_VIEWS = 10000

    filtered = []

    for v in videos:
        title = v.get("title", "")
        views = v.get("view_count", 0)
        likes = v.get("like_count", 0)   

        if views < MIN_VIEWS:
            continue

        if not any(k in title for k in KEYWORDS):
            continue

        filtered.append(v)

    filtered.sort(key=lambda x: x.get("like_count", 0), reverse=True)

    return filtered