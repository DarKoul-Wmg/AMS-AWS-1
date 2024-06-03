import os
import shutil

def carpeta():
    ruta_absoluta = os.getcwd() #Obtenemos el directorio completo de la ruta actual
    nom_carpeta = "Temp"
    ruta_temp = os.path.join(ruta_absoluta,nom_carpeta)

    if not os.path.exists(nom_carpeta):
        os.mkdir(nom_carpeta)
        print("Se ha creado la carpeta: "+ ruta_temp)

    else:
        #os.rmdir(nom_carpeta)
        shutil.rmtree(nom_carpeta) # Con esta opción nos aseguramos de borrar los archivos internos
        print("Se ha borrado la carpeta: "+ ruta_temp)

carpeta()
