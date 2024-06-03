import random

cadena = input("Introduce una cadena de texto: ")

palabra_actual = ''
apariciones_palabras = {}


for caracter in cadena.lower():
    if caracter.isalnum():
        palabra_actual += caracter
    elif palabra_actual:
        apariciones_palabras[palabra_actual] = apariciones_palabras.get(palabra_actual, 0) + 1
        palabra_actual = ''

if palabra_actual:
    apariciones_palabras[palabra_actual] = apariciones_palabras.get(palabra_actual, 0) + 1

print(apariciones_palabras)




cadena_texto = input("Introduce una cadena de texto: ")
apariciones_caracteres = {}

for caracter in cadena_texto:
    apariciones_caracteres[caracter] = apariciones_caracteres.get(caracter, 0) + 1

print(apariciones_caracteres)


iteraciones = int(input("Introduce la cantidad de iteraciones para tirar dos dados: "))
apariciones_sumas = {}

for _ in range(iteraciones):
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    suma = dado1 + dado2
    apariciones_sumas[suma] = apariciones_sumas.get(suma, 0) + 1

print(apariciones_sumas)


cadena_texto = input("Introduce una cadena de texto: ")
apariciones_caracteres = {}

for caracter in cadena_texto:
    apariciones_caracteres[caracter] = apariciones_caracteres.get(caracter, 0) + 1

print(apariciones_caracteres)

