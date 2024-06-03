
def esLletra(caracter):
    if caracter.isalpha():
        return 1

    if not caracter.isalpha():
        return 0

caracter = input("Introduce cualquier carácter: ")
print("Valor: "+ str(esLletra(caracter)))

