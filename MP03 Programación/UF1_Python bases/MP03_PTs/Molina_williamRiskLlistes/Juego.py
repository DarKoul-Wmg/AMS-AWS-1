import random
lista_jugadores = [["Juan",[],1], ["Rakel",[],1],["Raul",[],1],["Maria Isabel",[],1], ["Constantina",[],1], ["Jose Antonio",[],1]]

print("**********The Greatest Game In The World**********\n")
print("1) Show ranking")
print("2) Find player")
print("3) Select players")
print("4) Play")
print("5) Exit")


while True:
    #VERIFICAR PUNTUACION JUGADORES:
    for i in lista_jugadores:
        if i[2] <= 0:
            print(f"El jugador {i[0]} queda eliminado")
            lista_jugadores.remove(i)

    opcion = input("=>")
    if opcion.isdigit():
        opcion = int(opcion)

#RANKING
        if opcion == 1:
            cabecera = "RANKING".center(30,"'") + "\n" + "NAME".ljust(20) + "POINTS".rjust(10) + "\n" + "="*30
            print(cabecera)

            for recorrido in range(len(lista_jugadores)-1):
                for posicion in range(len(lista_jugadores) - recorrido - 1):
                    if lista_jugadores[posicion][2] < lista_jugadores[posicion + 1][2]:
                        lista_jugadores[posicion], lista_jugadores[posicion + 1] = lista_jugadores[posicion + 1], lista_jugadores[posicion]

            for jugador in lista_jugadores:
                nombreR = jugador[0].ljust(20)
                puntosR = str(jugador[2]).rjust(9)
                print(nombreR, puntosR)


#BUSCAR JUGADOR
        elif opcion == 2:

            nombre_buscado = input("Ingresa el nombre del jugador: ")
            resultados_busqueda = []

            for jugador in lista_jugadores:
                if nombre_buscado.lower() in jugador[0].lower():
                    resultados_busqueda.append(jugador)

            for recorrido in range(len(resultados_busqueda)-1):
                for posicion in range(len(resultados_busqueda) - recorrido -1):
                    if resultados_busqueda[posicion][2] < resultados_busqueda[posicion + 1][2]:
                         resultados_busqueda[posicion], resultados_busqueda[posicion + 1] = resultados_busqueda[posicion + 1], resultados_busqueda[posicion]

                for jugador in resultados_busqueda:
                    print(f"Jugador: {jugador[0]}, Puntuación: {jugador[2]}")
            else:
                print("Jugador no encontrado.")

#SELECCIONAR JUGADORES
        elif opcion == 3:
            player1 = lista_jugadores[random.randint(0, len(lista_jugadores) -1)]
            player2 = lista_jugadores[random.randint(0, len(lista_jugadores) -1)]
            while player1 == player2:
                player2 = random.choice(lista_jugadores)

            lista = [player1, player2]

            print (f"El primer jugador es: {lista[0][0]} con {lista[0][2]} puntos")
            print (f"El segundo jugador es: {lista[1][0]} con {lista[1][2]} puntos")

            for jugador in lista: #QUITAR JUGADORES DE LISTA principal
                if jugador in lista_jugadores:
                    lista_jugadores.remove(jugador)

#PARTIDA
        elif opcion == 4:
            if len(lista) != 2:
                print("Tienes que seleccionar jugadores antes de jugar!!!")

            else:
                turno = random.randint(0,1)
                turno_atacante = lista[turno%2] #0 es el jugador atacante
                turno_defensor = lista[(turno +1)%2] #1 es el jugador defensor
                print("El jugador atacante es:",  turno_atacante[0])
                print("El jugador defensor es:",  turno_defensor[0])
        #DADOS ATAQUE
                for i in range(4):
                    dado = random.randint(1, 6)
                    if i == 0:
                        turno_atacante[1].append(dado)
                    for j in range(len(turno_atacante[1])):

                        if dado > turno_atacante[1][j]:
                            turno_atacante[1].insert(j, dado)
                            break
                        if j == len(turno_atacante[1])-1 and dado <= turno_atacante[1][j]:
                            turno_atacante[1].append(dado)
                            break
        #DADOS DEFENSA
                for i in range(2):
                    dado = random.randint(1, 6)
                    if i == 0:
                        turno_defensor[1].append(dado)
                    for j in range(len(turno_defensor[1])):

                        if dado > turno_defensor[1][j]:
                            turno_defensor[1].insert(j, dado)
                            break
                        if j == len(turno_defensor[1]) - 1 and dado <= turno_defensor[1][j]:
                            turno_defensor[1].append(dado)
                            break
                print("Dados de {}:{}\nDados de {}:{}".format(turno_atacante[0],turno_atacante[1],turno_defensor[0], turno_defensor[1]))

                for i in range(len(turno_defensor[1])):

                #SI DADO ATK = DADO DEF O DADO DEF MAS GRANDE QUE DADO ATK:
                    if turno_atacante[1][i] == turno_defensor[1][i] or turno_atacante[1][i] < turno_defensor[1][i]:
                        turno_atacante[2] -= 1
                        turno_defensor[2] += 1


                #SI DADO ATK MAS GRANDE QUE DADO DEF:
                    elif turno_atacante[1][i] > turno_defensor[1][i]:
                        turno_atacante[2] += 1
                        turno_defensor[2] -= 1

                resultadoAtk = lista[0][0]+": "+str(lista[0][2])
                resultadoDef = lista[1][0]+": "+str(lista[1][2])
                print("Puntos "+ resultadoAtk)
                print("Puntos "+ resultadoDef)
                print("="*50)

        #AÑADIMOS JUGADORES DE PARTIDA A LA LISTA GENERAL, BORRAMOS DADOS Y LIMPIAMOS LISTA:
                for jugador in lista:
                    jugador[1].clear()
                    lista_jugadores.append(jugador)




        elif opcion == 5:
            print("¡Gracias por jugar!")
            break

        else:
            print("Opción no válida. Inténtalo de nuevo.")


    if len(lista_jugadores) == 1:

        print(f"¡El jugador ganador es: {lista_jugadores[0][0]}!\n")
        print("**********The Greatest Game In The World**********\n")
        print("1) Show ranking")
        print("2) Find player")
        print("3) Exit")

        while True:
            opcion = input("=>")
            if opcion.isdigit():
                opcion = int(opcion)

                if opcion == 1:
                    cabecera = "RANKING".center(30,"'") + "\n" + "NAME".ljust(20) + "POINTS".rjust(10) + "\n" + "="*30
                    print(cabecera)

                    for recorrido in range(len(lista_jugadores)):
                        for posicion in range(len(lista_jugadores) - recorrido - 1):
                            if lista_jugadores[posicion][2] < lista_jugadores[posicion + 1][2]:
                                lista_jugadores[posicion], lista_jugadores[posicion + 1] = lista_jugadores[posicion + 1], lista_jugadores[posicion]

                    for jugador in lista_jugadores:
                        nombreR = jugador[0].ljust(20)
                        puntosR = str(jugador[2]).rjust(9)
                        print(nombreR, puntosR)



                elif opcion == 2:

                    nombre_buscado = input("Ingresa el nombre del jugador: ")
                    resultados_busqueda = []

                    for jugador in lista_jugadores:
                        if nombre_buscado.lower() in jugador[0].lower():
                            resultados_busqueda.append(jugador)

                    for recorrido in range(len(resultados_busqueda)):
                        for posicion in range(len(resultados_busqueda) - recorrido -1):
                            if resultados_busqueda[posicion][2] < resultados_busqueda[posicion + 1][2]:
                                 resultados_busqueda[posicion], resultados_busqueda[posicion + 1] = resultados_busqueda[posicion + 1], resultados_busqueda[posicion]

                        for jugador in resultados_busqueda:
                            print(f"Jugador: {jugador[0]}, Puntuación: {jugador[2]}")
                    else:
                        print("Jugador no encontrado.")
                elif opcion == 3:
                    print("¡Gracias por jugar!")
                    break

                else:
                    print("Opción no válida. Inténtalo de nuevo.")
            else:
                print("Error: Ingresa un número para seleccionar una opción.")
    else:
        print("Error: Ingresa un número para seleccionar una opción.")




