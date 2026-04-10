from services.fetch_service import fetch_videos
from services.stats_service import get_video_status
from utils.filter import filter_videos


def main():
    videos = fetch_videos()

    videos_ids = [v["video_id"] for v in videos]
    stats = get_video_status(videos_ids)

    for v in videos:
        v["views"] = stats.get(v["video_id"], 0)
    
    filtered = filter_videos(videos)

    print("\n🔥 이번달 유행 영상 TOP 리스트\n")

    for i, v in enumerate(filtered, 1):
        print(f"{i}. {v['title']}")
        print(f"   👀 조회수: {v['views']:,}")
        print(f"   🔗 링크: {v['url']}\n")

if __name__ == "__main__":
    main()