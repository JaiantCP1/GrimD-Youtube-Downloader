from __future__ import unicode_literals
import youtube_dl
import ffmpeg
from time import sleep
import os

reset = '\033[m'
red = '\033[31m'
purple = '\033[35m'
blue = '\033[34m'
white = '\033[37m'
cyan = '\033[36m'
yellow = '\033[33m'
green = '\033[32m'

print(f'\nGrimD Developer Build : Test 1.1')
print(f'\nFeatures: -AutoSearch Youtube (Thanks to renanrcp)')
print(f'          -Youtube Videos')
print(f'          -Instagram Videos')
print(f'          -Facebook Videos')
print(f'          -Tiktok Videos')
print(f'          -Twitter Videos')
print(f'          -Dailymotion Videos')
print(f'          -Pinterest Videos')
print(f'          -Reddit Videos')

reprocessamento = 1

while reprocessamento != 0:
    print('\n\n')
    # AutoSearch Options
    ydl_opts = {
        'default_search': 'auto',
        'merge_output_format': 'mp4',
        'outtmpl': '%(title)s.%(ext)s'
    }

    # User input link
    link = str(input('\nDigite o link do vídeo: '))

    # Clear console
    os.system('cls||clear')

    # Instagram
    if 'instagram.com' in link:
        sleep(0.5)
        print(f'{purple}Detected: Instagram Video')
        ydl_opts = {
            'format': 'mp4',
            'outtmpl': '%(title)s.%(ext)s',
        }
    # Tiktok
    elif 'tiktok.com' in link:
        sleep(0.5)
        print(f'{white}Detected: TikTok Video')
        ydl_opts = {
            'format': 'mp4',
            'outtmpl': '%(title)s.%(ext)s',
        }

    # Facebook
    elif 'facebook.com' in link or 'fb.watch' in link:
        sleep(0.5)
        print(f'{blue}Detected: Facebook Video')
        ydl_opts = {
            'format': 'mp4',
            'outtmpl': '%(title)s.%(ext)s',
        }

    # Dailymotion
    elif 'dailymotion.com' in link:
        sleep(0.5)
        print(f'{cyan}Detected: Dailymotion Video')
        ydl_opts = {
            'format': 'mp4',
            'outtmpl': '%(title)s.%(ext)s',
        }

    # Pinterest
    elif 'pinterest.com' in link:
        sleep(0.5)
        print(f'{red}Detected: Pinterest Video')
        ydl_opts = {
            'format': 'mp4',
            'outtmpl': '%(title)s.%(ext)s',
        }

    # Twitter
    elif 'twitter.com' in link:
        sleep(0.5)
        print(f'{cyan}Detected: Twitter Video')
        ydl_opts = {
            'format': 'mp4',
            'outtmpl': '%(title)s.%(ext)s',
        }

    # Tumblr
    elif 'tumblr.com' in link:
        sleep(0.5)
        print(f'{blue}Detected: Tumblr Video')
        ydl_opts = {
            'format': 'mp4',
            'outtmpl': '%(title)s.%(ext)s',
        }

    # Reddit
    elif 'reddit.com' in link:
        sleep(0.5)
        print(f'{yellow}Detected: Reddit Video')
        ydl_opts = {
            'format': 'mp4',
            'outtmpl': '%(title)s.%(ext)s',
        }

    # Youtube
    else:
        sleep(0.5)
        print(f'{red}Detected: Youtube Video')
        print('\n=/=/=/=/=/=/=/=/=/=/=/=/\nMP4:\n 1- 360p\n 2- 720p(HD)\n 3- 1080p(FullHD)\n 4- Maior qualidade '
              'disponível')
        print('=/=/=/=/=/=/=/=/=/=/=/=/=/\nMP3:\n 5- 256kbps')
        opcao = int(input('\nSua escolha: '))
        if opcao == 1:
            ydl_opts = {
                'default_search': 'auto',
                'format': 'bestvideo[height<=360]+bestaudio[ext=m4a]',
                'merge_output_format': 'mp4',
                'outtmpl': '%(title)s.%(ext)s',
            }
        elif opcao == 2:
            ydl_opts = {
                'default_search': 'auto',
                'format': 'bestvideo[height<=720]+bestaudio[ext=m4a]',
                'merge_output_format': 'mp4',
                'outtmpl': '%(title)s.%(ext)s',
            }
        elif opcao == 3:
            ydl_opts = {
                'default_search': 'auto',
                'format': 'bestvideo[height<=1080]+bestaudio[ext=m4a]',
                'merge_output_format': 'mp4',
                'outtmpl': '%(title)s.%(ext)s',
            }
        elif opcao == 4:
            ydl_opts = {
                'default_search': 'auto',
                'format': 'bestvideo+bestaudio[ext=m4a]',
                'merge_output_format': 'mp4',
                'outtmpl': '%(title)s.%(ext)s',
                }
        elif opcao == 5:
            ydl_opts = {
                'default_search': 'auto',
                'format': 'bestaudio/best',
                'outtmpl': '%(title)s.%(ext)s',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'mp3',
                    'preferredquality': '256',
                }],
            }

    # Download
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([link])
    print(f'{reset}')
    sleep(0.5)
    os.system('cls||clear')
    
