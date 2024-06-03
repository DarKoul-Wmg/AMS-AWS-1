import os
import shutil

# 1 Crear directorio exercicis/Data/operacions
ruta_direct = "exercicis/Data/operacions"
def crearDirectorio(ruta_direct):
    if not os.path.exists(ruta_direct):
        os.makedirs(ruta_direct)

#crearDirectorio(ruta_direct)
# ----------------------------------------------------------------------------------------------------------------------
# 2 Pasar al archivo pacients.txt la información
def infoArchivo():
    fichero_pacientes = os.path.join(ruta_direct,"pacients.txt")
    pacient = {'nom': 'Pep', 'edat': 42, 'Diabetic': True}

    datos = ""
    for valor in pacient.values():
        datos += str(valor) + "    "
    datos += "\n"

    fichero = open(fichero_pacientes,"a+")
    print(datos)
    fichero.write(datos)
    fichero.close()

#infoArchivo()
# ----------------------------------------------------------------------------------------------------------------------

# 3 copiar estructura de directorios ---------import shutil-----------
def copiarDirect():
    if not os.path.exists("copia_exercici"):
        shutil.copytree("exercicis", "copia_exercici")

#copiarDirect()
# ----------------------------------------------------------------------------------------------------------------------

# 4 copiar archivo a carpeta data
def copiarArchivo():
    ruta_archivo = ruta_direct + "/pacients.txt"

    os.mkdir(ruta_direct+"/data") #Creamos carpeta en el directorio
    ruta_copia = ruta_direct + "/data/pacients.txt"
    shutil.copy(ruta_archivo,ruta_copia)

#copiarArchivo()
#5 eliminar un archivo
def eliminarArchivo():

    archivo_origen = ruta_direct + "/pacients.txt" # es lo mismo que: exercicis/Data/operacions/pacients.txt"
    os.remove(archivo_origen)

eliminarArchivo()
