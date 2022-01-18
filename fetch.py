# Importar librerias
import os
from os import path

# Presentar opciones
print("""
Selecciona una opcion (escribe el numero y pulsa enter):
1) Descargar video con audio en mp4 (Recomendado)
2) Descargar SOLO audio en mp3
""")
while True:
    try:
        opcion = int(input('Opcion: '))
        break
    except:
        print("Escribe un numero por favor \n")

# Introduccion del link
print('\nPor favor introduce el link a descargar y pulsa enter: \n')
link = input('Link: ')
print('\nIniciando descarga, por favor espera... \n')
print('Por favor no toques nada hasta que el programa te avise que la descarga fue completada\n')

# Descarga el video o audio, dependiendo de la opcion elegida, utilizando la configuracion
# de yt-dlp apropiada
if(opcion == 1):
    os.system(r'cmd /c ".\bin\yt-dlp.exe {} --config-location .\configs\bestmp4.conf" -P .\download'.format(link))
    print("\nDescarga completada con exito! \n")
    print('Tu video deberia estar en la subcarpeta download')
elif(opcion == 2):
    os.system(r'cmd /c ".\bin\yt-dlp.exe {} --config-location .\configs\bestmp3.conf" -P .\download'.format(link))
    print("\nDescarga completada con exito! \n")
    print('Tu audio deberia estar en la subcarpeta download')
else:
    print("Esa no es una opcion!")