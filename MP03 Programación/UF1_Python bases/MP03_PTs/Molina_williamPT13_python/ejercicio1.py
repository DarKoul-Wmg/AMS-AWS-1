import math

lista = [2.3,5.6,7.2,5.0,3.0,2.1]
for element in lista:
    print(element)
print("___________________")

for element in lista[::-1]:
    print(element)
print("___________________")

lista[2] = 6
print(lista)
print("___________________")

nuevo_num = float(input("Introdueix un número: "))

lista[3] = nuevo_num
print(lista)

print("___________________")
for i in range(0,len(lista), 2):
    print(lista[i])

print("___________________")
for i in range(1,len(lista), 2):
    print(lista[i])

print("___________________")
