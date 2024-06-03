import os

def exercici3(nom_directorio):

    directorio_crear = os.path.join(os.getcwd(),nom_directorio)
    directorio_final = os.path.join(directorio_crear,"backups","clients") #ruta absoluta y carpetas consecutivas

    if not os.path.exists(directorio_final):
        os.makedirs(directorio_final)
        print("Directorio creado")

    else:
        print("Ya existe este directorio")


nom_directorio = "MolinaWilliam"

exercici3(nom_directorio)
