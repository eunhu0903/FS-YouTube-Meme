from clients.youtube import youtube
from datetime import datetime, timedelta

def fetch_videos(query="웃긴 영상", max_results=10):
    thirty_days_ago = datetime.utcnow() - timedelta(days=30)

    published_after = thirty_days_ago.isoformat("T") + "Z"

    request = youtube.search().list(
        q=query,
        part="snippet",
        type="video",
        maxResults=max_results,
        order="viewCount",
        publishedAfter=published_after
    )

    response = request.execute()

    videos = []

    for item in response["items"]:
        video_id = item["id"]["videoId"]
        
        videos.append({
            "video_id": video_id,
            "title": item["snippet"]["title"],
            "publishedAt": item["snippet"]["publishedAt"],
            "url": f"https://www.youtube.com/watch?v={video_id}"
        })
    
    return videos