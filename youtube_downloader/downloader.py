from pytube import YouTube
import requests

class Downloader(object):

    def get_video_ob(yt_link):
        return YouTube(yt_link)

    def download_video(video_ob, save_path, file_name):
        video = video_ob.streams.get_by_itag(248) # 248 (webm) or 137 (mp4)
        video.download(save_path, file_name)

    def download_audio(video_ob, save_path, file_name):
        audio = video_ob.streams.get_by_itag(251) # 251 (webm) or 140 (mp4)
        audio.download(save_path, file_name) 

    def get_thumb_url(yt_link) -> str:
        video_ob = Downloader.get_video_ob(yt_link)
        return video_ob.thumbnail_url

    def download_image(path, save_path, file_name):
        with open(save_path + file_name, 'wb') as handle:
            response = requests.get(path, stream=True)

            if not response.ok:
                print(response)

            for block in response.iter_content(1024):
                if not block:
                    break

                handle.write(block)

def main() -> None:
    print("Running downloader.py directly")

if __name__ == "__main__":
    main()