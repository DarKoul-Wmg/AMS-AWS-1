diccionario = {"clave1":[1,"valor3",7]}

clave = input("Introduce una clave del diccioario:\n")
valor = input("Introduce el valor de la clave:\n")

if len(diccionario[clave]) > 1:
    print(diccionario[clave])
