
from lib.cartoons_to_video import cartoons_to_video
from lib.video_to_audio import video_to_audio
from lib.youtube_downloader import youtube_downloader
from lib.video_to_images import video_to_images
from lib.images_to_cartoons import images_to_cartoons

from services.insert_data_service import insert_data_service

import database.connection


def main():
    youtube_url = 'https://www.youtube.com/watch?v=uMeR2W19wT0'

    folder_name = youtube_downloader(youtube_url)
    insert_data_service(folder_name)
    video_to_audio(folder_name)
    video_to_images(folder_name)
    images_to_cartoons(folder_name)
    cartoons_to_video(folder_name)


main()
