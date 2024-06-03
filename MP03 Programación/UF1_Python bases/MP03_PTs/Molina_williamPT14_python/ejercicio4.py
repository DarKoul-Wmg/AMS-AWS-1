import random

llistaAleatoris = []
llistaDistancies = []

for i in range(20):
    llistaAleatoris.append(random.randint(0,9))

max_dist = 0
repeticiones = random.randint(5, 10)
for i in range(repeticiones):
    distancies_proces = []

    for j in range(len(llistaAleatoris)):
        suma_distancias = 0
        for num in llistaAleatoris:
            suma_distancias += abs(i - num)
        distancies_proces.append(suma_distancias)

        if suma_distancias > max_dist:
            max_dist = suma_distancias

    for dist in distancies_proces:
        llistaDistancies.append(dist)


histograma = [0] * (max_dist + 1)
for i in range(len(histograma)):
    count = llistaDistancies.count(i)
    asteriscos = '*' * count
    print(f"{i} --> {count} {asteriscos}")
