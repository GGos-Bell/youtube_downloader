from selector import Selector
import argparse
import os
import random

desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
random_n = random.randint(100, 999)
file_name = "yt"+str(random_n)

parser = argparse.ArgumentParser(description="Download youtube videos.")
parser.add_argument('-l', '--link', metavar="", type=str, required=True, help="Youtube video URL")
parser.add_argument('-sv', '--save_path', metavar="", type=str, default=desktop, help="Folder path where you will save your file")
parser.add_argument('-fn', '--file_name', metavar="", type=str, default=file_name, help="File name")
options = parser.add_mutually_exclusive_group()
options.add_argument('-v', '--video', action='store_true', help="Download only the video without sound.")
options.add_argument('-s', '--sound', action='store_true', help="Download only the sound.")
options.add_argument('-t', '--thumb', action='store_true', help="Download the thumbnail.")
args = parser.parse_args()

# komeko "https://www.youtube.com/watch?v=ERPlZKPYWuw"
# kaguya "https://www.youtube.com/watch?v=CEygJomZvBc"
# trump "https://www.youtube.com/watch?v=4EbRtU4z-nU"

def main() -> None:
    if args.video:
        video = Selector(args.link)
        video.get_only_video(args.save_path+"\\", args.file_name+".webm")
    elif args.sound:
        audio = Selector(args.link)
        audio.get_only_audio(args.save_path+"\\", args.file_name+".webm")
    elif args.thumb:
        thumb = Selector(args.link)
        thumb.get_thumb_img(args.save_path+"\\", args.file_name+".png")
    else:
        video = Selector(args.link)
        video.get_complete_video(args.save_path+"\\", args.file_name+".webm")

if __name__ == "__main__":
    main()