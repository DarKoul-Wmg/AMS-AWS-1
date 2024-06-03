import random

dimension = 4
matriz =[]
for fila in range(dimension):
    matriz.append([])
    for columna in range(dimension):
        matriz[fila].append(random.randint(1,100))
for fila in range(dimension):
    for columna in range(dimension):
        print(str(matriz[fila][columna]).rjust(5), end=" ")
    print()

print("\n *****************PRUEBA DE ORDENAR UNA FILA AL REVÉS******************")
# fila = 2
# for pasada in range(len(matriz)-1):
#         for j in range(len(matriz)-1, pasada, -1):
#
#             if matriz[fila][j] > matriz[fila][j-1]:
#                     aux = matriz[fila][j]
#                     matriz[fila][j] = matriz[fila][j-1]
#                     matriz[fila][j-1] = aux
#
# for fila in range (dimension):
#     for columna in range(dimension):
#         print(str(matriz[fila][columna]).rjust(5),end=" ")
#     print()
print("\n *****************PRUEBA DE ORDENAR TODAS LAS FILAS AL REVÉS******************")


# for fila in range(len(matriz)):
#     for pasada in range(len(matriz)-1):
#         for j in range(len(matriz)-1, pasada, -1):
#
#             if matriz[fila][j] > matriz[fila][j-1]:
#                     aux = matriz[fila][j]
#                     matriz[fila][j] = matriz[fila][j-1]
#                     matriz[fila][j-1] = aux
#
# for fila in range (dimension):
#     for columna in range(dimension):
#         print(str(matriz[fila][columna]).rjust(5),end=" ")
#     print()

print("\n *****************PRUEBA DE ORDENAR DIAGONAL / ******************")
#DEPENDENCIA:
# j = len(matriz)-1-pasada
#Aqui j es la fila
for i in range(len(matriz)):
    print(matriz[i][len(matriz)-1-i], end=" ")
print ("\n")
for pasada in range(len(matriz)-1):
    for j in range(len(matriz)-1 - pasada):#Establecer como limite la pasada
        # print("pasada = {}, elemento1 = {},{}, elemento2 = {}, {}".format(pasada, j, len(matriz)-1-j, j+1,len(matriz)-1-j-1))
        if matriz[j][len(matriz)-1-j] > matriz[j+1][len(matriz)-2-j]:
            aux = matriz[j][len(matriz)-1-j]
            matriz[j][len(matriz)-1-j] = matriz[j+1][len(matriz)-2-j]
            matriz[j + 1][len(matriz) - 2 - j] = aux

for fila in range (dimension):
    for columna in range(dimension):
        print(str(matriz[fila][columna]).rjust(5),end=" ")
    print()
