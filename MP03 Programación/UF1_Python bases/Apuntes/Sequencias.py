# MISMAS CARACTERISTICAS QUE LAS CADENAS:

lista = [2,3,"cadena1",3,3.5,True,3,["a","b",[333,444,555],"c"],"lalala",3]
# lista = []
cadena = "aeiou"
# lista[3] = "X" = [2, 3, 'cadena1', 'X', 3.5, True, 3, ['a', 'b', [333, 444, 555], 'c'], 'lalala', 3]
# lista.append("X") = [2, 3, 'cadena1', 3, 3.5, True, 3, ['a', 'b', [333, 444, 555], 'c'], 'lalala', 3, 'X']
# lista.insert(2,"X") = [2, 3, 'X', 'cadena1', 3, 3.5, True, 3, ['a', 'b', [333, 444, 555], 'c'], 'lalala', 3]
#lista.remove("X") = Te devuelve la cadena sin el elemento indicado, borra todos.
# #Para remover un elemento exacto, hay que saber su posicionamiento:
# print(lista[:10])
# print(lista[11:])
# lista = lista[:10] + lista[11:]
#=========================================================================================================
# lista1 = [1,2,3]
# lista2 = [4,5,6]
# lista3 = lista1 + lista2 == [1, 2, 3, 4, 5, 6]
# NO SE PUEDE RESTAR
# print(lista3)

#========================================================
# print(lista[7][2][2]) nos muestra 555
#=======================================================
# print(lista[7][1]) me da la b de la lista en psoicion 7
#=======================================================
# print(lista[1000]) = IndexError: list index out of range (acceder a algo que no existe)
# print(lista[8:2:-1])#Monta elementos al revés
# print(len(lista))

# lista = [34,54,234,34,65]
# lista = ["123","abc","9"]
# print(max(lista)) #Solo sirve con algunos valores
# print(min(lista)) #igual que max
# print("cadena11") in lista
#  print(lista.index(cadena24)) = error porque no se encuentra en ella
# print(lista.index(3,5)) #me muestra la posicion del 3 a partir de la posicion 5

#=========SIN RESOLVER======================================AÑADIMOS COUNT
# elemento = 3
# if elemento in lista:
#     posicion = 0
#     for i in range(lista.count(elemento)):
#
#         print(lista.index(elemento,posicion))
#         posicion = lista.index(elemento,posicion)+1
#
# else:
#     print("{} no esta en la lista".format(elemento))
#===========================================================
# print(lista.count(True))
