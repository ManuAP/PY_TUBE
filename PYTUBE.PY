from pytube import Playlist
from pytube import YouTube
from pwn import *
from os import system
import signal, re
import sys
import pdb
import pyfiglet

tit_menu = pyfiglet.figlet_format("          MP3Tube")
tit_audio = pyfiglet.figlet_format("          Audio Download")
tit_video = pyfiglet.figlet_format("          Video Download")
def def_handler(sig, frame):
    print("\nSaliendo...")
    sys.exit(1)

signal.signal(signal.SIGINT, def_handler)

def getURLList(url):
    p = Playlist(url)
    return p.video_urls

def downloadVideo(url, i):
    yt = YouTube(url)
    name = str(i) + " " + yt.title + ".mp4"
    name = re.sub(r'[<>:"/\|*?]', "-" , name)

    p1 = log.progress("")
    system('cls')
    print(tit_video)
    try:

        st=yt.streams.get_by_itag(22)
        p1.status("Descargando: " + name)
        if st == "NONE":
            for s in yt.streams:
                print(s)
            itag = input('Elige un itag distinto por defecto es el 22 y no funciona:')
            st=yt.streams.get_by_itag(itag)
        else:
            st.download(output_path=path, filename=name)

    except Exception as e:
        print("No se ha podido descargar el video")

def downloadAudio(url, i):
    yt = YouTube(url)
    name = str(i) + " " + yt.title + ".mp4"
    name = re.sub(r'[<>:"/\|*?]', "-" , name)
    print(name)
    print("Descargando...")

    try:
        st=yt.streams.get_by_itag(140)
        if st == "NONE":
            for s in yt.streams:
                print(s)
            itag = input('Elige un itag distinto por defecto es el 22 y no funciona:')
            st=yt.streams.get_by_itag(itag)
        else:
            st.download(output_path=path, filename=name)

    except Exception as e:
        print(str(e))

if __name__ == '__main__':
    system('cls')
    print(tit_menu)
    url = input("\nIntroduce la URL: ")

    aov = input("\nDescargar Audio -> a Video -> v: ")
    opcion = input("\nSe trata de una lista S/N: ")
    carpeta = input("\nNobre de la carpeta donde se guardara: ")
    path = 'E:\Descargas\pytube\\' + str(carpeta)
    i = 1
    if opcion == "s" or opcion == "S":
        if aov == "a" or aov == "A":
            p1 = log.progress('Descarga de Audio')
            lista = getURLList(url)
            for link in lista:
                system('cls')
                print(tit_audio)
                p1.status('Descargando cancion: %d de %d' % (i, len(lista)))
                downloadAudio(link, i)
                i = i + 1
            system('cls')
            print(tit_audio)
            print("Audios de la lista descargados :)")
            sys.exit(0)
        elif aov == "v" or aov == "V":
            p2 = log.progress('Descarga de video:')
            lista = getURLList(url)
            for link in lista:
                system('cls')
                print(tit_video)
                p2.status('Descargando video: %d de %d' % (i, len(lista)))
                downloadVideo(link, i)
                i += 1
            system('cls')
            print(tit_video)
            print("Videos de la lista descargados :)")
            sys.exit(0)
        else:
            print("Error no se trata de una lista")
    elif opcion == "n" or opcion == "N":
        if aov == "a" or aov == "A":
            system('cls')
            print(tit_audio)
            downloadAudio(url, i)
            system('cls')
            print(tit_audio)
            print("Audio descargado :)")
            sys.exit(0)
        elif aov == "v" or aov == "V":
            system('cls')
            print(tit_video)
            downloadVideo(url, i)
            system('cls')
            print(tit_video)
            print("Video descargado :)")
            sys.exit(0)
    else:
        print("Error no se ha podido descargar nada")
        sys.exit(1)
