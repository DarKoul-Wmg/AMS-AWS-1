import random


def adivina_el_numero():
    numero_secreto = random.randint(1, 1000)
    intentos = 0

    print("Benvingut al joc 'Endevina el número'!\n")
    print("Tinc un número entre 1 i 1000. Pots endevinar quin és?")

    while True:
        intento = int(input("\nIntrodueix el teu intent.\n> "))

        intentos += 1

        if intento < numero_secreto:
            print("El número secret és més gran. Torna a intentar.\n")
        elif intento > numero_secreto:
            print("El número secret és més petit. Torna a intentar.\n")
        else:
            print(f"\nFelicitats! Has endevinat el número en {intentos} intents.")
            break

# Ejecutar el juego
adivina_el_numero()
