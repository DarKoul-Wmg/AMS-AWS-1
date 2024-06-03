# # Cadena = nombre1.nombre2.nombre3.nombre4. ... .nombre n
# #Pedir numero, del 1 al n(cualquiera).
# #Num 3, que te imprima el nombre 3
# #Num 5, que te imprima el nombre 5
# #Se tiene que encontrar los puntos que separan los nombres
#
# # Cadena = nombre1.nombre2.nombre3.nombre4. ... .nombre n
# #Inicio = 0   final = cadena.index(".")
# # luego hacer print cadena [inicio:final]
#
# #Para otro que no sea el primero:
#     #inicio = final + 1
#     #final = cadena.index(".", final + 1)
#     # utilizar .count(".") para los nombres
#
# nombres = "nombre1.nombre2.nombre3.nombre4.nombre5.nombre6"
# inicio = 0
# final = 0
# num = 2
# #for i in range(nombres.count(".")):
# for i in range(num):
#     if i == 0:
#         inicio = 0
#         final =nombres.index(".")
#     else:
#         inicio = final + 1
#         final = nombres.index(".", final + 1)
#     print("inicio = {}, final = {}".format(inicio,final))
#     print(nombres[inicio:final])
# =========================================================================

#Usuario para probar MODIFICAR RANKING
nombre_usuario = "jose"
puntos_usuario = 50
datos_rank = ["antonio:100"]

if len(datos_rank) == 0:
    datos_rank = nombre_usuario +":"+ str(puntos_usuario)+";"
else:
    for i in range(0,datos_rank):
        if ";" == 0:
            inicio = 0
            final = datos_rank.index(";")

        else:
            inicio = final + 1
            final = datos_rank.index(";", final +1)

        if int(datos_rank[inicio:final][datos_rank[inicio:final].index(":") +1:]) < puntos_usuario:
            datos_rank = datos_rank[:inicio] + nombre_usuario + ":" + str(puntos_usuario) + ";" + datos_rank[inicio:]

        if i == datos_rank.count(";") -1 and not int(datos_rank[inicio:final][datos_rank[inicio:final].index(":") +1:]) < puntos_usuario:
            datos_rank = datos_rank[:inicio] + nombre_usuario + ":" + str(puntos_usuario) + ";" + datos_rank[inicio:]


print(datos_rank)
