from services.fetch_service import fetch_videos
from services.stats_service import get_video_status
from services.storage_service import save_videos
from utils.filter import filter_videos


def main():
    videos = fetch_videos()

    video_ids = [v["video_id"] for v in videos]

    stats = get_video_status(video_ids)

    for v in videos:
        if v["video_id"] in stats:
            v.update({
                "view_count": stats[v["video_id"]]["views"],
                "like_count": stats[v["video_id"]]["likes"]
            })

    filtered_videos = filter_videos(videos)

    filename = save_videos(filtered_videos)

    print(f"🚀 완료! 저장 파일: {filename}")


if __name__ == "__main__":
    main()