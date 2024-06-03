import random

llistaAleatoris = []
comptadorAleatoris = [0]*10
# print(comptadorAleatoris)
for i in range(20):
    llistaAleatoris.append(random.randint(0,9))

print(llistaAleatoris)

repeticions = random.randint(5,10)

for i in range(repeticions):
    for num in llistaAleatoris:
        comptadorAleatoris[num] +=1

print(comptadorAleatoris)
# Crear el histograma
for i in range(len(comptadorAleatoris)):
    count = comptadorAleatoris[i]
    asteriscos = '*' * count
    print(f"{i} --> {count} {asteriscos}")
