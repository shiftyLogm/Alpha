from pytubefix import YouTube
import os
from scripts.FFMPEG_fix import merge_ffmpeg 
from scripts.TITLE_fix import fix_title_video
from scripts.REWRITING_fixes import *

class DownloadVideo:

    def __init__(self, link, path, format, on_progress_bar):
        self.link = link
        self.path = path
        self.format = format
        self.url = YouTube(self.link, on_progress_callback=on_progress_bar)
        self.resolutionValue = None

    # Thumb Url return
    def getImageUrl(self) -> str:
        return self.url.thumbnail_url
    
    # Resolution setter
    def setResolutionValue(self, value: str) -> None:
        self.resolutionValue = value
    
    # Title return
    def Title(self) -> str:
        return self.url.title
    
    # MP4 res return
    def getResolutions_mp4(self) -> list:
        streams = self.url.streams.filter(mime_type='video/mp4', adaptive=True)
        
        resolutions = list()
        for res in streams:
            resolutions.append(res.resolution)

        return resolutions
    
    # abrs mp3 return
    def getAudios_abr(self) -> list:
        streams = self.url.streams.filter(mime_type="audio/mp4", adaptive=True)

        resolutions = list()
        for abr in streams:
            resolutions.append(abr.abr)

        return resolutions

    # Download video method
    def Download(self):
        video = self.url.streams.filter(res=self.resolutionValue).first()

        fixed_t = fix_title_video(t_v=self.url.title)

        if (verifyFile(f"{self.path}/{fixed_t}")):
            increaseTitle(self.path, fixed_t)

        if self.format == 'mp4':

            video_path = video.download(output_path=self.path, filename=f'{fixed_t}.mp4')

            audio = self.url.streams.filter(only_audio=True).first()
            
            audio_path = audio.download(output_path=self.path, filename=f'{fixed_t}.mp3')
        
        else: 
            return self.url.streams.filter(only_audio=True).first().download(output_path=self.path, filename=f'{fixed_t}.mp3')

        # Audio fix with FFMPEG        
        merge_ffmpeg(
            v_p=video_path,
            a_p=audio_path,
            path=self.path,
            final_t=f"{fixed_t.strip().replace(" ", "_")}"    
        )

        os.remove(video_path)
        os.remove(audio_path)
