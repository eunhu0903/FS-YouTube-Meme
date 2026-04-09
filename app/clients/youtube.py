from googleapiclient.discovery import build
from core.config import api_key

youtube = build("youtube", "v3", developerKey=api_key)

def test_search():
    request = youtube.search().list(
        q="웃긴 영상",
        part="snippet",
        type="video",
        maxResults=5
    )

    response = request.execute()

    for item in response["items"]:
        print(item["snippet"]["title"])