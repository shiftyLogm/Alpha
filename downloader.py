from pytube import YouTube

class DownloadVideo:

    def __init__(self, link, path, format):
        self.link = link
        self.path = path
        self.format = format
        self.url = YouTube(self.link)

    def Title(self):
        return self.url.title

    def Download(self):
        video = self.url.streams.get_highest_resolution()

        if self.format == 'mp3':
            audio = self.url.streams.filter(only_audio=True).first()
            return audio.download(output_path=self.path)

        video.download(output_path=self.path)

