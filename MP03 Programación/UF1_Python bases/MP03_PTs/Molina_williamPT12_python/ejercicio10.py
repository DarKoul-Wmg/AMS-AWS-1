cadena = input("Introduce algo")

contador_May = 0

for caracter in cadena:
    if caracter.isupper():
        contador_May += 1

print(contador_May)
