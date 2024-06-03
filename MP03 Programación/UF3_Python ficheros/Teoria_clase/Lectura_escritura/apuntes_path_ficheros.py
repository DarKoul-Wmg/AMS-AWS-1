import os
import shutil

print(os.getcwd()) # Mostrar mi ubicación

print(os.listdir()) # Listar archivos en ubicación actual

lista = os.listdir() # Se pueden guardar los archivos de un directorio dentro de una lista

os.chdir("path") # Nos desplaza al directorio introducido

os.mkdir("nom_carpeta") # Crea una nueva carpeta

os.makedirs("ruta/de/archivos") # Crea mas de una carpeta con subdirectorios

os.remove("nom_archivo") # Borra el archivo introducido

os.rmdir("ruta/o/carpeta") # Borra una carpeta o directorio

shutil.rmtree("ruta/o/carpeta") #para la eliminación recursiva de la carpeta y su contenido (archivos).

os.path.exists("nom_carpeta") # Devuelve True or False segun existe el directorio o no

