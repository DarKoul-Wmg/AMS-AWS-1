# —————————————————————————————————————————————————————————————————————————————————————————————————————————— 1r EXEMPLE.
try:
    num = int(input("—" * 53 + "\n|  Diguem un número i et diré el doble! :)\n|  > "))
except:
    print("|  Això no és un número! :(")
else:
    print(f"|  El doble de {num} és {num * 2}. \n" + "—" * 53)
finally:
    print("|  Programa terminat! Gràcies per utilitzar-lo. :)  |\n" + "—" * 53)

# —————————————————————————————————————————————————————————————————————————————————————————————————————————— 2n EXEMPLE.
try:
    num = int(input("\n\n\n" + "—" * 53 + "\n|  Diguem un número i et diré 10 entre aquell número.\n|  > "))
    res = 10 / num
except ZeroDivisionError:
    print("—" * 53 + "\nNo es pot dividir entre 0.")
except Exception:
    print("|  Això no és un número! :(")
else:
    print(f"|  El doble de {num} és {num * 2}.")
finally:
    print("—" * 53 + "\n|  Programa terminat! Gràcies per utilitzar-lo. :)  |\n" + "—" * 53)

# —————————————————————————————————————————————————————————————————————————————————————————————————————————— 3r EXEMPLE.
from moduloperaciones import sumar, multiplicar
a = int(input("—" * 53 + "\n|  Diguem el primer número.\n|  > "))
b = int(input("|  Diguem el segon número.\n|  > "))

print(f"|  La suma de {a} y {b} és {sumar (a, b)}.")
print(f"|  La suma de {a} y {b} és {multiplicar (a, b)}.\n" + "—" * 53)

"""
————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
————————————————————————————————————— COM IMPORTAR RANDOM DE DOS MANERES DIFERENTS —————————————————————————————————————
————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
                                        · PRIMERA MANERA:
                                                import random
                                                n = random.randint(1, 6)
                                        ——————————————————————————————————
                                        · SEGONA MANERA:    
                                                from random import randint
                                                n = randint(1, 6)
————————————————————————————————————————————————————————————————————————————————————————————————————————————————————————
"""
