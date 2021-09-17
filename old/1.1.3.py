from tkinter import *
from tkinter import filedialog, messagebox
#----------------------------------#
import youtube_dl
#----------------------------------#
from os import makedirs, system, getcwd
#----------------------------------#
from wget import download
import zipfile
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
largura = ux.winfo_screenwidth()
altura = ux.winfo_screenheight()
posx = (largura/2 - 720/2) - 10
posy = (altura/2 - 450/2) - 40

#Define resolution and positioning
ux.geometry('720x450+%d+%d' % (posx,posy))
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
    a = Label(ux,font='Arial,17',bg='#6d4e6e',fg='white',text='Pasta destino: '+newdirectory)
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
    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([textbox.get()])
    except:
        print('')

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

    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([textbox.get()])
    except:
        print('')

#Download ffmpeg
ffmpeg_url = 'https://github.com/JaintC/GrimD-Youtube-Downloader/releases/download/v1.1.2/gffmpeg-4.4-essentials_build.zip'

def downloadffmpeg():
    print('Baixando FFmpeg...')

    try:
        makedirs('/gFFmpeg')
    except WindowsError:
        print('Pasta já existente')

    download(ffmpeg_url, '/gFFmpeg/gffmpeg-4.4-essentials_build.zip')
    print('Download concluído.')

#Extract ffmpeg
def extractffmpeg():
    print('\nExtraindo FFmpeg...')
    with zipfile.ZipFile('C:/gFFmpeg/gffmpeg-4.4-essentials_build.zip', 'r') as zip_ref:
        zip_ref.extractall('/gFFmpeg')
    print('Extração completa')


#Add to path
def addffmpegtopath():
    print('\nAdicionando ffmpeg ao path...')
    system('SETX PATH "%PATH%;C:\gFFmpeg\gffmpeg-4.4-essentials_build\gbin" ')
    print('FFmpeg foi adicionado ao path')

#Popup Close app
def popupclose():
    info = messagebox.showinfo("GrimD", "Reabra o aplicativo para aplicar as configurações")
    ux.quit()
#Popup Wait
def popupwait():
    wait = messagebox.showinfo("GrimD", "Aperte OK para começar a instalação do FFmpeg (só é necessário uma vez)")

#Background
background_image=PhotoImage(file= current_path+ "\images\Camada1.png")
background_label = Label(ux, image=background_image, background='black')
background_label.place(x=0, y=0, relwidth=1, relheight=1)

#Top
text = Label(ux, text='GrimD Downloader', font=('Arial',25),fg = '#ca00ff',bg='#4c5577')
text.grid(row=0,column=0)

#TextBox
textbox = Entry(ux, bg= '#ca00ff',fg = 'white', font = ('Arial', 15), width = 50)
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

file_menu = Menu(my_menu)
my_menu.add_cascade(label='Opções',activebackground='black', activeforeground='purple', menu=file_menu)
file_menu.add_command(label='FFmpeg Fix', command=lambda:[popupwait(),downloadffmpeg(),extractffmpeg(), addffmpegtopath(),popupclose()])
file_menu.add_command(label='Fechar', command=ux.quit)

#Additional Info
text = Label(ux,font='Arial,14',text='GrimD Ver 1.1.3 - Made by JaintC - Ux by Biskatuxa', bg = '#6d4e6e',fg = 'white')
text.grid(row=4,column=0,padx=100,pady=150)

ux.mainloop()

#end
