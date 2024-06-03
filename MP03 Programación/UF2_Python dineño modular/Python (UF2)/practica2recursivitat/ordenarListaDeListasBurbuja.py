def ordenar_lista_de_listas(lista):
    n = len(lista)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if lista[j][0] > lista[j + 1][0]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]

# Ejemplo de uso
lista_de_listas = [[3, 2, 1], [6, 5, 4], [9, 8, 7]]
print("Lista de listas sin ordenar:", lista_de_listas)
ordenar_lista_de_listas(lista_de_listas)
print("Lista de listas ordenada:", lista_de_listas)
