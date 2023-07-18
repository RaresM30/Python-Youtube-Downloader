from pytube import YouTube
from tkinter import *
import tkinter as tk
from urllib.error import HTTPError


def downloader():
    global res
    t = text.get()
    try:
        video = YouTube(t)
        if res1.get() == 1:
            res = '360p'
        elif res2.get() == 1:
            res = '720p'
        elif res3.get() == 1:
            res = '1080p'

        video_stream = video.streams.filter(progressive=True, file_extension='mp4', resolution=res).first()
        video_stream.download(filename="Untitled")
        Label(window, text="Downloaded Successfully").pack()
    except HTTPError as e:
        Label(window, text="Error: Video not available or removed").pack()


window = Tk()
window.geometry("700x350")
window.title("YTDownloader")

text = tk.StringVar()
res1 = IntVar()
res2 = IntVar()
res3 = IntVar()

Label(window, text="YT Downloader for all", bg="black", font=("Arial", 15), fg="red").pack()
Label(window, text="Enter the link to download", bg="yellow", font=("Arial", 12)).pack()
Entry(window, textvariable=text, width=50).pack()

Checkbutton(window, text='360p', onvalue=1, offvalue=0, variable=res1).pack()
Checkbutton(window, text='720p', onvalue=1, offvalue=0, variable=res2).pack()
Checkbutton(window, text='1080p', onvalue=1, offvalue=0, variable=res3).pack()
Button(window, text="Download", bg='green', command=downloader).pack()

window.mainloop()
