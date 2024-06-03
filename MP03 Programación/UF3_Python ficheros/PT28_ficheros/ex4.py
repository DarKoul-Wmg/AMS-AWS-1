with open("archivo3","r") as fichero:
    lineas = 0
    palabras = 0
    caracter = 0

    datos = fichero.readlines()
    lineas = len(datos)

    for linea in datos:
        pal = linea.split()
        palabras += len(pal)
        caracter += len(linea)

print("Lineas: " + str(lineas))
print("Palabras: " + str(palabras))
print("Caracteres: " + str(caracter))
