import math

def suma(num1,num2):
    sum = num1 + num2
    return print("Suma de los dos numeros: "+ str(sum))

def arrel(num):
    return print("Raíz cuadrada del numero es: "+ str(math.sqrt(num)))

def logaritme(num):
    return print("Logaritmo del numero es: "+ str(math.log(num)))

def ajuda():
    return print("Ajuda...")

opcio = 'x'
while(opcio!='T'):
    print("====================")
    print("Pren S per a SUMAR")
    print("Pren R per a ARREL QUADRADA")
    print("Pren L per a LOGARITME")
    print("Pren A per a AJUDA")
    print("Pren T per a TERMINAR")
    opcio = input()
    if opcio == 'S':
        num1 = int(input("Introduce un numero: "))
        num2 = int(input("Introdcue otro num: "))
        suma(num1,num2)

    if opcio == 'R':
        num = int(input("Introduce un numero: "))
        arrel(num)

    if opcio == 'L':
        num = int(input("Introduce un numero: "))
        logaritme(num)

    if opcio == 'A':
        ajuda()
