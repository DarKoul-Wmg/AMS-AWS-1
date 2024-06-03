fichero1 = open("1a100.txt","r")
fichero_linea = open("15arxiu2","r")

entradas = fichero_linea.readlines()
datos = fichero1.readlines()
for num in entradas:
    num = int(num)
    print("linea: " + str(num))
    print("datos: " + str(datos[num-1]))

fichero1.close()
fichero_linea.close()
