import os
import shutil


def exercici3(nom_directorio):

    directorio_crear = os.path.join(os.getcwd(),nom_directorio)
    directorio_final = os.path.join(directorio_crear,"backups","clients") #ruta absoluta y carpetas consecutivas

    if not os.path.exists(directorio_final):
        #print(directorio_final)
        os.makedirs(directorio_final)
        print("Directorio creado: "+directorio_final)

    else:
        print("El directorio ya existe, vamos a borrarlo...")
        shutil.rmtree(nom_directorio)
        print("Directorio borrado, vuelva a ejecutar para crearlo")


nom_directorio = "MolinaWilliam"

exercici3(nom_directorio)
