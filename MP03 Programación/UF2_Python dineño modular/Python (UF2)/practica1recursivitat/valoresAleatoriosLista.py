import random


def insertar_valores_aleatorios(lista, n):
    if n == 0:
        return
    else:
        lista.append(random.randint(1, 100))
        return insertar_valores_aleatorios(lista, n - 1)


n = 5
lista = []
insertar_valores_aleatorios(lista, n)
print("Lista con valores aleatorios:", lista)
