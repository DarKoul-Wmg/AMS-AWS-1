lista = []

def procediment(lista):

    for valor in lista:
        print("*"* valor)
        print(" ")




for i in range(3):
    num = int(input("Introduce un numero entero: "))
    lista.append(num)

procediment(lista)
