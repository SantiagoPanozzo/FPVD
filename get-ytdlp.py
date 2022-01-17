# Importar librerias
import os
from os import path

# Chequear la presencia de aria2 en el directorio bin
if path.exists(r'.\bin\aria2c.exe') == False:
    print('aria2 no encontrado, descargando...\n')
    exec(open('get-aria2.py').read())

# Descargar yt-dlp.exe a traves de aria2c
os.system(r'cmd /c ".\bin\aria2c.exe https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp.exe -o .\bin\yt-dlp.exe --allow-overwrite=true"')

# Descargar ytdlp.exe a traves de wget
# os.system(r'cmd /c ".\bin\wget.exe https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp.exe -O .\bin\yt-dlp.exe"')