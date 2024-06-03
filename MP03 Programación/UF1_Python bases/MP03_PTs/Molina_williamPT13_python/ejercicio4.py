import math
lista = [1,2,3,4,5,6]

suma = 0
for num in range(len(lista)):
    suma += lista[num]

media = suma / len(lista)
print("Suma", suma)
print("Mitjana", media)

print("Factorials:")
for num in lista:
    factorial_num = 1
    for i in range(1, num + 1):
        factorial_num *= i
    print(f"Factorial de {num}: {factorial_num}")
