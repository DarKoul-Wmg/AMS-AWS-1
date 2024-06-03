#ficherito = open("datos.txt","a+")
# print(type(ficherito))
# print(ficherito)

#ficherito.write("lalala")
#contenido = ficherito.read()
#print(contenido)
# print(type(contenido))

# r modo lectura
# w modo escritura (elimina el contenido)
# Si lo abres de un modo, solo puede usarse de ese modo

# a modo para añadir contenido a un fichero, si no existe lo crea
# r+ Puedes escribir, pero empieza desde el principio y substituye t-odo lo que pilla:
## ficherito.write("lalala")
## contenido = ficherito.read()
## print(contenido)

# w+ Si se abre con esto y le ordenas escribir algo (lalala), te borra t-odo y lee despues del texto añadido

# a+ Añade el texto al final del puntero (detras del ultimo caracter)

###########Compatibiliza programas entre windows y linux (problema de / o \)
#import os
#print(os.path.join("data","arxiu.txt"))
################


# ficherito = open("datos.txt","r")
# contenido = ficherito.read(3)
# print(contenido)
# contenido = ficherito.read(4)#  continua desde donde lo ha dejado el cursor
# print(contenido)
# #a12
# #34
# #l

#conteido = ficherito.readlines() #devuelve una lista con todas las lineas del fichero
#print(conteido)
#conteido = ficherito.readline()
#print(conteido)


# ficherito.close()
# print(ficherito.closed)
# .closed para saber que la conexión se ha cerrado, close para cerrarlo

# Se puede iterar:
# for linea in ficherito:
#     print("linea = ", linea)


#============================= Escribir ==============================

ficherito = open("datos.txt","r")
#
# #ficherito.write("gffdgdgg")
# lista = ["a\n","b\n","c"]
# ficherito.writelines(lista)

# #Abre y cierra fichero de forma automatica
# with open("datos.txt","r") as f:
#     print(f.read())
# print(f.closed)

print(ficherito.read(2))
print(ficherito.tell()) # Dice la posicion donde estas

print(ficherito.read(7))
print(ficherito.tell())

print(ficherito.seek(4))
print(ficherito.tell())

print(ficherito.mode)
print(ficherito.name)
print(ficherito.encoding)
