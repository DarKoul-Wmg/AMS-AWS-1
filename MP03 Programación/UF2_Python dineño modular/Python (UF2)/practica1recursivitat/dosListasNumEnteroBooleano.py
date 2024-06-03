def listas_iguales(lista1, lista2):
    if len(lista1) != len(lista2):
        return False
    elif len(lista1) == 0:
        return True
    else:
        return (lista1[0] == lista2[0]) and listas_iguales(lista1[1:], lista2[1:])


lista1 = [1, 2, 3, 4, 5]
lista2 = [1, 2, 3, 4, 5]
print("¿Las listas son iguales?:", listas_iguales(lista1, lista2))
