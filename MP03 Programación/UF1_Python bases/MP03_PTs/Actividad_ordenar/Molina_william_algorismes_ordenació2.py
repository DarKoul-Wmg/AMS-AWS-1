#Metodo2: Burbuja
lista = [5,6,1,9,22,31,12,2]
for pasada in range(len(lista)-1):
    for i in range(len(lista)-1-pasada):
        if lista[i] > lista[i + 1]:
            aux = lista[i]
            lista[i] = lista[i + 1]
            lista[i + 1] = aux
print(lista)