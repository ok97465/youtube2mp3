"""Download youtube."""
import os
import os.path as osp
import youtube_dl # Youtube_dl is used for download the video
import argparse

FOLDER_OUT = "/home/ok97465/비디오"
VIDEO_EXTS = ('mp4', 'flv', 'webm', '3gp', 'm4a', 'mp3', 'ogg', 'aac', 'wav')

# Here we give some advanced settings. outtmpl is used to define the path of
# the video that we are going to download


def download_youtube_link(link, ydl_opt):
    """Start the download operation."""
    try:
        with youtube_dl.YoutubeDL(ydl_opt) as yd: 
            yd.download([link])  # Start the download
    except Exception as e:
        print(e)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Download Youtube using youtubedl.")
    parser.add_argument('url', type=str, help='URL of youtube')
    parser.add_argument('--video', action='store_true', help='store video of youtube')
    args = parser.parse_args()

    ydl_opt = {"outtmpl" : FOLDER_OUT + "/%(title)s.%(ext)s",
               "format": "bestaudio/best",
               "writeautomaticsub": True}

    if args.video is True:
        ydl_opt["format"] = "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best"

    download_youtube_link(args.url, ydl_opt)

