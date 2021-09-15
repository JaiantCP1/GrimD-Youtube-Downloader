from tkinter import *
from tkinter import filedialog, messagebox
#----------------------------------#
import youtube_dl
#----------------------------------#
from os import makedirs, system, getcwd
#----------------------------------#
from wget import download
from zipfile import ZipFile
#----------------------------------#
from threading import Thread

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
ux.iconbitmap(current_path+'\images\icon.ico')


#get typed link
def getlink():
    print(textbox.get())

#save directory
def askthedirectory():
    global newdirectory
    newdirectory = filedialog.askdirectory()
    b = Label(ux,font='Arial,17', bg='#6d4e6e',text='                                                                                                                                         ')
    a = Label(ux,font='Arial,17',bg='#6d4e6e',fg='white',text='Pasta destino: '+newdirectory)
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
    in_progress = Label(ux,font=('Arial',18),fg='white',bg='#6d4e6e',text='                   Baixando Vídeo(s)!                   ')
    in_progress.grid(row=4,column=0,pady=30)
    
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([textbox.get()])
    
    download_complete = messagebox.askokcancel("GrimD", "Download concluído!")
    
    terminated = Label(ux,font=('Arial',18),fg='white',bg='#6d4e6e',text='                   Vídeo(s) Baixado(s)!                   ')
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
            }],
        }
    in_progress = Label(ux,font=('Arial',18),fg='white',bg='#6d4e6e',text='                   Baixando Música(s)!                   ')
    in_progress.grid(row=4,column=0,pady=30)
    
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([textbox.get()])
    
    download_complete = messagebox.askokcancel("GrimD", "Download concluído!")

    terminated = Label(ux,font=('Arial',18),fg='white',bg='#6d4e6e',text='                   Música(s) Baixada(s)!                   ')
    terminated.grid(row=4,column=0,pady=30)

#Download ffmpeg
def fix_ffmpeg_all():
    ask_download = messagebox.askokcancel("GrimD", "Aperte OK para começar a instalação do FFmpeg (só é necessário uma vez)")
    if ask_download:
    
        fixing = Label(ux,font='Arial,17',fg='white',bg='#6d4e6e',text='Concertando FFmpeg, por favor aguarde!')
        fixing.grid(row=4,column=0,pady=30)
        try:
            makedirs('/gFFmpeg')
        except:
            pass
    
        ffmpeg_url = 'https://github.com/JaintC/GrimD-YoutubeDL/releases/download/v1.1.2/gffmpeg-4.4-essentials_build.zip'
        download(ffmpeg_url, '/gFFmpeg/gffmpeg-4.4-essentials_build.zip')

        with ZipFile('C:/gFFmpeg/gffmpeg-4.4-essentials_build.zip', 'r') as zip_ref:
            zip_ref.extractall('/gFFmpeg')

        system('SETX PATH "%PATH%;C:\gFFmpeg\gffmpeg-4.4-essentials_build\gbin" ')
        fixed = Label(ux,font='Arial,17',fg='white',bg='#6d4e6e',text='                   Reabra o aplicativo!                   ')
        fixed.grid(row=4,column=0,pady=30)
        info = messagebox.showinfo("GrimD", "Reabra o aplicativo para aplicar as configurações")
        ux.quit()

#Background
background_image=PhotoImage(file= current_path+ "\images\Camada1.png")
background_label = Label(ux, image=background_image, background='black')
background_label.place(x=0, y=0, relwidth=1, relheight=1)

#Top
text = Label(ux, text='            GrimD Downloader', font=('Arial',25),fg = '#ca00ff',bg='#4c4e6f')
text.grid(row=0,column=0)

#TextBox
textbox = Entry(ux, bg= '#ca00ff',fg = 'white', font = ('Arial', 14), width = 50)
textbox.grid(row=1,column=0,padx=20,pady=00)

#Button 720p
img720 = PhotoImage(file= current_path+ "\images\Video.png")
baixar1 = Button(ux, image = img720, bg='#456686',highlightthickness = 0, bd = 0, command=lambda:[Thread(target=getlink).start(),Thread(target=download_720).start()])
baixar1.grid(row=1,column=1,padx=20,pady=20)

#Button Mp3
mp3img= PhotoImage(file= current_path+ "\images\Mp3.png")
baixar2 = Button(ux,image = mp3img,background = '#536b89',highlightthickness = 0, bd = 0,command=lambda:[Thread(target=getlink).start(),Thread(target=download_mp3).start()])
baixar2.grid(row=2,column=1,padx=1,pady=1)

#Directory
mudardiretorioimg = PhotoImage(file= current_path+ "\images\Diretorio.png")
mudardiretorio = Button(ux,image = mudardiretorioimg,highlightthickness = 0, bd = 0, bg='#545276', command=askthedirectory)
mudardiretorio.grid(row=3,column=0,padx=20,pady=20)

#MenuBar
my_menu = Menu(ux)
ux.config(menu=my_menu)

opcoes_menu = Menu(my_menu,tearoff=0)
my_menu.add_cascade(label='Opções',activebackground='black', activeforeground='purple', menu=opcoes_menu)
opcoes_menu.add_command(label='FFmpeg Fix', command=lambda:[Thread(target=fix_ffmpeg_all).start()])
opcoes_menu.add_command(label='Fechar', command=ux.quit)
#-----#
def cant_download_videos():
    help1 = messagebox.askokcancel("GrimD Help", "Infelizmente, o youtube bloqueia a visualização de vídeos com restrição de idade e localização.")
def cant_convert_mp3():
    help2 = messagebox.askokcancel("GrimD Help","Para que as converções para mp3 funcionem, vá no menu: Opções/FFmpeg Fix e isso será resolvido (reabra o aplicativo para fazer efeito)")

help_menu = Menu(my_menu, tearoff=0)
my_menu.add_cascade(label='Ajuda', menu=help_menu)
help_menu.add_command(label='Não consigo baixar um certo vídeo',command=cant_download_videos)
help_menu.add_command(label='Vídeos não estão sendo convertidos para mp3',command=cant_convert_mp3)

#Additional Info
text = Label(ux,font='Arial,14',text='GrimD Ver 1.2.0 - Made by JaintC - Ux by Biskatuxa', bg = '#6d4e6e',fg = 'white')
text.grid(row=5,column=0,padx=100,pady=140)

ux.mainloop()

#end
