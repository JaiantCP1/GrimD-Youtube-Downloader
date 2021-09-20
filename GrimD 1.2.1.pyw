from tkinter import *
from tkinter import filedialog, messagebox
#----------------------------------#
import youtube_dl
#----------------------------------#
from os import makedirs, system, getcwd, execl
import sys
#----------------------------------#
from wget import download
from zipfile import ZipFile
#----------------------------------#
from threading import Thread
#----------------------------------#
import webbrowser
#----------------------------------#

#Code by JaintC
#ytdl

#----------------------------------#
#todo:
#-add all options
#-only one button to download
#-progressbar
#----------------------------------#

#Current path
current_path = getcwd()

#Window Info
ux = Tk()
ux.title('GrimD Video Downloader')

#User resolution
global Largura, Altura, Posx, Posy
Largura = ux.winfo_screenwidth()
Altura = ux.winfo_screenheight()
Posx = (Largura/2 - 720/2) - 10
Posy = (Altura/2 - 450/2) - 40

#Define resolution and positioning
ux.geometry('720x450+%d+%d' % (Posx,Posy))
ux.resizable(0,0)
ux.configure(background='black')
ux.iconbitmap(current_path+'\lib\images\g_icon.ico')


#get typed link
def getlink():
    print(textbox.get())

#save directory
def askthedirectory():
    global newdirectory
    newdirectory = filedialog.askdirectory()
    b = Label(ux,font=('Cambria',14), bg='#16091d',text='                                                                                                                                         ')
    a = Label(ux,font=('Cambria',14),bg='#16091d',fg='white',text='Pasta destino: '+newdirectory)
    b.grid(row=2,column=0)
    a.grid(row=2,column=0)

#ydl stock options
ydl_opts = {}

#720p opts
def download_720():
    ydl_opts = {
            'default_search': 'auto',
            'format': 'bestvideo[height<=720]+bestaudio[ext=m4a]',
            'merge_output_format': 'mp4',
            'ignoreerrors' : 'True',
            'outtmpl' : newdirectory + '/%(title)s.%(ext)s'
        }
    in_progress = Label(ux,font=('Cambria',18),fg='white',bg='#251539',text='                   Baixando Vídeo(s)!                   ')
    in_progress.grid(row=4,column=0,pady=30)
    
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([textbox.get()])
    
    download_complete = messagebox.askokcancel("GrimD", "Download concluído!")
    
    terminated = Label(ux,font=('Cambria',18),fg='white',bg='#251539',text='                   Vídeo(s) Baixado(s)!                   ')
    terminated.grid(row=4,column=0,pady=30)

#360p opts
def download_360():
    ydl_opts = {
            'default_search': 'auto',
            'format': 'bestvideo[height<=360]+bestaudio[ext=m4a]',
            'merge_output_format': 'mp4',
            'ignoreerrors' : 'True',
            'outtmpl' : newdirectory + '/%(title)s.%(ext)s'
        }
    in_progress = Label(ux,font=('Arial',18),fg='white',bg='#251539',text='                   Baixando Vídeo(s)!                   ')
    in_progress.grid(row=4,column=0,pady=30)
    
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([textbox.get()])
    
    download_complete = messagebox.askokcancel("GrimD", "Download concluído!")
    
    terminated = Label(ux,font=('Arial',18),fg='white',bg='#251539',text='                   Vídeo(s) Baixado(s)!                   ')
    terminated.grid(row=4,column=0,pady=30)

#mp3 opts
def download_mp3():
    ydl_opts = {
            'default_search': 'auto',
            'format': 'bestaudio/best',
            'outtmpl': newdirectory + '/%(title)s.%(ext)s',
            'ignoreerrors' : 'True',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '256',
            }
            ],
        }
    
    in_progress = Label(ux,font=('Cambria',17),fg='white',bg='#251539',text='                   Baixando Música(s)!                   ')
    in_progress.grid(row=4,column=0,pady=30)
    
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([textbox.get()])
    
    download_complete = messagebox.askokcancel("GrimD", "Download concluído!")

    terminated = Label(ux,font=('Cambria',17),fg='white',bg='#251539',text='                   Música(s) Baixada(s)!                   ')
    terminated.grid(row=4,column=0,pady=30)

#Download ffmpeg
def fix_ffmpeg_all():
    ask_download = messagebox.askokcancel("GrimD", "Aperte OK para começar a instalação do FFmpeg (só é necessário uma vez)")
    if ask_download:
    
        fixing = Label(ux,font=('Cambria',18),fg='white',bg='#251539',text='Concertando FFmpeg, por favor aguarde!')
        fixing.grid(row=4,column=0,pady=30)
        try:
            makedirs('/gFFmpeg')
        except:
            pass
    
        ffmpeg_url = 'https://github.com/JaintC/GrimD-YoutubeDL/releases/download/v1.1.2/gffmpeg-4.4-essentials_build.zip'
        download(ffmpeg_url, '/gFFmpeg/gffmpeg-4.4-essentials_build.zip')

        with ZipFile('C:/gFFmpeg/gffmpeg-4.4-essentials_build.zip', 'r') as zip_ref:
            zip_ref.extractall('/gFFmpeg')

        system('SETX PATH "%PATH%;C:\gFFmpeg\gffmpeg-4.4-essentials_build\gbin"')
        fixed = Label(ux,font=('Cambria',18),fg='white',bg='#251539',text='                   Reabra o aplicativo!                   ')
        fixed.grid(row=4,column=0,pady=30)
        
        info = messagebox.showinfo("GrimD", "Para que as alterações sejam feitas, abra novamente o aplicativo!")
        restart = sys.executable
        ux.quit()

#Background
background_image=PhotoImage(file= current_path+ "\lib\images\g_background.png")
background_label = Label(ux, image=background_image, background='black')
background_label.place(x=0, y=0, relwidth=1, relheight=1)

#Top
text = Label(ux, text='GrimD Downloader', font=('Cambria Bold',25),fg = '#ca00ff',bg='#26143a')
text.grid(row=0,column=0)

#Options Text
text_options = Label(ux, text ='Opções:',fg='white', font=('Cambria',16),bg='#4b2674')
text_options.grid(row=0,column=1)

#TextBox
textbox = Entry(ux, bg= '#ca00ff',fg = 'white', font = ('Arial', 14), width = 50)
textbox.grid(row=1,column=0,padx=20,pady=00)

#Button 720p
img720 = PhotoImage(file= current_path+ "\lib\images\g_720p.png")
baixar1 = Button(ux, image = img720, bg='#53297d',highlightthickness = 0, bd = 0, command=lambda:[Thread(target=getlink).start(),Thread(target=download_720).start()])
baixar1.grid(row=1,column=1,padx=20,pady=20)

#Button 360p
img360 = PhotoImage(file= current_path+ "\lib\images\g_360p.png")
baixar1 = Button(ux, image = img360, bg='#5e2f8d',highlightthickness = 0, bd = 0, command=lambda:[Thread(target=getlink).start(),Thread(target=download_360).start()])
baixar1.grid(row=2,column=1,padx=20,pady=20)

#Button Mp3
mp3img= PhotoImage(file= current_path+ "\lib\images\g_mp3.png")
baixar2 = Button(ux,image = mp3img,background = '#48246c',highlightthickness = 0, bd = 0,command=lambda:[Thread(target=getlink).start(),Thread(target=download_mp3).start()])
baixar2.grid(row=3,column=1,padx=1,pady=1)

#Directory
mudardiretorioimg = PhotoImage(file= current_path+ "\lib\images\g_savepath.png")
mudardiretorio = Button(ux,image = mudardiretorioimg,highlightthickness = 0, bd = 0, bg='#29143d', command=askthedirectory)
mudardiretorio.grid(row=3,column=0,padx=20,pady=20)

#MenuBar
my_menu = Menu(ux)
ux.config(menu=my_menu)

opcoes_menu = Menu(my_menu,tearoff=0)
my_menu.add_cascade(label='Opções',activebackground='black', activeforeground='purple', menu=opcoes_menu)
opcoes_menu.add_command(label='FFmpeg Fix', command=lambda:[Thread(target=fix_ffmpeg_all).start()])
opcoes_menu.add_command(label='Fechar', command=ux.quit)
#-----#
def not_saving_path():
    help1 = messagebox.askokcancel("GrimD Help", 'Não se esqueça de salvar o diretório antes de baixar :)')
def cant_download_videos():
    help2 = messagebox.askokcancel("GrimD Help", "Infelizmente, o youtube bloqueia a visualização de vídeos com restrição de idade e localização.")
def cant_convert_mp3():
    help3 = messagebox.askokcancel("GrimD Help","Para que as converções para mp3 funcionem, vá no menu: Opções/FFmpeg Fix e isso será resolvido (reabra o aplicativo para fazer efeito)")
def version():
    help4 = messagebox.askokcancel("GrimD Version", "GrimD = Versão 1.2.1")

help_menu = Menu(my_menu, tearoff=0)
my_menu.add_cascade(label='Ajuda', menu=help_menu)
help_menu.add_command(label='Não está baixando nenhum vídeo ou música',command=not_saving_path)
help_menu.add_command(label='Não consigo baixar um certo vídeo',command=cant_download_videos)
help_menu.add_command(label='Vídeos não estão sendo convertidos para mp3',command=cant_convert_mp3)
#------#
def version():
    info1 = messagebox.askokcancel("GrimD Version", "GrimD = Versão 1.2.1")
def site():
    info2 = webbrowser.open('https://github.com/jaintc/grimd-youtubedl', 2) 

info_menu = Menu(my_menu, tearoff=0)
my_menu.add_cascade(label="Informações",menu=info_menu)
info_menu.add_command(label='Versão', command=version)
info_menu.add_command(label='Site Github',command=site)

ux.mainloop()

#end