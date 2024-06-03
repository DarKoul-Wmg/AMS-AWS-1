import os
import shutil

def exercici4(fichero,directorio):
    if not os.path.exists(fichero):
        print("El archivo no existe en el directorio de trabajo")

    elif not os.path.exists(directorio):
        print("La ruta dada no existe en este directorio")

    else:
        ruta_fichero = os.path.join(os.getcwd(),fichero)
        ruta_copia = os.path.join(directorio,"backups","clients")
        shutil.copy(ruta_fichero,ruta_copia)
        print("Archivo copiado")

fichero = "clients.txt"
directorio = "MolinaWilliam"
exercici4(fichero,directorio)
