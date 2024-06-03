def lecturaInterval(min,max):
    num = int(input("Introduce un numero dentro del intervalo: "))
    while not num in range(min,max+1):
        num = int(input("Numero no válido, tiene que encontrarse entre el intervalo {} - {}: ".format(min,max)))
    else:
        return print("Numero Válido")

min = int(input("Introduce el valor mínimo del intervalo: "))
max = int(input("Introduce el valor máximo del intervalo: "))
lecturaInterval(min,max)