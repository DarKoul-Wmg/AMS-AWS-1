
def generar_n_caracters(num,car):

    return car * num

car = input("Introduce un caracter: ")
num = int(input("Introduce un valor para multiplicar el caracter: "))

resultado = generar_n_caracters(num,car)

print(resultado)
