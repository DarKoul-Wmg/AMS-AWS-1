# Ejercicio 8
"""8. Escriu un programa que tingui una funció que demani dos anys i retorni quants anys de traspàs hi ha entre les dos
    dates (inclosos els dos anys):
    - Comptador de anys de traspàs
    - Escriu un any: 2000
    - Escriu altre any posterior a 2000: 1999
    - 1999 no es major que 2000. Torna de nou: 2013
    - De 2000 a 2013 hi ha 14 anys, 4 d’ells de traspàs."""


def contar_anys_de_traspas(any1, any2):
    if any1 > any2:
        # Asegurar que any1 <= any2:
        any1, any2 = any2, any1
    anys_traspas = 0
    for any in range(any1, any2 + 1):
        if any % 4 == 0 and (any % 100 != 0 or any % 400 == 0):
            anys_traspas += 1
    return anys_traspas


any1 = int(input("Escribe un año\n> "))
any2 = int(input("Escribe otro año posterior al primero.\n> "))
while any2 <= any1:
    print(any2, "no es mayor que", any1, end="" + ". Inténtalo de nuevo.")
    any2 = int(input("\n\nEscribe otro año posterior al primero.\n> "))
num_anys_traspas = contar_anys_de_traspas(any1, any2)
print(f"De {any1} a {any2} hay {any2 - any1} años, {num_anys_traspas} de ellos son años bisiestos.")
