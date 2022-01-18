# Importar librerias
import os
from os import path

# Titulo
print("Fool Proof Video Downloader Updater")
print ("Esta herramienta te permitirá actualizar los programas utilizados por el script")

# Opciones
while True:
    print("""
Elige cual programa quieres actualizar:

1) yt-dlp
2) ffmpeg
3) Salir del actualizador
    """)
    while True:
        try:
            opcion = int(input('Opcion (1,2,3): '))
            break
        except:
            print("Escribe un numero por favor \n")
    if (opcion == 1):
        exec(open('.\python\get-ytdlp.py').read())
        print("yt-dlp actualizado correctamente \n")
    elif (opcion == 2):
        exec(open('.\python\get-ffmpeg.py').read())
        print("ffmpeg actualizado correctamente \b")
    elif (opcion == 3):
        break
    else:
        print("Esa no es una opción! \n")
    os.system('cls')