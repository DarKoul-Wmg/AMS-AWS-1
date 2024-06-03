def division(dividendo,divisor):
    resultado = 0
    if dividendo <= 0:
        return resultado

    else:
        dividendo = dividendo - divisor
        resultado +=1
        return resultado + division(dividendo,divisor)





divisor = 3
dividendo = 18
print("Resultado división: " + str(division(dividendo,divisor)))
