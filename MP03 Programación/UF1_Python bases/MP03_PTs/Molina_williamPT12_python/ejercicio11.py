cadena = input("Introduce algo con numeros")

contador_Num = 0

for caracter in cadena:
    if caracter.isdigit():
        contador_Num += 1

print(contador_Num)
