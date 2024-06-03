numT = int(input("Quants números vols introduir? "))
#=======================================================================================================================
# max: Esta variable se inicializa con el valor (-inf) = -infinito.
# Asegurarse de que cualquier número ingresado por el usuario se considere mayor que el valor inicial.
# De esta manera, cuando se compara el primer número ingresado por el usuario, siempre será mayor hasta que se encuentre
# un número mayor durante el bucle, se actualizará esta variable.

# min: Esta variable se inicializa con el valor (inf) = infinito.
# Asegurarse de que cualquier número ingresado sea considerado menor que el valor inicial.
# De esta manera, cuando se compara el primer número ingresado por el usuario, siempre será menor que infinito,
# y si se encuentra un número menor durante el bucle, se actualizará esta variable.
#=======================================================================================================================
max = float("-inf")
min = float("inf")
suma = 0

#Numeros a introduir i procésde càlcul:
for i in range(numT):
    num = float(input("Introdueix els números: "))
    suma += num
    if num > max:
        max = num

    if num < min:
        min = num

mitjana = float(suma / numT)
print("El número més gran es: " + str(max))
print("El número més petit es: " + str(min))
print("La mitjana del números introduits és: " + str(mitjana))
