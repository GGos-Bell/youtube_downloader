from pytube import YouTube
import requests
import re

class Downloader(object):

    def get_video_ob(yt_link):
        return YouTube(yt_link)

    def get_stream_video_itag(video_ob):
        streams = [str(video_ob.streams[i]) for i in range(len(video_ob.streams)-1)]
        regex = '<Stream: itag="\d{2,3}" mime_type="video/webm" res="1080p" fps="\d{1,2}fps" vcodec="[a-zA-Z0-9_.]+" progressive="False" type="video">'
        for stream in streams:
            match = re.search(regex, stream)
            if match != None:
                right_stream = match
                continue
        stream_itag = re.findall('itag="(\d{1,3})"', str(right_stream))
        return stream_itag

    def download_video(video_ob, save_path, file_name, itag):
        video = video_ob.streams.get_by_itag(itag) # 248 (webm) or 137 (mp4)
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