import os
from mutagen.easyid3 import EasyID3

ruta_directorio = "./media/musica2"

def data_files():
    for nombre_archivo in os.listdir(ruta_directorio):
        ruta_archivo = os.path.join(ruta_directorio, nombre_archivo)
        
        print(ruta_archivo)

        if nombre_archivo.endswith('.mp3'):
            audio = EasyID3(ruta_archivo)
            print(audio)
            if len(audio) != 0:
                nuevo_nombre = audio["title"][0]

                print(nuevo_nombre)
                nueva_ruta_archivo = os.path.join("./media/musica3", nuevo_nombre)
        
                os.rename(ruta_archivo,str(nueva_ruta_archivo)+'.mp3')
            else:
                print("error")
            

data_files()