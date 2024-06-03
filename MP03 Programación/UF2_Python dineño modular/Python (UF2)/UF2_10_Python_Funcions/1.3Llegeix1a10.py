# 1.3) Función para leer un número entre 0 y 10
"""Creeu una funció “llegeix1a10” que s’encarregui de demanar a l’usuari que introdueixi pel teclat un nombre
entre 0 i 10. Fins que el nombre no està entre el 0 i el 10, continua demanat a l’usuari el número."""


def llegeix_1a10():
    numero = int(input("Introduce un número entre 0 y 10: "))
    while numero < 0 or numero > 10:
        numero = int(input("Número incorrecto. Introduce un número entre 0 y 10: "))
    return numero


numero_leido = llegeix_1a10()
print("Número leído:", numero_leido)