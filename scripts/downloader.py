from pytubefix import YouTube
from pytubefix.cli import on_progress

class DownloadVideo:

    def __init__(self, link, path, format):
        self.link = link
        self.path = path
        self.format = format
        self.url = YouTube(self.link)

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
    def Download(self) -> None:
        video = self.url.streams.get_by_resolution(self.resolution)

        if self.format == 'mp3':
            audio = self.url.streams.filter(only_audio=True).first()
            return audio.download(output_path=self.path)

        video.download(output_path=self.path)
