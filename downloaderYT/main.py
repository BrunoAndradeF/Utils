import yt_dlp
import sys

def progress_hook(d):
    if d['status'] == 'downloading':
        percent = d['_percent_str']  
        speed = d['_speed_str']  
        eta = d['_eta_str']  
        filename = d['filename']
        sys.stdout.write(f'\rBaixando {filename}: {percent} ({speed} - ETA: {eta})')
        sys.stdout.flush()
    elif d['status'] == 'finished':
        sys.stdout.write(f'\nDownload concluído: {d["filename"]}\n')
        sys.stdout.flush()

url = str(input("Video's URL: "))
path = str(input("Folder: "))

if len(path) == 0: path = "INSERT DEFAULT FOLDER"

if not path.endswith("/"): path+="/"

ydl_opts = {
    'format': 'bestvideo+bestaudio/best',
    'outtmpl': path+'%(title)s.%(ext)s',
    'progress_hooks': [progress_hook],
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

print("Download concluído!")
