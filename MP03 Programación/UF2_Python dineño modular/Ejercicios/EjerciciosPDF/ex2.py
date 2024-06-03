
def calculaResidu(dividend,divisor):
    residuo = dividend % divisor
    return residuo


dividend = int(input("Introduce el dividendo: "))
divisor = int(input("Introduce el divisor: "))

print("Residuio: " + str(calculaResidu(dividend,divisor)))


