from pytube import YouTube
import os
bool = True
# input de la url del usuario
while(bool):
    res = str(input("Introduzca el link del video: \n>> "))
    if res != "q":
        yt = YouTube(res)
# conseguir que solo se quede el audio
        video = yt.streams.filter(only_audio=True).first()
  
# el destino donde queremos que se descargue
        print("Elegir el destino: ")
        destination = str("C:\\Users\\User\\Downloads\\Canciones") or '.'
  
# descargar el archivo
        out_file = video.download(output_path=destination)
  
# guardar el archivo
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)

        print(yt.title + " se ha descargado correctamente.")

    else:
        print("Saliendo!")
        bool = False
