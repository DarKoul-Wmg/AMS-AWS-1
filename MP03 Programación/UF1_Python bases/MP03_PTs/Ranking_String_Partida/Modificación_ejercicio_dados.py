import random

usuario = ""
puntuacion_usuario = 0
puntuacion_maquina = 0
partidas_jugadas = 0
ranking = []

while True:
    print("\n--- Juego de Dados ---")
    print("1. Jugar partida")
    print("2. Crear usuario")
    print("3. Mostrar ranking")
    print("4. Salir")
    opcion = input("Selecciona una opción: ")

    if opcion == "1":
        if usuario == "":
            print("Debes crear un usuario primero (opción 2).")
        else:
            print("\n¡Comienza la partida, ", usuario, "!\n")
            input("Presiona Enter para iniciar la partida...")

            puntuacion_partida = 0

            for i in range(50):
                input(f"Turno {i + 1}: Presiona Enter para lanzar los dados...")
                turno_usuario = random.randint(1, 6)
                turno_maquina = random.randint(1, 6)

                suma_dados = turno_usuario + turno_maquina

                if suma_dados % 2 == 0:
                    puntuacion_usuario += turno_usuario if turno_usuario > turno_maquina \
                        else turno_maquina
                else:
                    puntuacion_usuario -= turno_usuario if turno_usuario < turno_maquina \
                        else turno_maquina

                puntuacion_maquina += turno_usuario if turno_usuario > turno_maquina \
                    else turno_maquina

                print(f"Turno {i + 1}: {usuario} obtiene {turno_usuario} y la máquina obtiene {turno_maquina}\n")

                puntuacion_partida += turno_usuario if turno_usuario > turno_maquina \
                    else turno_maquina  # Sumar la puntuación de la partida actual

            if puntuacion_usuario > puntuacion_maquina:
                print("\n¡", usuario, " ha ganado la partida con", puntuacion_usuario, " puntos!")
            elif puntuacion_maquina > puntuacion_usuario:
                print("\nLa máquina ha ganado la partida con", puntuacion_maquina, "puntos.")
            else:
                print("\n¡Ha habido un empate!")

            # Agregar el usuario y su puntuación a la lista de ranking
            ranking.append((usuario, puntuacion_usuario))

            # Reiniciar las puntuaciones para la próxima partida
            puntuacion_usuario = 0
            puntuacion_maquina = 0
            partidas_jugadas += 1

    elif opcion == "2":
        usuario = input("Introduce tu nombre de usuario: ")
        print("Bienvenido,", usuario, "!")

    elif opcion == "3":
        cadena = "RANKING".center(30," ") + "\n" + "NAME".ljust(20) + "POINTS".rjust(10) + "\n" + "-"*30
        print(cadena)

        for recorrido in range(1, len(ranking)):
            for posicion in range(len(ranking) - recorrido):
                if ranking[posicion][1] < ranking[posicion + 1][1]:
                    ranking[posicion], ranking[posicion + 1] = ranking[posicion + 1], ranking[posicion]

        for nombre, puntos in ranking:
            nombre = nombre.ljust(20)
            puntos = str(puntos).rjust(10)
            print(nombre, puntos)
        # for i in range(ranking.count(";")):
        #     if i == 0:
        #         inicionom = 0
        #         finalnom = ranking.index(":")
        #         iniciopunt = ranking.index(":") + 1
        #         finalpunt = ranking.index(";")
        #
        #     else:
        #         inicionom = ranking.index(";", finalnom) + 1
        #         finalnom = ranking.index(":", finalnom + 1)
        #         iniciopunt = ranking.index(":", finalpunt) + 1
        #         finalpunt = ranking.index(";", finalpunt + 1)
        #
        # for recorrido in range(1, len(ranking)):
        #     for posicion in range(len(ranking) - recorrido):
        #         if ranking[posicion] < ranking[posicion + 1]:
        #            ranking[posicion], ranking[posicion + 1] = ranking[posicion + 1], ranking[posicion]
        #
        # for nombre, puntos in ranking:
        #     print(nombre.ljust(20), str(puntos).rjust(10))

        print("-"*30)
    elif opcion == "4":
        print("¡Gracias por jugar!")
        break

    else:
        print("Opción no válida. Inténtalo de nuevo.")

