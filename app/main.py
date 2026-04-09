from services.fetch_service import fetch_videos
from services.stats_service import get_video_status


def main():
    # 1. 영상 가져오기
    videos = fetch_videos()

    # 2. video_id 추출
    video_ids = [v["video_id"] for v in videos]

    # 3. 조회수 가져오기
    stats = get_video_status(video_ids)

    # 4. 합치기
    for v in videos:
        v["views"] = stats.get(v["video_id"], 0)

    # 5. 출력
    for v in videos:
        print(v)


if __name__ == "__main__":
    main()