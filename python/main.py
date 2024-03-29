# Cargar librerias y limpiar terminal para inicio
import os
from os import path
os.system('cls')

# Titulo
print("""
     ___      ___      __   __     ___  
    | __|    | _ \     \ \ / /    |   \ 
    | _|  _  |  _/  _   \   /  _  | |) |
    |_|  (_) |_|   (_)   \_/  (_) |___/ 

      - Fool Proof Video Downloader -
""")

# Chequear si existen las carpetas necesarias y crearlas si no estan
if path.exists(r".\temp") == False:
    os.mkdir(r".\temp")
if path.exists(r".\download") == False:
    os.mkdir(r".\download")
if path.exists(r".\bin") == False:
    os.mkdir(r".\bin")

# Chequear si ffmpeg, ffplay, ffprobe y yt-dlp existen en el directorio bin
ffmpegstat = path.exists(r".\bin\ffmpeg.exe")
ytdlpstat = path.exists(r".\bin\yt-dlp.exe")

# Comprobar la falta de alguno y descargarlos
if(ffmpegstat is False):
    print("La librería ffmpeg no existe en el directorio bin y es necesaria\n")
    input("Pulsa ENTER para descargarla, esto puede tardar un rato...\n")
    exec(open(r'.\python\get-ffmpeg.py').read())
    os.system('cls')
else: print("Encontrado ffmpeg!")

if(ytdlpstat is False):
    print("La librería yt-dlp no existe en el directorio bin y es necesaria\n")
    input("Pulsa ENTER para descargarla, esto puede tardar un rato... \n")
    exec(open(r'.\python\get-ytdlp.py').read())
    os.system('cls')
else: print("Encontrado ytdlp!")

# Ejecucion del script de descarga
print("Todo funcionando correctamente, iniciando! \n")

while True:
    exec(open(r'.\python\fetch.py').read())
    # Pregunta de descargar otro video
    print("\n¿Deseas descargar otro video/audio? (Introduce S o N y pulsa ENTER)")
    seguir = input("(S/Si/N/No): ")
    if seguir == "N" or seguir == "n" or seguir == "no" or seguir == "No":
        break
    os.system('cls')