from pytubefix import YouTube
import os
from FFMPEG_fix import merge_ffmpeg 

class DownloadVideo:

    def __init__(self, link, path, format):
        self.link = link
        self.path = path
        self.format = format
        self.url = YouTube(self.link)
        self.resolutionValue = None

    # Setter da resolução
    def setResolutionValue(self, value: str) -> None:
        self.resolutionValue = value
    
    # Retorno do título
    def Title(self) -> str:
        return self.url.title
    
    # Retorno das resoluções MP4
    def getResolutions_mp4(self) -> list:
        streams = self.url.streams.filter(mime_type='video/mp4', adaptive=True)
        
        resolutions = list()
        for res in streams:
            resolutions.append(res.resolution)

        return resolutions
    
    # Retorno dos abrs MP3
    def getAudios_abr(self) -> list:
        streams = self.url.streams.filter(mime_type="audio/mp4", adaptive=True)

        resolutions = list()
        for abr in streams:
            resolutions.append(abr.abr)

        return resolutions

    # Método para download do video
    def Download(self):
        video = self.url.streams.filter(res=self.resolutionValue).first()

        video_path = video.download(output_path=self.path, filename=f'{self.url.title}.mp4')

        audio = self.url.streams.filter(only_audio=True).first()
        
        audio_path = audio.download(output_path=self.path, filename=f'{self.url.title}.mp3')

        # Audio fix with FFMPEG        
        merge_ffmpeg(
            v_p=video_path,
            a_p=audio_path,
            path=self.path,
            final_t="output"    
        )

        os.remove(f'{self.path}/{self.url.title}.mp3')
