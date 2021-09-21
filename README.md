# GrimD Downloader
## Aplicativo para Windows que permite baixar Vídeos do Youtube e outros sites.


#### [DESCRIÇÃO](https://github.com/JaiantCP1/GrimD-Youtube-Downloader#descri%C3%A7%C3%A3o)
#### [REQUISITOS](https://github.com/JaiantCP1/GrimD-Youtube-Downloader#requisitos)
#### [DOWNLOADS](https://github.com/JaiantCP1/GrimD-Youtube-Downloader#downloads)
#### [INSTALAÇÃO](https://github.com/JaiantCP1/GrimD-Youtube-Downloader#instala%C3%A7%C3%A3o)


## Descrição:

GrimD é um projeto para baixar vídeos do youtube (e outros sites) usando [youtube-dl](https://github.com/ytdl-org/youtube-dl)

Você tem total liberdade para editar este projeto e torná-lo seu.

Interface feita com [tkinter](https://docs.python.org/3/library/tkinter.html)

<div style="display: inline_block"><br>
 <img alt="Jean-GrimD" src="https://cdn.discordapp.com/attachments/733782835067879487/889618212445102080/ezgif.com-gif-maker_7.gif">
 </div>

## Observações:
#### O botão 720p baixa videos em 720p(webm), sendo eles convertidos para MP4 (ffmpeg)
#### O botão 360p baixa videos em 360p, sendo eles convertidos para MP4 (ffmpeg)
#### O botão MP3 baixa audios em M4A e usando o ffmpeg converte para MP3
#### É possível fazer download de vídeos pelo nome (sem precisar do link) e também download de playlists
#### O youtube-dl permite o download de vídeos em outros sites, porém devido à conversão pode ser que os vídeos não baixem


## Instalação Windows (v1.2.1):
#### [Visual C++](https://aka.ms/vs/16/release/vc_redist.x64.exe)
#### [FFmpeg](https://ffmpeg.org/download.html) adicionado ao path (caso queira adiciona-lo manualmente)\

#### 1- Baixe e instale o GrimD
#### 2- Abra o GrimD.exe. Depois de aberto, vá no menu opções/ffmpeg fix (só é necessário fazer este processo uma vez [caso vc já tenha o ffmpeg adicionado ao path não precisa]).
#### 3- Feche o programa e abra novamente
#### 4- Aproveite!

## Variante linux (v1.2.1):
```
sudo apt-get update
sudo apt-get install ffmpeg
```
#### 1- Baixe o arquivo GrimD Linux
#### 2- Extraia a pasta
#### 3- Execute o GrimD:
```
cd <DiretórioPastaExtraída>
chmod +x Grimd
./GrimD
```
