# print("a")
#
# diccionario = {"clave1":"valor1","clave2":"valor2","clave3":"valor3"}
#
# #NO PUEDEN TENER LISTAS, SOLO VALORES INMUTABLES:
# # diccionario = {1:"valor1","clave2":"valor2",(2,3,4,[1,2]):"valor3"} = TypeError: unhashable type: 'list'
#
# #NOS DA EL VALOR CORRESPONDIENTE
# # print(diccionario["clave2"]) = valor2
#
# diccionario = {1:"valor1","clave2":"valor2",(2,3,4):"valor3"}
#
# # print(diccionario.get("claveN")) = None #EVITAMOS QUE EL PROGRAMA PETE
#
# # print(diccionario.get("claveN",10)) = 10 COMO NO EXISTE CLAVEN, SI AÑADIMOS ALGO DETRAS DE LA COMA DA UN VALOR POR DEFECTO.
#
# # AÑADIR ELEMENTOS EN DICCIONARIO
# # diccionario = {}
# #
# # # diccionario["clave4"] = "valor4"
# # # print(diccionario) = {'clave4': 'valor4'}
# #
# # diccionario["clave2"] = "valor4"
# # print(diccionario)
# #
# # #BORRAR COSAS EN ELDICCIONARIO:
# # del(diccionario["clave2"])
# # print(diccionario)
#
# #RECORRER DICCIONARIO:
#
# # for clave in diccionario:
# #     print(clave)
# #     print(diccionario[clave]) =\
# # 1
# # valor1
# # clave2
# # valor2
# # (2, 3, 4)
# # valor3
#
# # print("clave2" in diccionario) = True
# # print(len(diccionario)) = 3
#
#
# # diccionario.clear() limpia diccionario
# # d1 = diccionario.copy() #Copia el diccionario
# # print(d1)
# # d1[1] =['XXX']
# # print(d1)  {1: ['XXX'], 'clave2': 'valor2', (2, 3, 4): 'valor3'}
# # print(diccionario) {1: 'valor1', 'clave2': 'valor2', (2, 3, 4): 'valor3'}
#
# # si d1 = diccionario, los dos print salen iguales por los apuntadores
#
# diccionario1 = {"clave1":"valor1","clave2":"valor2","clave3":"valor3"}
# diccionario2 = {1:"valor1","clave2":"valor2",(2,3,4):"valor3"}

# diccionario2.update(diccionario1)
# print(diccionario2) #={1: 'valor1', 'clave2': 'valor2', (2, 3, 4): 'valor3', 'clave1': 'valor1', 'clave3': 'valor3'}


#SACAMOS CLAVES DE DICCIONARIO Y SE METEN EN UNA LISTA
# lista = list(diccionario2.keys())
# print(lista)
# for elemento in lista:
#     print(elemento)
#
#
# #TAMBIEN FUNCIONA CON VALORES DEL DICCIONARIO:
# lista = list(diccionario2.values())
# print(lista)
# for elemento in lista:
#     print(elemento)

# #MUESTRA TODO:
# lista = list(diccionario2.items())
# print(lista)
# for elemento in lista:
#     print(elemento)

# print("**********")
# for clave,valor in diccionario2.items():
#     print(clave," tiene asociado el valor ",valor)
# 1  tiene asociado el valor  valor1
# clave2  tiene asociado el valor  valor2
# (2, 3, 4)  tiene asociado el valor  valor3



# diccionario = {"clave1":"valor1","clave2":[10,20,30]}
# diccionario["clave3"]["c3"] = []
# diccionario["clave3"]["c3"].append({})
# diccionario["clave3"]["c3"].append(1000)


#USANDO DDATOS DEL EJERCICIO:
#desde 'usuarios'
usuario1 = {"nombre":"Pedro Javier Morales",  "direccion": "Flores 36 8º 2º", "tfn":["+0034345345345"],"compras":[1234,423,23]}
usuario2 = {"nombre":"Maite Lopez Miravet", "direccion":"Balames 31 1º 2º","tfn":["+0034234234235","+0034239999235"],"compras":[12344]}
usuario3 = {"nombre":"Marta Garcia Suarez",  "direccion":"Valencia 21 3º 1º","tfn": ["+0075766576575"],"compras":[34,423,23,6]}
usuario3 = {"nombre":"Osorio Lopez Cardenales",  "direccion":"aribau 21 3º 1º","tfn":[],"compras":[34,423,23,6]}
usuarios = {"47474747X":usuario1,"24536425T":usuario2,"76767676H":usuario3}

# print(usuarios["76767676H"]["direccion"]) = Valencia 21 3º 1º
print(usuarios["76767676H"]["tfn"].append('666666666'))
# print(usuarios["76767676H"]["tfn"][1]) = 666666666

# suma = 0
# for i in range(len(usuarios["76767676H"]["compras"])):
#     suma += usuarios["76767676H"]["compras"][i]
# print("suma = ",suma)
#
# dni = '55555555M'
# nombre = "Frasquito"
# direccion = "Calle santander 24"
# telefonos = [222333333,444444444]
# compras = []
#
# nuevo_usuario = {"nombre":nombre,"direccion":direccion, "tfn":telefonos,"compras":[]}
# print(nuevo_usuario)
#
# usuarios[dni] = nuevo_usuario
# print(usuarios)
# usuarios[dni]["compras"].append(1000)
# print(usuarios)

#MUESTRA TODA LA INFORMACION DE TELEFONOS DE GOLPE

# for clave in usuarios:
#     print(usuarios[clave]['tfn'])
#
# #MUESTRA TTODOS LOS TELEFONOS DE UNO EN UNO
#
# for clave in usuarios:
#     print(usuarios[clave]['nombre'])
#     for i in range(len(usuarios[clave]["tfn"])):
#         print(usuarios[clave]['tfn'][i])

datos = ""
for clave in usuarios:
    # print(usuarios[clave]['nombre'])
    datos += usuarios[clave]['nombre'].ljust(50)
    if len(usuarios[clave]["tfn"]) > 0:
        for i in range(len(usuarios[clave]["tfn"])):
            # print(usuarios[clave]['tfn'][i])
            if i ==0:
                datos += usuarios[clave]["tfn"][i].rjust(15)+'\n'
            else:
                datos += " ".ljust(50)+usuarios[clave]["tfn"][i].rjust(15) + '\n'
    else:
        datos += " ".rjust(15)+ "\n"
print(datos)