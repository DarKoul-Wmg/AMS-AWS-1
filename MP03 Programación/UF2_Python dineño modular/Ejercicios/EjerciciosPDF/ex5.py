def esDigit(caracter):
    if caracter.isdigit():
        return 1
    if not caracter.isdigit():
        return 0


caracter = input("Introduce cualquier carácter: ")

print("Valor: "+ str(esDigit(caracter)))