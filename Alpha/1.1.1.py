from tkinter import *
from tkinter import filedialog
import youtube_dl
from os import makedirs
from os import system
from wget import download
import zipfile

#Code by JaintC
#ytdl

#todo:
#add all options
#only one button to download

#Window Info
ux = Tk()
ux.title('GrimD Video Downloader')
ux.geometry('1015x250+430+310')
ux.resizable(0,0)
ux.configure(background='black')
ux.iconbitmap('C:/Users/jcsch/Downloads/icon.ico')

#ydl stock options
ydl_opts = {}

#get typed link
def bt_onlick():
    print(textbox.get())

#save directory
def askthedirectory():
    global newdirectory
    newdirectory = filedialog.askdirectory()
    a = Label(ux,font='Arial,13',bg='black',fg='white',text='Pasta destino: '+newdirectory)
    a.grid(row=2,column=0)

#720p opts
def download_720():
    ydl_opts = {
            'default_search': 'auto',
            'format': 'bestvideo[height<=720]+bestaudio[ext=m4a]',
            'merge_output_format': 'mp4',
            'outtmpl' : newdirectory + '/%(title)s.%(ext)s'
        }
    
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([textbox.get()])

#mp3 opts
def download_mp3():
    ydl_opts = {
            'default_search': 'auto',
            'format': 'bestaudio/best',
            'outtmpl': newdirectory + '/%(title)s.%(ext)s',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '256',
            }],
        }
    
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([textbox.get()])

#Download ffmpeg
url = 'https://download936.mediafire.com/towt9ktw2ung/nuns20pbvkgyklu/FFmpeg-Full.zip'
def downloadffmpeg():
    print('Baixando FFmpeg...')

    try:
        makedirs('/FFmpeg')
    except WindowsError:
        print('Pasta já existente')

    download(url, '/FFmpeg/FFmpeg-Full.zip')
    print('Download concluído.')

#Extract ffmpeg
def extractffmpeg():
    print('\nExtraindo FFmpeg...')
    with zipfile.ZipFile('C:/FFmpeg/FFmpeg-Full.zip', 'r') as zip_ref:
        zip_ref.extractall('/FFmpeg')
    print('Extração completa')

#Add to path
def addffmpegtopath():
    print('\nAdicionando ffmpeg ao path...')
    system('SETX PATH "%PATH%;C:\FFmpeg\FFmpeg-Full\lbin" ')
    print('FFmpeg foi adicionado ao path')

#Popup Close app
def popup():
    top = Toplevel()
    top.geometry('+600+500')
    top.configure(background='black')
    label1 = Label(top,fg='white',bg='purple', font= 'Arial, 20' , text='Para que as configurações sejam salvas, reabra o aplicativo')
    label1.pack()
    top.mainloop()

#Top
text = Label(ux, text='GrimD Downloader', font=('Arial',25),fg = 'purple',bg='black')
text.grid(row=0,column=0)

#TextBox
textbox = Entry(ux, bg= 'purple',fg = 'white', font = ('Arial', 15), width = 80)
textbox.grid(row=1,column=0,padx=10,pady=10)

#Button 720p
img720 = PhotoImage(file= r"C:/Users/jcsch/Downloads/Ux-Jainct/Video.png")
baixar1 = Button(ux, image = img720, bg='black',highlightthickness = 0, bd = 0, command=lambda:[bt_onlick(), download_720()])
baixar1.grid(row=1,column=1,padx=10,pady=10)

#Button Mp3
mp3img= PhotoImage(file= r"C:/Users/jcsch/Downloads/Ux-Jainct/Mp3.png")
baixar2 = Button(ux,image = mp3img,background = 'black',highlightthickness = 0, bd = 0,command=lambda:[bt_onlick(), download_mp3()])
baixar2.grid(row=2,column=1,padx=1,pady=1)

#Directory
mudardiretorio = Button(ux, text='Salvar diretório',fg='white',bg='black',command=askthedirectory)
mudardiretorio.grid(row=3,column=1,padx=10,pady=10)

#MenuBar
my_menu = Menu(ux)
ux.config(menu=my_menu)

file_menu = Menu(my_menu)
my_menu.add_cascade(label='Opções',activebackground='black', activeforeground='purple', menu=file_menu)
file_menu.add_command(label='FFmpeg Fix', command=lambda:[downloadffmpeg(),extractffmpeg(), addffmpegtopath(),popup()])
file_menu.add_command(label='Fechar', command=ux.quit)

#Additional Info
addinfo = PhotoImage(file= r"C:/Users/jcsch/Downloads/Ux-Jainct/info.png")
text = Label(ux, bg = 'black',fg = 'white', image = addinfo)
text.grid(row=4,column=0,padx=10,pady=10)

ux.mainloop()

#end
