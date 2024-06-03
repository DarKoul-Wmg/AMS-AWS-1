num = int(input("Introdueix un número per trobar els seus divisors: "))

divisores = [] #almacenar divisores
y = 1
while y <= num:
    if num % y == 0:
        divisores.append(y) #Se agregan los resultados de Y a la lista

        #print(f"Els divisors de {num} són: {divisores}")

    y = y + 1
if divisores:
    result_div = divisores[-1] #-1 para obtener ultimo resultado
    print(f"Els divisors de {num} són: {divisores}")
