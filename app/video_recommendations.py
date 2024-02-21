import random

from utils.videos import resume_videos


def generate_video_recommendations():
    recommended_videos = []

    # Get 3 random video recommendations
    random_recommendations = random.sample(resume_videos, 3)

    for video_link in random_recommendations:
        recommended_videos.append(video_link)
    return recommended_videos
