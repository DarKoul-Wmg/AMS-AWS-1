
def imprimir(fichero, num):
    lineas = fichero.readlines()

    for i in range(num):
        print(lineas[i])



fichero = open("archivo1","r")

while True:
    num = input("Introduce un nombre para imprimir lineas: ")
    if num.isdigit() and not int(num) <= 0:
        imprimir(fichero, int(num))
        break

    else:
        print("Tiene que ser un numero o un valor valido")

fichero.close()
