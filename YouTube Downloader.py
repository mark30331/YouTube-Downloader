from pytube import YouTube
from playsound import playsound
import tkinter as tk

window_width = 500
window_height = 150
window_title = "YouTube Downloader"
button_click = "clicks.m4a"

class YouTubeDownloader:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("{}x{}".format(window_width, window_height))
        self.window.configure(bg="#a8323a")
        self.window.title(window_title)
        
        #creation of lables
        self.link_lable = tk.Label(self.window, text = "Download Link")
        self.link_lable.grid(column= 0, row=0)
        self.name_lable = tk.Label(self.window, text= "Save File As")
        self.name_lable.grid(column = 0, row= 1)
        self.path_lable = tk.Label(self.window, text = "Save File Path")
        self.path_lable.grid(column = 0, row = 2)
        self.extension_lable = tk.Label(self.window, text = "File Extension")
        self.extension_lable.grid(column = 0, row = 3)


        #creation of entry
        self.link_entry = tk.Entry(master=self.window, width = 50)
        self.link_entry.grid(column = 1 , row = 0)
        self.name_entry = tk.Entry(master=self.window, width = 50)
        self.name_entry.grid(column =1, row= 1)
        self.path_entry = tk.Entry(master= self.window, width = 50)
        self.path_entry.grid(column = 1, row=2)
        self.extension_entry = tk.Entry(master=self.window, width = 50)
        self.extension_entry.grid(column = 1, row=3)


        #creation of button
        self.download_button = tk.Button(self.window, text = "Download", command = self.__getLink)
        self.download_button.grid(column= 1, row = 4)

        return

    def __downloader(self, link, save_path = "", save_name = "", extension ="1080p"):
        yt = YouTube(link)
        yt_stream  = yt.streams.filter(progressive=True, file_extension = extension).order_by("resolution").desc().first()
        yt_stream.download(output_path = save_path, filename = save_name)

        return

    def __getLink(self):
        #playsound(button_click)
        link = self.link_entry.get()
        name = self.name_entry.get()
        path = self.path_entry.get()
        extension = self.extension_entry.get()

        self.__downloader(link, path, name, extension)

        return

    def run_app(self):
        self.window.mainloop()
        return

if __name__ == "__main__":
    app = YouTubeDownloader()
    app.run_app()

