"""Download youtube."""
import os
import os.path as osp
import youtube_dl # Youtube_dl is used for download the video
from pydub import AudioSegment

FOLDER_OUT = "/home/ok97465/비디오"
VIDEO_EXTS = ('mp4', 'flv', 'webm', '3gp', 'm4a', 'mp3', 'ogg', 'aac', 'wav')

# Here we give some advanced settings. outtmpl is used to define the path of
# the video that we are going to download
ydl_opt = {"outtmpl" : FOLDER_OUT + "/%(title)s.%(ext)s",
           "format": "bestaudio/best",
           "writeautomaticsub": True}


def download_youtube_link(link):
    """Start the download operation."""
    try:
    # The method YoutubeDL() take one argument which is a dictionary for
    # changing default settings
        file_list_prev = set(os.listdir(FOLDER_OUT))
        with youtube_dl.YoutubeDL(ydl_opt) as yd: 
            yd.download([link])  # Start the download

            # 다운로드된 파일명을 알기 위해서 이전 폴더 파일 List와 비교한다.
            file_list = set(os.listdir(FOLDER_OUT))
            file_list_new = list(file_list - file_list_prev)
            file_list_new = [name for name in file_list_new 
                             if name.endswith(VIDEO_EXTS)]
            
            # MP3 파일명 생성
            path_video = osp.join(FOLDER_OUT, file_list_new[0])
            name, ext = osp.splitext(path_video)
            path_audio = name + '.mp3'
            ext = ext.replace('.', '')

            # 동영상에서 MP# 추출
            audio = AudioSegment.from_file(path_video, ext)
            audio.export(path_audio, format='mp3')
    except Exception as e:
        print(e)


if __name__ == "__main__":
    download_youtube_link("https://www.youtube.com/watch?v=wiHBmFUH7JY")

