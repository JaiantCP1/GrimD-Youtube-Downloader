from tkinter import *
from tkinter import filedialog
import youtube_dl
import os

#Code by JaintC
#ytdl

#todo: ask directory in a different button
#add all options
#only one button to download

ux = Tk()

ux.title('GrimD Youtube Downloader')
ux.geometry('1300x500+300+210')
ux.minsize(1225,250)
ux.configure(background='black')

#ydl stock options
ydl_opts = {}

#get typed link
def bt_onlick():
    print(textbox.get())

#720p opts
def download_720():
    directory = filedialog.askdirectory()
    ydl_opts = {
            'default_search': 'auto',
            'format': 'bestvideo[height<=720]+bestaudio[ext=m4a]',
            'merge_output_format': 'mp4',
            'outtmpl' : directory + '/%(title)s.%(ext)s'
        }
    
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([textbox.get()])

#mp3 opts
def download_mp3():
    directory = filedialog.askdirectory()
    ydl_opts = {
            'default_search': 'auto',
            'format': 'bestaudio/best',
            'outtmpl': directory + '/%(title)s.%(ext)s',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '256',
            }],
        }
    
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([textbox.get()])

text = Label(ux, text='GrimD Downloader', font=('Arial',25),fg = 'purple',bg='black')
text.grid(row=0,column=0)

#TextBox
textbox = Entry(ux,bg= 'gray',fg = 'white', font = ('Arial', 15), width = 100)
textbox.grid(row=1,column=0,padx=10,pady=10)

#Button 720p
baixar1 = Button(ux, text= '720p',bg = 'gray', fg = 'white',height = 5,width = 10, command=lambda:[bt_onlick(), download_720()])
baixar1.grid(row=1,column=1,padx=10,pady=10)

#Button Mp3
baixar2 = Button(ux, text= 'MP3',bg = 'gray',fg = 'white',height = 5,width = 10, command=lambda:[bt_onlick(), download_mp3()])
baixar2.grid(row=2,column=1,padx=1,pady=1)

#Additional Info
text = Label(ux, bg = 'gray',fg = 'white',text='Videos são baixados em 720p(HD)\n\nMade by JaintC')
text.grid(row=2,column=0,padx=10,pady=10)
ux.mainloop()
