from clients.youtube import youtube

def get_video_status(video_ids):
    request = youtube.videos().list(
        part="statistics",
        id=",".join(video_ids)
    )

    response = request.execute()

    stats = {}

    for item in response["items"]:
        stats[item["id"]] = {
            "views": int(item["statistics"].get("viewCount", 0)),
            "likes": int(item["statistics"].get("likeCount", 0))
        }
    
    return stats