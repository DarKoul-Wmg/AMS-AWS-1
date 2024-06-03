tupla = (2,3,4.5,"pepe","juan",(9,8,7),[8,9])
# print(tupla[:3]) =(2, 3, 4)

# tupla es invariable: Se usa para datos estaticos
# tupla [1] = 'asf' = tupla [1] = 'asf' TypeError: 'tuple' object does not support item assignment


# lista en tupla se peude modificar:
# print(tupla) = (2, 3, 4.5, 'pepe', 'juan', (9, 8, 7), [8, 9])
# tupla[6][0]=1000
# print(tupla) = (2, 3, 4.5, 'pepe', 'juan', (9, 8, 7), [1000, 9])

#NO DEJAN DE SER SECUENCIAS:
# print("pepe" in tupla) = True
# print("pepeqw" in tupla) = False

#PARA IDENTIFICAR QUE SEA UNA TUPLA: tupla(5,) == SINO tupla(5) el codigo lo lee como int


#DESEMPAQUETAR: Para hacerlo tiene que tener el mismo numero de variables que elementos en tupla.
# tupla = ("44445555","Pepe")
# dni,nombre = tupla
# print("nombre =", nombre)
# print("dni = ",dni)

#ELIMINAR TUPLA: del(tupla), si luego la delcaras, te da error conforme no esta definida

# tupla1 = (1,2,3)
# tupla2 = (4,5,6)
#
# print(tupla1 > tupla2) #false
#
# tupla1 = (4,5,6,4,5)
#
# print(tupla1 > tupla2) #True


# for i in range (len(tupla)):
#     print(tupla[i])
# print("***************")
#
# for elemento in tupla:
#     print(elemento)
# resultado:2
# 3
# 4.5
# pepe
# juan
# (9, 8, 7)
# [8, 9]
# ***************
# 2
# 3
# 4.5
# pepe
# juan
# (9, 8, 7)
# # [8, 9]
#
# # #CREAR LISTAS CON TUPLA:
# # # (puede ser a la inversa)
# # # lista = list(tupla)
# # # print(lista) = [2, 3, 4.5, 'pepe', 'juan', (9, 8, 7), [8, 9]]
# #
# #  lista = [2, 3, 4.5, 'pepe', 'juan', (9, 8, 7), [8, 9]]
# #  tupla = tuple(lista)
# #  print(tupla)
#
# #INTERCAMBIO DE VARIABLES:
#
# # a = 10
# # b = 20
# #
# # aux = a #guardar valor de a en una variable auxiliar
# # a = b
# # b = aux
# #
# # print("a = {}, b = {}".format(a,b)) = a = 20, b = 10
#
# # =============================================================================================
#
# lista_alumnos = [("11111111A","Nombre1",3.4),("22222222B","Nombre2",2.7)]
#
# #dni     nombre      Nota
#
# # 1)Nuevo alumno (dni,nombre,nota)
# # 2)Mostrar notas
# # 3)Salir
#
# # option 2:
# #
# # DNI        NOMBRE               NOTA (Comprobar que es un float)
#
# # (LAS OPCIONES TIENEN QUE SER NUMERICAS, HAY QUE METER ELDIGITO EN ENTERO)
#
# lista=['T','R','W','A','G','M','Y','F','P','D','X','B','N','J','Z','S','Q','V','H','L','C','K','E']
#
# print(33333333%23)
# print(lista[33333333%23])
#
# dni_correcto = False
# while not dni_correcto:
#     dni = input("dame el dni")
#     if len(dni) != 9:
#         print("longitud incorrecta")
#     elif not dni[0:8].isdigit():
#         print("los primeros 8 caraceteres no son digitos")
#     elif not dni[8].isupper():
#         print("letra tiene que ser mayuscula")
#     elif dni[8]==lista[int(dni[0:8])%23]:
#         print("letra dni no es correcta")
#     else:
#         print("DNi correcto")
#         dni = dni.upper()
#         dni_correcto = True
# print("DNI Correcto: ",dni)
#
# #QUEDA COMPROBAR NOMBRE (PUEDE TENER ESPACIOS) Y NOTA CORRECTO
# #ORDENAR NOTAS DE MAYOR A MENOR
#
# DNI 10L + NOMBRE 20L + NOTA 7 R



#=====================================================================================
print("a".ljust(5, "+"))
nota = 7
notas = [7.34,6,10,9.3]
# print(str(nota).split(".")[0])
# print(str(nota).split(".")[1])
for nota in notas:
    if str(nota).count(".") == 1:
        str_nota = str(nota).split(".")[0].rjust(2,"+") +"."+str(nota).split(".")[1].ljust(3,"+")

    else:
        str_nota = str(nota).rjust(2,"+")+" ".ljust(4,"+")
    print(str_nota)