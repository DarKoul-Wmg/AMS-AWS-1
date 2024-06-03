""" Exercici 4:
Dissenya una funció que rebi dos llistes i retorni els elements comuns a ambdós, sense repetir cap (intersecció de
conjunts). Exemple: si rep les llistes [1, 2, 1] i [2, 3, 2, 4], retornarà la llista [2]."""


def interseccion_conjuntos(lista1, lista2):
    # Convertir las listas en conjuntos para eliminar elementos duplicados.
    set1 = set(lista1)
    set2 = set(lista2)

    # Realizar la intersección de conjuntos y convertirla de nuevo a lista.
    interseccion = list(set1.intersection(set2))

    return interseccion


lista1 = [1, 2, 3, 4]
lista2 = [1, 2, 3, 5]
resultado = interseccion_conjuntos(lista1, lista2)
print("Elementos comunes a ambas listas:", resultado)
