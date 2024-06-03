def interseccionConjuntos(lista1,lista2):
    lista_Interseccion = []

    for num in lista1:
        if num in lista2 and not num in lista_Interseccion:
            lista_Interseccion.append(num)

    #print(lista_Interseccion)
    return lista_Interseccion


lista1 = [1,3,4,6,7,7]
lista2 = [2,3,4,7,7]

resultado = interseccionConjuntos(lista1,lista2)
print(resultado)
