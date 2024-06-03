lista = [5,6,1,9,22,31,12,2]

for pasada in range(len(lista)-1):
     for j in range(pasada+1,len(lista)):
         # print("pasada = {}, j ={}".format(pasada,j))
         if lista[pasada] > lista[j]:
             aux = lista[pasada]
             lista[pasada] = lista[j]
             lista[j] = aux

print(lista)
