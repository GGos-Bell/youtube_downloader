from downloader import Downloader
from editor import Editor
import os

class Selector(object):
    def __init__(self, yt_link) -> None:
        self.yt_link = yt_link

    def get_only_audio(self, save_path, file_name) -> None:
        video_ob = Downloader.get_video_ob(self.yt_link)
        Downloader.download_audio(video_ob, save_path, file_name)

    def get_only_video(self, save_path, file_name) -> None:
        video_ob = Downloader.get_video_ob(self.yt_link)
        Downloader.download_video(video_ob, save_path, file_name)

    def get_complete_video(self, save_path, file_name):
        video_ob = Downloader.get_video_ob(self.yt_link)
        itag = Downloader.get_stream_video_itag(video_ob)
        Downloader.download_video(video_ob, save_path, "videof.webm", itag[0])
        Downloader.download_audio(video_ob, save_path, "audiof.webm")
        save_paths = [save_path+"videof.webm", save_path+"audiof.webm"]
        Editor.merge_video(save_paths, save_path, file_name)
        os.remove(save_path+"videof.webm")
        os.remove(save_path+"audiof.webm")
   
    def get_thumb_img(self, save_path, file_name) -> None:
        thumb_url = Downloader.get_thumb_url(self.yt_link)
        Downloader.download_image(thumb_url, save_path, file_name)

def main() -> None:
    print("Running selector.py directly")

if __name__ == "__main__":
    main()