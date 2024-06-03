#Algoritmo para generar una matriz de 3x3 aleatoria
import random

dimension = 4
matriz =[]
for fila in range(dimension):
    matriz.append([])
    for columna in range(dimension):
        matriz[fila].append(random.randint(1,100))
# print(matriz)
#Representar matriz con su forma;

for fila in range(dimension):
    for columna in range(dimension):
        print(str(matriz[fila][columna]).rjust(5),end=" ")
    print()#Print vacio para hacer el salto de linea

#======================================================
#MOSTRAR UNA FILA EN CONCRETO
# print("******************************")
# num = 1#fila
# for columna in range(len(matriz)):
#     print(str(matriz[num][columna]).rjust(5),end=" ")
# print()
#
# #=====================================================
# #ORDENAR FILA RESULTANTE CON BURBUJA
# print('*************************')
#
# print("\nOrdenamos la fila {}".format(num))
# for pasada in range(len(matriz)-1):
#     for j in range(len(matriz)-1-pasada):
#         if matriz[num][j] > matriz[num][j+1]:
#             aux = matriz[num][j]
#             matriz[num][j] = matriz[num][j+1]
#             matriz[num][j+1] = aux
# for columna in range(len(matriz)):
#     print(str(matriz[num][columna]).rjust(5),end=" ")
#
# print("\n*************Ordenamos la matriz******************************\n")
#
# #ORDENAR CADA FILA DE LA MATRIZ "toda": AÑADIMOS UN TERCER FOR
# # Y CAMBIAMOS NUM POR FILA PARA ITERAR EN LAS TRES FILAS:
# for fila in range(len(matriz)):
#     for pasada in range(len(matriz)-1):
#         for j in range(len(matriz)-1-pasada):
#             if matriz[fila][j] > matriz[fila][j+1]:
#                 aux = matriz[fila][j]
#                 matriz[fila][j] = matriz[fila][j+1]
#                 matriz[fila][j+1] = aux
#
# for fila in range(dimension):
#     for columna in range(dimension):
#         print(str(matriz[fila][columna]).rjust(5),end=" ")
#     print()
print("*************-SACAR COLUMNA-************** ")
#SACAMOS COLUMNA:

num = 2#columna
for fila in range(len(matriz)):
    print(str(matriz[fila][num]).rjust(5),end=" ")
print()

print("\n***************-ORDENAR COLUMNA SACADA-*************")
#ORDENAMOS COLUMNA:

for pasada in range(len(matriz)-1):
    for j in range(len(matriz)-1-pasada):
        if matriz[j][num] > matriz[j+1][num]:
            aux = matriz[j][num]
            matriz[j][num] = matriz[j+1][num]
            matriz[j+1][num] = aux
for fila in range(len(matriz)):
    print(str(matriz[fila][num]).rjust(5),end=" ")


print("\n**************-SACAR COLUMNA AL REVÉS-*********")
columna = 1
for fila in range(len(matriz)-1,-1,-1):
    print(str(matriz[fila][columna]).rjust(5),end=" ")

print("\n**************-ORDENAR COLUMNA AL REVÉS-*********")
columna = 1
for pasada in range(len(matriz)-1):
    for j in range(len(matriz)-1-pasada):
        if matriz[j][num] > matriz[j+1][num]:
            aux = matriz[j][num]
            matriz[j][num] = matriz[j+1][num]
            matriz[j+1][num] = aux
for fila in range(len(matriz)-1,-1,-1):
    print(str(matriz[fila][num]).rjust(5),end=" ")


print("\n**************-ORDENA TODAS LAS COLUMNAS AL REVÉS-*********")
columna = 1 #es lo mismo que num
for columna in range(len(matriz)):
    for pasada in range(len(matriz)-1):
        for j in range(len(matriz)-1-pasada):
            if matriz[j][columna] < matriz[j+1][columna]:
                aux = matriz[j][columna]
                matriz[j][columna] = matriz[j+1][columna]
                matriz[j+1][columna] = aux

for fila in range(dimension):
    for columna in range(dimension):
        print(str(matriz[fila][columna]).rjust(5),end=" ")
    print()


#EJEMPLO ORDENAR MATRIZ DE 4
print("\n *****************PRUEBA DE ORDENAR columna (al revés)******************")
columna = 1
for pasada in range(len(matriz) - 1):
    for j in range(len(matriz) - 1, pasada, -1):
        if matriz[j][columna] > matriz[j - 1][columna]:
            aux = matriz[j][columna]
            matriz[j][columna] = matriz[j-1][columna]
            matriz[j-1][columna] = aux

for fila in range(len(matriz) - 1, -1, -1):
    print(str(matriz[fila][num]).rjust(5), end=" ")
print()

print("\n *****************PRUEBA DE ORDENAR TODAS LAS COLUMNAS AL REVÉS******************")

columna = 1
for columna in range(len(matriz)):
    for pasada in range(len(matriz)-1):
        for j in range(len(matriz)-1, pasada, -1):
            # print(f"Pasada{pasada}, j={j},j+1 ={j-1}")
            if matriz[j][columna] > matriz[j-1][columna]:
                    aux = matriz[j][columna]
                    matriz[j][columna] = matriz[j-1][columna]
                    matriz[j-1][columna] = aux

for fila in range (dimension):
    for columna in range(dimension):
        print(str(matriz[fila][columna]).rjust(5),end=" ")
    print()