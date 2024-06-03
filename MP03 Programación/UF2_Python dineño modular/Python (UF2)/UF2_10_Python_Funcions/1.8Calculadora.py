# 1.8) Programa para realizar cálculos
"""Volem fer un programa per a fer càlculs. El programa mostra un petit menú i cada opció ens demanarà un o dos números per
a fer un càlcul determinat. Exemple:
Funcions: math.sqrt(num) y math.log(num)"""
import math


# No recursiva:
def menu_calculos():
    while True:
        print("\n" * 2 + "Menú de cálculos")
        print("1. Raíz cuadrada.")
        print("2. Logaritmo natural.")
        print("3. Salir.")

        opcion = input("\nSelecciona una opción.\n> ")

        if opcion == '1':
            numero = float(input("\nIntroduce un número para calcular su raíz cuadrada.\n> "))
            print("La raíz cuadrada de", numero, "es:", math.sqrt(numero))
        elif opcion == '2':
            numero = float(input("\nIntroduce un número para calcular su logaritmo natural\n> "))
            print("El logaritmo natural de", numero, "es:", math.log(numero))
        elif opcion == '3':
            print("Saliendo del programa.")
            break
        else:
            print("Opción no válida. Por favor, selecciona una opción válida.\n")


menu_calculos()


# Recursiva:
def menu_calculosRecursivo():
    print("\n" * 2 + "Menú de cálculos recursivo")
    print("1. Raíz cuadrada.")
    print("2. Logaritmo natural.")
    print("3. Salir.")

    opcion = input("\nSelecciona una opción.\n> ")

    if opcion == '1':
        numero = float(input("\nIntroduce un número para calcular su raíz cuadrada.\n> "))
        print("La raíz cuadrada de", numero, "es:", math.sqrt(numero))
        menu_calculosRecursivo()
    elif opcion == '2':
        numero = float(input("\nIntroduce un número para calcular su logaritmo natural\n> "))
        print("El logaritmo natural de", numero, "es:", math.log(numero))
        menu_calculosRecursivo()
    elif opcion == '3':
        print("Saliendo del programa.")
        # Termina la recursión:
        return
    else:
        print("Opción no válida. Por favor, selecciona una opción válida.\n")
        menu_calculosRecursivo()


menu_calculosRecursivo()
