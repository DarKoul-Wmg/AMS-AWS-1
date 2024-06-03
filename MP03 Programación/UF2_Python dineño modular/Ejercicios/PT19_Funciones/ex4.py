lista1 = [1,3,4,6,8]
#lista1 = [0,2,4,6,8]
lista2 = [1,3,5,7,9]


def superposicio(lista1,lista2):
    encontrado = False
    for elemento in lista1:
        if elemento in lista2:
            encontrado = True

    return encontrado

resultado = superposicio(lista1,lista2)

print(resultado)
