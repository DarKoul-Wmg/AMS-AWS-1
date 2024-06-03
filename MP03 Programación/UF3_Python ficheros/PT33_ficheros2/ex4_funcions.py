import os

# Pedir nombre y borrar archivo
def delNomFitxer():
    nom = input("Introduce el nombre del fichero a borrar: ")
    ruta_actual = os.getcwd()
    #print(ruta_actual)

    ruta_archivo = os.path.join(ruta_actual,nom)
    #print(ruta_archivo)

    if os.path.exists(ruta_archivo):
        os.remove(ruta_archivo)
        print("Se ha borrado elñ archivo: ",nom)
    else:
        print("No existe en el directorio actual un archivo con ese nombre")

#delNomFitxer()

# Pedir nombre y mostrar

def propNomFitxer():
    nom = input("Nombre del archivo para ver tamaño: ")
    ruta_actual = os.getcwd()
    ruta_archivo = os.path.join(ruta_actual,nom)

    if os.path.exists(ruta_archivo):
        mida = os.path.getsize(ruta_archivo)
        print("El tamaño del archivo seleccionado es:",mida,"bytes")
    else:
        print("El nombre introducido no existe en este directorio")
propNomFitxer()

# Convertir el tamaño a kilobytes o megabytes para una mejor legibilidad
#         if tamano_bytes < 1024:
#             tamano_legible = f"{tamano_bytes} bytes"
#         elif 1024 <= tamano_bytes < 1024**2:
#             tamano_legible = f"{tamano_bytes/1024:.2f} KB"
#         else:
#             tamano_legible = f"{tamano_bytes/(1024**2):.2f} MB"
