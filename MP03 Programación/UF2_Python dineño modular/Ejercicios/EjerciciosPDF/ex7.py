def aMajuscula(caracter):
    if caracter.isalpha():
        return caracter.upper()
    if not caracter.isalpha():
        return caracter

caracter = input("Introduce cualquier carácter: ")
print("Caracter: "+ aMajuscula(caracter))