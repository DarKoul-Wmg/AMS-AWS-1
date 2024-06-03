import random

def crearMatriz(fila,columna):
    resultado = []
    if fila >1:
        for i in range(fila):
            resultado.append([])
            for j in range(columna):
                resultado[i].append(random.randint(1,99))
    else:
        for i in range(columna):
            resultado.append(random.randint(1,99))

    return resultado

# print(crearMatriz(2,4))

def imprime_matriz(lista):
    try:
        if type(lista[0]) != list:
            raise ValueError(" Solo imprimir matrices con mas de una fila")

        elif len(lista[0]) <= 1:
            raise ValueError(" Solo imprimir matrices con mas de una columna")

        for i in range(len(lista)):
            for j in range(len(lista[0])):
                print(str(lista[i][j]).rjust(5),end="")
            print()
    except ValueError as error:
        print(error)
