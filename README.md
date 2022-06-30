# Download YouTube Videos
![Python Versions](https://img.shields.io/pypi/pyversions/django?logo=python&logoColor=white&style=for-the-badge)

Using Pytube and automatic merging video and audio from the YouTube API.

Video and sound files will be saved as .webm files.  
Image files will be saved as .png files.

## How to run
**Download video with sound**  
`py main.py -l [video url]`

**Download video without sound**  
`py main.py -l [video url] -v`

**Download only sound**  
`py main.py -l [video url] -s`

**Download video thumbnail**  
`py main.py -l [video url] -t`

**Optional commands**  
`-sv [save_path]` -> To choose a folder to save the file (default: desktop)  
`-fn [file_name]` -> To choose a file name (default: yt+[random number])

### TODO

- [X] Download only video or audio.
- [X] Download video with sound.
- [X] Download the video thumbnail.
- [X] Add CLI scripts.