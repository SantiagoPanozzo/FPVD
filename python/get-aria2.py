import os
from os import path
import urllib.request

# Definir la url de aria2 mas reciente a la hora de hacer la build actual, tengo que encontrar como automatizar esto...
aria2url = 'https://github.com/aria2/aria2/releases/download/release-1.36.0/aria2-1.36.0-win-64bit-build1.zip'

# Descargar aria2 desde la url especificada
urllib.request.urlretrieve(aria2url, r'.\temp\aria2.zip')
os.system(r'cmd /c "tar -xf .\temp\aria2.zip -C ".\temp')
os.system(r'cmd /c "del .\temp\aria2.zip"')
os.chdir('temp')
leer = str(os.listdir('.'))
leer2 = leer.replace('[','')
leer3 = leer2.replace("'","")
carpeta = leer3.replace(']','')
os.chdir(carpeta)
os.system(r'cmd /c "copy aria2c.exe ..\..\ /y"')
os.chdir('..\..')
os.system(r'cmd /c "copy aria2c.exe .\bin\aria2c.exe /y"')
os.system(r'cmd /c "del aria2c.exe"')
os.system(r'cmd /c "rmdir /Q /S .\temp\{}"'.format(carpeta))
print('aria2 encontrado! \n')