# FPVD
A minimal and Fool Proof Video Downloader script for Windows that is portable and only requires python to be executed

## English:
A minimal, light, portable, easy-to-use command line script for downloading videos and audio files using [yt-dlp](https://github.com/yt-dlp/yt-dlp).
Currently it only works out-of-the-box on Windows 10 (1903) build 17063 and above, as it does requires the `tar` command introduced in said version (which you *may* otherwise be able to install yourself in other versions of Windows).
It is intended for people with little to no knowledge of CLIs, GNU, Linux, terminals, and all that juicy stuff.
Just run the `Launcher.bat` file and follow the instructions to download video and audio files.
***All the texts in this program are written in Spanish.***

### Configurations:
There are two main configuration files that yt-dlp will use, one for downloading video with the best possible quality in mp4 format, and one for downloading audio in the best quality possible in mp3 format. **Editing these configuration files is not advised unless you have read and understood the yt-dlp manuals.**

## Español:
Un script de consola minimo, liviano, portable y facil de utilizar para descargar video y audio a través de yt-dlp en Windows que solo necesita python para ejecutarse.
Actualmente solo funciona en la version de Windows 10 (1903) build 17063 en adelante, ya que requiere el comando `tar` introducido en dicha versión (el cual *podrías* llegar a poder instalar por tu cuenta en otras versiones de Windows).
Esta hecho para personas con poco o nulo conocimiento de CLIs, GNU, Linux, terminales, y todas esas cosas jugosas.
Solo ejecuta el archivo `Launcher.bat` y sigue las instrucciones para descargar tus archivos de audio y video.
***Todo el texto de este programa esta escrito en Español.***

## Dependencies / Dependencias:

- [Python 2/3](https://www.python.org/downloads/)

## Other dependencies:

- `tar` (already included in Windows 10 1903 and above) / (ya incluido en Windows 10 1903 en adelante).
- [`wget`](https://eternallybored.org/misc/wget/) (should already be in the /bin folder) / (ya debería estar en la carpeta /bin)
- [`ffmpeg`](https://www.ffmpeg.org/download.html) (the script should download it automatically) / (el script deberia descargarlo automaticamente)
- [`yt-dlp`](https://github.com/yt-dlp/yt-dlp) (the script should download it automatically) / (el script deberia descargarlo automaticamente)
