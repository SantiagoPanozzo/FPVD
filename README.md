# FPVD
A minimal and Fool Proof Video Downloader script for Windows that is portable and only requires python to be executed.

Un script mínimo y A Prueba de Tontos para Windows que es portable y solo requiere python para ser ejecutado. 

## English:
A minimal, light, portable, easy-to-use command line script for downloading videos and audio files using [yt-dlp](https://github.com/yt-dlp/yt-dlp).
Currently it only works out-of-the-box on Windows 10 (1903) build 17063 and above, as it does requires the `tar` command introduced in said version (which you *may* otherwise be able to install yourself in other versions of Windows).
It is intended for people with little to no knowledge of CLIs, GNU, Linux, terminals, and all that juicy stuff.
Just run the `Launcher.bat` file and follow the instructions to download video and audio files.
The program works for YouTube, Vimeo, and all the other sites compatible with [youtube-dl](https://github.com/ytdl-org).
***All the texts in this program are written in Spanish.***

### Configurations:
There are two main configuration files that yt-dlp will use, one for downloading video with the best possible quality in mp4 format, and one for downloading audio in the best quality possible in mp3 format. **Editing these configuration files is not advised unless you have read and understood the [yt-dlp manuals](https://github.com/yt-dlp/yt-dlp#usage-and-options).**

## Español:
Un script de consola minimo, liviano, portable y facil de utilizar para descargar video y audio a través de yt-dlp en Windows que solo necesita python para ejecutarse.
Actualmente solo funciona en la version de Windows 10 (1903) build 17063 en adelante, ya que requiere el comando `tar` introducido en dicha versión (el cual *podrías* llegar a poder instalar por tu cuenta en otras versiones de Windows).
Esta hecho para personas con poco o nulo conocimiento de CLIs, GNU, Linux, terminales, y todas esas cosas jugosas.
Solo ejecuta el archivo `Launcher.bat` y sigue las instrucciones para descargar tus archivos de audio y video.
Este programa funciona para YouTube, Vimeo, y todos los otros sitios compatibles con [youtube-dl](https://github.com/ytdl-org).
***Todo el texto de este programa esta escrito en Español.***

### Configuraciones:
Hay dos archivos principales de configuración que yt-dlp va a utilizar, uno para descargar videos con la mejor calidad posible en formato mp4, y una para descargar audio en la mejor calidad posible en formato mp3. **Editar estos archivos de configuracion no es recomendado a no ser que hayas leído y comprendido los [manuales de yt-dlp](https://github.com/yt-dlp/yt-dlp#usage-and-options).**

## Dependencies / Dependencias:

- [Python 2/3](https://www.python.org/downloads/)

## Other dependencies:

- `tar` (already included in Windows 10 1903 and above) / (ya incluido en Windows 10 1903 en adelante).
- [`aria2`](https://github.com/aria2/aria2) (the script should download it automatically) / (el script deberia descargarlo automaticamente)
- [`ffmpeg`](https://www.ffmpeg.org/download.html) (the script should download it automatically) / (el script deberia descargarlo automaticamente)
- [`yt-dlp`](https://github.com/yt-dlp/yt-dlp) (the script should download it automatically) / (el script deberia descargarlo automaticamente)

# COPYRIGHT
This script and all its parts and related files are released into the public domain. I do not own or have participated in the development of yt-dlp, ffmpeg, or anything other than the python scripts in the root directory of this repository. All the credit goes to the open source programs used, which all are also in the public domain, and its creators and developers. For any other questions in this regard refer to the [GNU General Public License website](http://www.gnu.org/licenses/gpl-3.0) or the v3 copy present in this repository.
