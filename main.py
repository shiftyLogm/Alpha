import tkinter
import tkinter.messagebox
from tkinter import *
from tkinter import filedialog
from downloader import DownloadVideo
import os

class MyApp:
    def __init__(self):
        self.inputPathVar = None
        self.inputText = None
        self.inputPath = None
        self.input_urlobj = None
        self.download_btnobj = None
        self.mainWindow = Tk()
        self.mainWindow.title("Alpha")
        self.mainWindow.geometry("1000x500")
        self.mainWindow.resizable(False, False)
        self.mainWindow.configure(bg="#d9eff1")
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
        titleLabel = Label(master=self.mainWindow, text="Bem-vindo ao Alpha!", bg="#d9eff1",
                           font=("Consolas", 30, "bold"))
        titleLabel.pack(pady=(20, 0))

    def labelUrl(self):
        label = Label(master=self.mainWindow, text="Coloque a URL no campo abaixo", bg="#d9eff1", font=("Consolas", 20),
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
        label = Label(master=self.mainWindow, text="Localizar pasta de destino", bg="#d9eff1", font=("Consolas", 20),
                      anchor='w')
        label.pack(padx=(20, 0), pady=(20, 0), anchor="w")

    def pathBtn(self):
        pathBtn = Button(master=self.mainWindow, command=self.getpath, text="Abrir", bd=1, width=12)
        pathBtn.pack(padx=(20, 0), pady=(10, 0), anchor="w")

    def getpath(self):
        pathway = filedialog.askdirectory()  # Abrir file explorer para colocar a pasta
        if pathway:
            self.inputPath.config(state='normal')
            self.inputPath.delete(0, END)
            self.inputPath.insert(0, pathway)
            self.inputPath.config(state='readonly')

    def searchBtn(self):
        self.search_btnobj = Button(master=self.mainWindow, command=self.Search_Video,
                                      text="Pesquisar", bd=1, width=12, state='disabled')
        self.search_btnobj.pack(padx=(20, 0), pady=(10, 0), anchor='w')
        # self.search_btnobj.grid(column=0, row=0)

    def downloadBtn(self):
        self.download_btnobj = Button(master=self.mainWindow, command=self.Download_Video,
                                      text="Download", bd=1, width=12, state='disabled')
        self.download_btnobj.pack(padx=(20, 0), pady=(10, 0), anchor='w')
        # self.download_btnobj.grid(column=1, row=0)

    def labelTitleUrl(self):
        self.titleUrl = Label(master=self.mainWindow, bg="#d9eff1", font=("Consolas", 15, 'bold'),
                              anchor='w')
        self.titleUrl.pack(padx=(20, 0), pady=(20, 0), anchor="w")

    def formatOption(self):
        self.selectedFormat = StringVar(value='mp4')
        self.mp4button = Radiobutton(self.mainWindow, text='MP4', value='mp4', variable=self.selectedFormat, bg="#d9eff1", )
        self.mp4button.pack_forget()
        self.mp3button = Radiobutton(self.mainWindow, text='MP3', value='mp3', variable=self.selectedFormat, bg="#d9eff1")
        self.mp4button.pack_forget()
        
    def Search_Video(self):
        self.link = self.inputText.get()
        self.path = self.inputPathVar.get()
        self.option = self.selectedFormat.get()
        try:
            self.video = DownloadVideo(link=self.link, path=self.path, format=self.option)
            self.titleUrl.config(text=self.video.Title())
            self.download_btnobj.config(state='normal')
            self.mp4button.pack(padx=(20, 0), anchor='w')
            self.mp3button.pack(padx=(20, 0), anchor='w')
        except Exception:
            tkinter.messagebox.showerror(title='Erro', message='URL inválido')

    def Download_Video(self):
        self.video.format = self.selectedFormat.get()
        self.video.Download()
        print(self.video.format)

app = MyApp()
app.mainWindow.mainloop()
