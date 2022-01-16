# Importar librerias
import os

# Descargar ffmpeg.zip a traves de wget
os.system(r'cmd /c ".\bin\wget.exe https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip -O .\temp\ffmpeg.zip"')

# Desempaquetar ffmpeg.zip a traves de tar
os.system(r'cmd /c "tar -xf .\temp\ffmpeg.zip -C .\temp"')

# Borrar el zip
os.system(r'cmd /c "del .\temp\ffmpeg.zip"')

# cd a la carpeta temporal
os.chdir('temp')

# Conseguir el nombre de la version de ffmpeg y cd a la carpeta extraida
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