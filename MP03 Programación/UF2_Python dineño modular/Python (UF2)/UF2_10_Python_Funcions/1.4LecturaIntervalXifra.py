# 1.4) Función para leer un número dentro de un intervalo
"""Creeu una funció “lecturaInterval” que faci una lectura d’una xifra dins d’un interval. A la funció li
passarem el valor mínim del rang, el valor màxim, i ens tornarà un valor llegit del teclat que estigui dins
d’aquest rang. Com a l’exercici anterior, fins que el nombre no estigui dins l’interval, la funció continuarà
demanat el nombre a l’usuari.       lecturaInterval(minim , maxim)"""


def lectura_intervalo(minimo, maximo):
    numero = int(input(f"Introduce un número entre {minimo} y {maximo}: "))
    while numero < minimo or numero > maximo:
        numero = int(input(f"Número incorrecto. Introduce un número entre {minimo} y {maximo}: "))
    return numero


numero_leido = lectura_intervalo(0, 10)
print("Número leído dentro del intervalo:", numero_leido)
