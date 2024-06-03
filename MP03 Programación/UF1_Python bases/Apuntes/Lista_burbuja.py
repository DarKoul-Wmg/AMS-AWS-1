lista =[5,6,1,9,22,31,12,2]
for recorrido in range(1, len(lista)):
    for posicion in range(len(lista) - recorrido):
        if lista[posicion] > lista[posicion + 1]:
            lista[posicion], lista[posicion + 1] = lista[posicion + 1], lista[posicion]
print(lista)

