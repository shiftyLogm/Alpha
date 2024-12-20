import tkinter.messagebox
from tkinter import *
from tkinter import filedialog
import tkinter.ttk
from scripts.downloader import DownloadVideo
from scripts.WINDOW_icon import window_icon
import os

class Alpha:
    def __init__(self):
        self.inputPathVar = None
        self.inputText = None
        self.inputPath = None
        self.input_urlobj = None
        self.download_btnobj = None
        self.selectedResolution = None
        self.radioBtnRes = []
        self.radioBtnAbrs = []
        self.mainWindow = Tk()

        # Window configs
        self.mainWindow.title("Alpha")
        self.mainWindow.geometry("1000x600")
        self.mainWindow.resizable(False, False)
        self.mainWindow.configure(bg="#d9eff1")
        window_icon()
        self.mainWindow.iconbitmap("icon/mainlogo.ico")

        # Call methods
        self.titleLabel()
        self.labelUrl()
        self.inputUrl()
        self.searchBtn()
        self.downloadBtn()
        self.labelPath()
        self.path()
        self.pathBtn()
        self.labelTitleUrl()
        self.formatOption()

    def titleLabel(self):
        titleLabel = Label(master=self.mainWindow, text="Welcome to Alpha!", bg="#d9eff1",
                           font=("Consolas", 30, "bold"))
        titleLabel.pack(pady=(20, 0))

    def labelUrl(self):
        label = Label(master=self.mainWindow, text="Please enter the URL in the field below", bg="#d9eff1", font=("Consolas", 20),
                      anchor='w')
        label.pack(padx=(20, 0), pady=(20, 0), anchor="w")                                                  

    def inputUrl(self):
        self.inputText = StringVar()
        self.inputText.trace_add('write', self.disableInput)
        self.input_urlobj = Entry(master=self.mainWindow, font=("Arial", 15), justify=LEFT, bd=1, width=50,
                                  textvariable=self.inputText)
        self.input_urlobj.pack(padx=(20, 0), pady=(10, 0), anchor="w")

    def disableInput(self, *args):
        if len(self.inputText.get()) > 0: return self.search_btnobj.config(state='normal')
        return self.search_btnobj.config(state='disabled')

    def path(self):
        self.inputPathVar = StringVar(value=os.path.join(os.path.expanduser('~'), 'Downloads'))
        self.inputPath = Entry(master=self.mainWindow, font=("Arial", 15), justify=LEFT, bd=1, width=50,
                               textvariable=self.inputPathVar, state='readonly')
        self.inputPath.pack(padx=(20, 0), pady=(10, 0), anchor="w")

    def labelPath(self):
        label = Label(master=self.mainWindow, text="Locate the destination folder", bg="#d9eff1", font=("Consolas", 20),
                      anchor='w')
        label.pack(padx=(20, 0), pady=(20, 0), anchor="w")

    def pathBtn(self):
        pathBtn = Button(master=self.mainWindow, command=self.getpath, text="Open", bd=1, width=12)
        pathBtn.pack(padx=(20, 0), pady=(10, 0), anchor="w")

    def getpath(self):
        pathway = filedialog.askdirectory()
        if pathway:
            self.inputPath.config(state='normal')
            self.inputPath.delete(0, END)
            self.inputPath.insert(0, pathway)
            self.inputPath.config(state='readonly')

    def searchBtn(self):
        self.search_btnobj = Button(master=self.mainWindow, command=self.Search_Video,
                                      text="Search", bd=1, width=12, state='disabled')
        self.search_btnobj.pack(padx=(20, 0), pady=(10, 0), anchor='w')

    def downloadBtn(self):
        self.download_btnobj = Button(master=self.mainWindow, command=self.Download_Video,
                                      text="Download", bd=1, width=12, state='disabled')
        self.download_btnobj.pack(padx=(20, 0), pady=(10, 0), anchor='w')

    def labelTitleUrl(self):
        self.titleUrl = Label(master=self.mainWindow, bg="#d9eff1", font=("Consolas", 15, 'bold'),
                              anchor='w')
        self.titleUrl.pack(padx=(20, 0), pady=(20, 0), anchor="w")

    def formatOption(self):
        self.selectedFormat = StringVar(value='mp4')
        self.mp4button = Radiobutton(self.mainWindow, text='MP4', value='mp4', variable=self.selectedFormat, bg="#d9eff1",)
        self.mp4button.pack_forget()
        self.mp3button = Radiobutton(self.mainWindow, text='MP3', value='mp3', variable=self.selectedFormat, bg="#d9eff1",)
        self.mp4button.pack_forget()

    def showDownloadTypesInfos(self, typevalue):
        
        if (typevalue == 'mp4'):

            y = 414
            for button in self.radioBtnRes:
                button.place(x=80, y=y)
                y += 20

            _ = [i.place(x=0, y=2000) for i in self.radioBtnAbrs]


        elif (typevalue == 'mp3'):
            
            y = 414
            for button in self.radioBtnAbrs:
                button.place(x=80, y=y)
                y += 20

            _ = [i.place(x=0, y=2000) for i in self.radioBtnRes]

        
    def Search_Video(self):
        self.link = self.inputText.get()
        self.path = self.inputPathVar.get()
        self.option = self.selectedFormat.get()

        try: 
            self.video = DownloadVideo(link=self.link, path=self.path, format=self.option, on_progress_bar=self.on_progress_pBar)
        except:
            tkinter.messagebox.showerror(title="Invalid URL", message="Your URL is invalid")
            return

        self.titleUrl.config(text=self.video.Title())

        self.download_btnobj.config(state='normal')

        self.mp4button.pack(padx=(20, 0), anchor='w')
        self.mp3button.pack(padx=(20, 0), anchor='w')

        resolutions = self.video.getResolutions_mp4()
        abrs = self.video.getAudios_abr()

        self.selectedResolution = StringVar(value=resolutions[0])

        self.create_pBar_Video()
        
        y = 414
        for res in sorted(set(resolutions), key=lambda x: int(x.split('x')[0][:-1]), reverse=True):
            radio = Radiobutton(self.mainWindow, text=res, value=res, variable=self.selectedResolution, bg="#d9eff1")
            radio.place(x=80, y=y)
            self.radioBtnRes.append(radio)
            y += 20
        
        for abr in sorted(set(abrs), key=lambda x: int(x.split('x')[0][:-4]), reverse=True):
            radio = Radiobutton(self.mainWindow, text=abr, value=abr, variable=self.selectedResolution, bg="#d9eff1")
            radio.place(x=0, y=2000)
            self.radioBtnAbrs.append(radio)

        self.mp4button.config(command=lambda: self.showDownloadTypesInfos(typevalue='mp4'))
        self.mp3button.config(command=lambda: self.showDownloadTypesInfos(typevalue='mp3'))

    def Download_Video(self):
        self.video.format = self.selectedFormat.get()
        self.video.setResolutionValue(self.selectedResolution.get())
        self.video.Download()

    def create_pBar_Video(self):

        # Progress bar of download
        self.progress_bar = tkinter.ttk.Progressbar(self.mainWindow, length=300, mode='determinate')
        self.progress_bar.pack()

        # Percentage of download
        self.percentage_label = Label(self.mainWindow, text="0%", bg="#d9eff1")
        self.percentage_label.pack()
    
    def on_progress_pBar(self, stream, chunk, bytes_remaining):
        total_size = stream.filesize
        bytes_downloaded = total_size - bytes_remaining
        percent = bytes_downloaded / total_size * 100

        self.progress_bar['value'] = percent
        self.percentage_label.config(text=f"{int(percent)}%")
        
        # Update interface
        self.mainWindow.update_idletasks()
