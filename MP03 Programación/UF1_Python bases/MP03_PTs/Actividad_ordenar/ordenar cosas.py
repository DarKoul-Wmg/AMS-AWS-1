import random

# lista_aleatoria = []
# for i in range(6):
#     lista_aleatoria.append(random.randrange(100))
# print(lista_aleatoria)

#METODO 1 (se empieza desde el primer digito)

# for pasada in range(len(lista_aleatoria)-1):
#     for j in range(pasada+1,len(lista_aleatoria)):
#         # print("pasada = {}, j ={}".format(pasada,j))
#         if lista_aleatoria[pasada] > lista_aleatoria[j]:
#             aux = lista_aleatoria[pasada]
#             lista_aleatoria[pasada] = lista_aleatoria[j]
#             lista_aleatoria[j] = aux
#
# print(lista_aleatoria)
#
# #METODO 2:Burbuja (se empieza desde 0)
#
# for pasada in range(len(lista_aleatoria)-1):
#     for j in range(len(lista_aleatoria)-1-pasada):
#
#         # print("pasada = {}, j ={}, j+1 = {}".format(pasada,j,j+1))
#         if lista_aleatoria[j] > lista_aleatoria[j+1]:
#             aux = lista_aleatoria[j]
#             lista_aleatoria[j] = lista_aleatoria[j+1]
#             lista_aleatoria[j+1] = aux
#
# print(lista_aleatoria)


#========================ORDENAR DICCIONARIO=================================
diccionario = {"codigo9":{"nombre":"pepe","dni":"11111111H"},
               "codigo5":{"nombre":"juan","dni":"99999999H"},
               "codigo3":{"nombre":"isa","dni":"33333333H"},
               "codigo7":{"nombre":"anabel","dni":"83838383H"}}


#ORDEN POR CODIGOS
for code in diccionario:
    print(code," - ",diccionario[code])

lista_codes=list(diccionario.keys())
print(lista_codes)

for pasada in range(len(lista_codes)-1):
     for j in range(len(lista_codes)-1-pasada):


         if lista_codes[j] > lista_codes[j+1]:
             aux = lista_codes[j]
             lista_codes[j] = lista_codes[j+1]
             lista_codes[j+1] = aux

for code in lista_codes:
    print(code," - ",diccionario[code])

print("======================================")
#ORDENAR POR DNI (para ordenar nombres de la misma forma pero cambiando dni por nombre)
lista_codes=list(diccionario.keys())
print(lista_codes)

for pasada in range(len(lista_codes)-1):
     for j in range(len(lista_codes)-1-pasada):
         if diccionario[lista_codes[j]]["dni"] > diccionario[lista_codes[j+1]]["dni"]:
             aux = lista_codes[j]
             lista_codes[j] = lista_codes[j + 1]
             lista_codes[j + 1] = aux

for code in lista_codes:
    print(code," - ",diccionario[code])



