import random


def insertar_valores_aleatorios_sin_repeticion(lista, n):
    if n == 0:
        return
    else:
        valor = random.randint(1, 100)
        if valor not in lista:
            lista.append(valor)
            return insertar_valores_aleatorios_sin_repeticion(lista, n - 1)
        else:
            return insertar_valores_aleatorios_sin_repeticion(lista, n)


n = 5
lista = []
insertar_valores_aleatorios_sin_repeticion(lista, n)
print("Lista con valores aleatorios sin repetición:", lista)
