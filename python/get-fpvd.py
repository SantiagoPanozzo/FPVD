# Importar librerias
import os
from os import path

# Chequear la presencia de aria2 en el directorio bin
if path.exists(r'.\bin\aria2c.exe') == False:
    print('aria2 no encontrado, descargando...\n')
    exec(open('.\python\get-aria2.py').read())

# Descargar ultima version del codigo fuente del script de github
os.system(r'cmd /c ".\bin\aria2c.exe https://github.com/SnowieMischief/FPVD/archive/refs/heads/main.zip -o .\temp\main.zip --allow-overwrite=true"')

# Desempaquetar main.zip a traves de tar
os.system(r'cmd /c "tar -xf .\temp\main.zip -C .\temp"')

# Borrar el zip
os.system(r'cmd /c "del .\temp\main.zip"')

# cd a la carpeta temporal
os.chdir('temp')

# Conseguir el nombre de la version del codigo fuente y cd a la carpeta extraida
leer = str(os.listdir('.'))
leer2 = leer.replace('[','')
leer3 = leer2.replace("'","")
carpeta = leer3.replace(']','')
os.chdir(carpeta)

#Copiar todo lo extraido a la carpeta raiz del programa
os.system(r'cmd /c "Xcopy .\ ..\..\ /E /H /I /y"')

# cd a la carpeta raiz y borrar todo en la carpeta temporal
os.chdir("..\..")
os.system(r'cmd /c "rmdir /Q /S .\temp\{}"'.format(carpeta))