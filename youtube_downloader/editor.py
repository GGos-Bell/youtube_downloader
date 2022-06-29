import moviepy.editor as mpe

class Editor(object):
    
    def merge_video(paths, save_path, file_name):
        video_clip = mpe.VideoFileClip(paths[0])
        audio_clip = mpe.AudioFileClip(paths[1])
        final_clip = video_clip.set_audio(audio_clip)
        final_clip.write_videofile(save_path+file_name)

def main() -> None:
    print("Running editor.py directly.")

if __name__ == "__main__":
    main()

