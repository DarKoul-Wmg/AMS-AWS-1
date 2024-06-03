#menu00= ("opc1","opc2","opc3","opc4")

def miPrimeraFuncion(argumento1,argumento2):
    print("Hola {},{}. QUe tal te va el dia".format(argumento1,argumento2))


# print("Antes de llamar a la función")
# miPrimeraFuncion("Matias","Carrizosa")
# print("Después de llamar a la función")
#
# print("Otra vez antes de llamar a la función")
# miPrimeraFuncion("ESter","Leon")
# print("Después de llamar a la función")

def division_entera(dividendo,divisor):
    cociente = dividendo//divisor
    resto = dividendo%divisor
    print("antes return")
    return cociente     #Después de un return nos saca de la función y no ejecuta codigo
    #Si return esta vacio, devuelve None.
    print("despues return")

resultado_division = division_entera(11,2)
print("El resultado es ",resultado_division)
print(type(resultado_division))