import tkinter as tk
from tkinter import  ttk,filedialog
from ttkbootstrap import Colors, Style
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-

import yt_dlp
import os
import webbrowser
import wget
from zipfile import ZipFile
from threading import Thread
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-

from all_formats_list import list_formats
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-

def download_format_selected():
    selected_format = list_combobox.get()
    selected_directory = cwd.get()

    if selected_format == 'mp4-144p':
        ydl_opts = {
            'default_search': 'auto',
            'format': 'bestvideo[height<=144]+bestaudio[ext=m4a]',
            'ignoreerrors' : 'True',
            'outtmpl' : selected_directory + '/%(title)s.%(ext)s',
            'merge_output_format': 'mp4',
        }
  
    if selected_format == 'mp4-240p':
        ydl_opts = {
            'default_search': 'auto',
            'format': 'bestvideo[height<=240]+bestaudio[ext=m4a]',
            'ignoreerrors' : 'True',
            'outtmpl' : selected_directory + '/%(title)s.%(ext)s',
            'merge_output_format': 'mp4',
        }
   
    if selected_format == 'mp4-360p':
        ydl_opts = {
            'default_search': 'auto',
            'format': 'bestvideo[height<=360]+bestaudio[ext=m4a]',
            'ignoreerrors' : 'True',
            'outtmpl' : selected_directory + '/%(title)s.%(ext)s',
            'merge_output_format': 'mp4',
        }

    if selected_format == 'mp4-480p':
        ydl_opts = {
            'default_search': 'auto',
            'format': 'bestvideo[height<=480]+bestaudio[ext=m4a]',
            'ignoreerrors' : 'True',
            'outtmpl' : selected_directory + '/%(title)s.%(ext)s',
            'merge_output_format': 'mp4',
        }

    if selected_format == 'mp4-720p':
        ydl_opts = {
            'default_search': 'auto',
            'format': 'bestvideo[height<=720]+bestaudio[ext=m4a]',
            'merge_output_format': 'mp4',
            'ignoreerrors' : 'True',
            'outtmpl' : selected_directory + '/%(title)s.%(ext)s',
            
        }

    if selected_format == 'mp4-1080p':
        ydl_opts = {
            'default_search': 'auto',
            'format': 'bestvideo[height<=1080]+bestaudio[ext=m4a]',
            'ignoreerrors' : 'True',
            'outtmpl' : selected_directory + '/%(title)s.%(ext)s',
            'merge_output_format': 'mp4',
        }

    if selected_format == 'mp4-1440p':
        ydl_opts = {
            'default_search': 'auto',
            'format': 'bestvideo[height<=1440]+bestaudio[ext=m4a]',
            'ignoreerrors' : 'True',
            'outtmpl' : selected_directory + '/%(title)s.%(ext)s',
            'merge_output_format': 'mp4',
        }

    if selected_format == 'mp4-2160p':
        ydl_opts = {
            'default_search': 'auto',
            'format': 'bestvideo[height<=2160]+bestaudio[ext=m4a]',
            'ignoreerrors' : 'True',
            'outtmpl' : selected_directory + '/%(title)s.%(ext)s',
            'merge_output_format': 'mp4',
        }
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
    
    if selected_format == 'mkv-144p':
        ydl_opts = {
            'default_search': 'auto',
            'format': 'bestvideo[height<=144]+bestaudio[ext=m4a]',
            'ignoreerrors' : 'True',
            'outtmpl' : '%(title)s.%(ext)s',
            'merge_output_format': 'mkv',
        }

    if selected_format == 'mkv-240p':
        ydl_opts = {
            'default_search': 'auto',
            'format': 'bestvideo[height<=240p]+bestaudio[ext=m4a]',
            'ignoreerrors' : 'True',
            'outtmpl' : '%(title)s.%(ext)s',
            'merge_output_format': 'mkv',
        }

    if selected_format == 'mkv-360p':
        ydl_opts = {
            'default_search': 'auto',
            'format': 'bestvideo[height<=360]+bestaudio[ext=m4a]',
            'ignoreerrors' : 'True',
            'outtmpl' : '%(title)s.%(ext)s',
            'merge_output_format': 'mkv',
        }

    if selected_format == 'mkv-480p':
        ydl_opts = {
            'default_search': 'auto',
            'format': 'bestvideo[height<=480p]+bestaudio[ext=m4a]',
            'ignoreerrors' : 'True',
            'outtmpl' : '%(title)s.%(ext)s',
            'merge_output_format': 'mkv',
        }

    if selected_format == 'mkv-720p':
        ydl_opts = {
            'default_search': 'auto',
            'format': 'bestvideo[height<=720]+bestaudio[ext=m4a]',
            'ignoreerrors' : 'True',
            'outtmpl' : '%(title)s.%(ext)s',
            'merge_output_format': 'mkv',
        }

    if selected_format == 'mkv-1080p':
        ydl_opts = {
            'default_search': 'auto',
            'format': 'bestvideo[height<=1080]+bestaudio[ext=m4a]',
            'ignoreerrors' : 'True',
            'outtmpl' : '%(title)s.%(ext)s',
            'merge_output_format': 'mkv',
        }

    if selected_format == 'mkv-1440p':
        ydl_opts = {
            'default_search': 'auto',
            'format': 'bestvideo[height<=1440]+bestaudio[ext=m4a]',
            'ignoreerrors' : 'True',
            'outtmpl' : '%(title)s.%(ext)s',
            'merge_output_format': 'mkv',
        }

    if selected_format == 'mkv-2160p':
        ydl_opts = {
            'default_search': 'auto',
            'format': 'bestvideo[height<=2160]+bestaudio[ext=m4a]',
            'ignoreerrors' : 'True',
            'outtmpl' : '%(title)s.%(ext)s',
            'merge_output_format': 'mkv',
        }
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-    
    
    if selected_format == 'mpeg-144p':
        ydl_opts = {
                'default_search': 'auto',
                'format': 'bestvideo[height<=144p]+bestaudio[ext=m4a]',
                'ignoreerrors' : 'True',
                'outtmpl' :selected_directory + '/%(title)s.%(ext)s',
                'postprocessors': [{
                'key' : 'FFmpegVideoConvertor',
                'preferedformat' : 'mpeg2'
            }]
        }
    
    if selected_format == 'mpeg-240p':
        ydl_opts = {
                'default_search': 'auto',
                'format': 'bestvideo[height<=240]+bestaudio[ext=m4a]',
                'ignoreerrors' : 'True',
                'outtmpl' :selected_directory + '/%(title)s.%(ext)s',
                'postprocessors': [{
                'key' : 'FFmpegVideoConvertor',
                'preferedformat' : 'mpeg2'
            }]
        }
    
    if selected_format == 'mpeg-360p':
        ydl_opts = {
                'default_search': 'auto',
                'format': 'bestvideo[height<=360]+bestaudio[ext=m4a]',
                'ignoreerrors' : 'True',
                'outtmpl' :selected_directory + '/%(title)s.%(ext)s',
                'postprocessors': [{
                'key' : 'FFmpegVideoConvertor',
                'preferedformat' : 'mpeg2'
            }]
        }
    
    if selected_format == 'mpeg-480p':
        ydl_opts = {
                'default_search': 'auto',
                'format': 'bestvideo[height<=480]+bestaudio[ext=m4a]',
                'ignoreerrors' : 'True',
                'outtmpl' :selected_directory + '/%(title)s.%(ext)s',
                'postprocessors': [{
                'key' : 'FFmpegVideoConvertor',
                'preferedformat' : 'mpeg2'
            }]
        }

    if selected_format == 'mpeg-720p':
        ydl_opts = {
            'default_search': 'auto',
            'format': 'bestvideo[height<=720]+bestaudio[ext=m4a]',
            'ignoreerrors' : 'True',
            'outtmpl' : selected_directory + '/%(title)s.%(ext)s',
            'postprocessors': [{
                'key' : 'FFmpegVideoConvertor',
                'preferedformat' : 'mpeg'
            }]
        }

    if selected_format == 'mpeg-1080p':
        ydl_opts = {
            'default_search': 'auto',
            'format': 'bestvideo[height<=1080]+bestaudio[ext=m4a]',
            'ignoreerrors' : 'True',
            'outtmpl' : selected_directory + '/%(title)s.%(ext)s',
            'postprocessors': [{
                'key' : 'FFmpegVideoConvertor',
                'preferedformat' : 'mpeg',
            }]
        }
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-

    if selected_format == 'mp3-128kbps':
        ydl_opts = {
            'default_search': 'auto',
            'format': 'bestaudio/best',
            'ignoreerrors' : 'True',
            'outtmpl' : selected_directory + '/%(title)s.%(ext)s',
            'postprocessors': [{
                'key' : 'FFmpegExtractAudio',
                'preferredcodec' : 'mp3',
                'preferredquality' : '128',
            }]
        }

    if selected_format == 'mp3-192kbps':
        ydl_opts = {
            'default_search': 'auto',
            'format': 'bestaudio/best',
            'ignoreerrors' : 'True',
            'outtmpl' : selected_directory + '/%(title)s.%(ext)s',
            'postprocessors': [{
                'key' : 'FFmpegExtractAudio',
                'preferredcodec' : 'mp3',
                'preferredquality' : '192',
            }]
        }

    if selected_format == 'mp3-256kbps':
        ydl_opts = {
            'default_search': 'auto',
            'format': 'bestaudio/best',
            'ignoreerrors' : 'True',
            'outtmpl' : selected_directory + '/%(title)s.%(ext)s',
            'postprocessors': [{
                'key' : 'FFmpegExtractAudio',
                'preferredcodec' : 'mp3',
                'preferredquality' : '256',
            }]
        }

    if selected_format == 'mp3-320kbps':
        ydl_opts = {
            'default_search': 'auto',
            'format': 'bestaudio/best',
            'ignoreerrors' : 'True',
            'outtmpl' : selected_directory + '/%(title)s.%(ext)s',
            'postprocessors': [{
                'key' : 'FFmpegExtractAudio',
                'preferredcodec' : 'mp3',
                'preferredquality' : '320',
            }]
        }
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-

    if selected_format == 'No conversion':
        ydl_opts = {'outtmpl' : '%(title)s.%(ext)s',}

    link = link_box.get()
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        
        black_clean = tk.Label(frame_progress,bg=color_bg,font=('Arial',17),text='                                                     ').grid(row=0,column=0)
        show_progress = tk.Label(frame_progress,bg=color_bg,fg='yellow',font=('Arial',17),text='Download in progress').grid(row=0,column=0)
        
        ydl.download([link])
        
        black_clean = tk.Label(frame_progress,bg=color_bg,font=('Arial',17),text='                                                     ').grid(row=0,column=0)
        show_finish = tk.Label(frame_progress,bg=color_bg,fg='#00FF00',font=('Arial',17),text='Finished Download').grid(row=0,column=0)

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-

def github():
    info2 = webbrowser.open('https://github.com/jaintc/grimd-youtubedl', 2) 

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-

def askdirectory():
    global current_path
    current_path = tk.filedialog.askdirectory()
    cwd.delete(0, tk.END)
    cwd.insert(0,current_path)

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-

def fix_ffmpeg_all():
    ask_download = tk.messagebox.askokcancel("GrimD", "Install ffmpeg?")
    if ask_download:
        try:
            os.makedirs('/gFFmpeg')
        except:
            pass
    
        black_clean = tk.Label(frame_progress,bg=color_bg,font=('Arial',17),text='                                                          ').grid(row=0,column=0)
        show_progress = tk.Label(frame_progress,bg=color_bg,fg='yellow',font=('Arial',17),text='         Download in progress').grid(row=0,column=0)

        ffmpeg_url = 'https://github.com/JaintC/GrimD-YoutubeDL/releases/download/v1.4.0/gffmpeg-2021-10-28-git-full_build.zip'
        wget.download(ffmpeg_url, '/gFFmpeg/gffmpeg-2021-10-28-git-full_build')

        with ZipFile('C:/gFFmpeg/gffmpeg-2021-10-28-git-full_build.zip', 'r') as zip_ref:
            zip_ref.extractall('/gFFmpeg')

        os.system('SETX PATH "%PATH%;C:\gFFmpeg\gffmpeg-4.4-essentials_build\gbin"')
        
        black_clean = tk.Label(frame_progress,bg=color_bg,font=('Arial',17),text='                                                          ').grid(row=0,column=0)
        show_finish = tk.Label(frame_progress,bg=color_bg,fg='#00FF00',font=('Arial',17),text='         Finished Download').grid(row=0,column=0)

        info = tk.messagebox.showinfo("GrimD", "Please reopen the app!")
        gui.quit()
        
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-

current_path = os.getcwd()

gui=tk.Tk()
gui.title('GrimD 1.4.0')
gui.geometry('640x400')
gui.resizable(0,0)
color_bg = '#1e1e1e'
gui.configure(bg='#1e1e1e')
gui.iconbitmap(current_path+"\images\icon_big.ico")
#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-

top = tk.Label(gui,fg='#bdbdbd',font=('Arial',24),text='GrimD Downloader',bg=color_bg).grid(row=0,column=1,pady=40)

link_text= tk.Label(gui,fg='#bdbdbd',bg=color_bg,text='Video link:',font=('Arial',16)).grid(row=1,column=0)
link_box = tk.Entry(gui,selectbackground='green', fg='#bdbdbd',bg=color_bg,font=('Arial',11),width=21)
link_box.grid(row=2,column=0,padx=5,pady=15)

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-
select_label = tk.Label(gui,fg='#bdbdbd',bg=color_bg,text='Format options:',font=('Arial',16)).grid(row=1,column=1)

style = ttk.Style()
style.theme_use('alt')

gui.option_add('*TCombobox*Listbox*Background', '#212121')
gui.option_add('*TCombobox*Listbox*Foreground', 'white')
gui.option_add('*TCombobox*Listbox*selectBackground', 'green')
gui.option_add('*TCombobox*Listbox*selectForeground', 'white')

style.map('TCombobox', fieldbackground=[('','#212121')])
style.map('TCombobox', selectbackground=[('', 'green')])
style.map('TCombobox', selectforeground=[('', 'white')])
style.map('TCombobox', background=[('', '#212121')])
style.map('TCombobox', foreground=[('', 'white')])
style.map('TCombobox', arrowcolor=[('', 'white')])

list_combobox = ttk.Combobox(gui,state="readonly",values=list_formats,font=('Arial',11))
list_combobox.set('mp3-256kbps')
list_combobox.grid(row=2,column=1,padx=0,pady=15)

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-

btn = tk.Button(gui,bg='green',fg='white',text='Download',command=lambda:[Thread(target=download_format_selected).start()])
btn.grid(row=2,column=2,padx=25)

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-

link_ask= tk.Label(gui,fg='#bdbdbd',bg=color_bg,border=0,text='Directory:',font=('Arial',16)).grid(row=3,column=0,pady=15)

cwd_text = tk.StringVar()
cwd = tk.Entry(gui,selectbackground='green', fg='white',bg=color_bg,font=('Arial',11),width=21,text=cwd_text)
cwd_text.set('C:\Music')
cwd.grid(row=4,column=0,padx=5)

button_directory = tk.Button(gui,fg='white',bg='#896b18',text='Directory',command=askdirectory)
button_directory.grid(row=5,column=0,pady=10)

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-

frame_progress = tk.Frame(gui,bg=color_bg,borderwidth=5,width=300,height=50)
frame_progress.place(x=230,y=280)

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-

button_github = tk.Button(gui,fg='white',bg='#375a7f',text='Github',command=lambda:[Thread(target=github).start()])
button_github.place(x=575,y=365)

button_ffmpeg = tk.Button(gui,fg='white',bg='#375a7f',text='FFmpeg',command=lambda:[Thread(target=fix_ffmpeg_all).start()])
button_ffmpeg.place(x=500,y=365)

#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-#-

gui.mainloop()
