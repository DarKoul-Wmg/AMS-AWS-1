import random
lista_jugadores = [["Juan",[],10], ["Rakel",[],10],["Raul",[],10],["Maria Isabel",[],10], ["Constantina",[],10], ["Jose Antonio",[],10]]


partida = True

while len(lista_jugadores) > 1:#EJECUTAMOS BUCLE HASTA QUE QUEDE 1

    for i in lista_jugadores:
        if i[2] <= 0:
            print(f"El jugador {i[0]} queda eliminado")
            lista_jugadores.remove(i)

    if len(lista_jugadores) == 1:
        # partida = False
        break


    atacante = lista_jugadores[random.randint(0, len(lista_jugadores) -1)]
    defensor = lista_jugadores[random.randint(0, len(lista_jugadores) -1)]
    while defensor == atacante:
        defensor = random.choice(lista_jugadores)

# print(atacante, defensor)
    lista = [atacante, defensor]
    for jugador in lista: #QUITAR JUGADORES DE LISTA
        if jugador in lista_jugadores:
            lista_jugadores.remove(jugador)

# print(lista_jugadores)

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

    # print(lista)

#METODO BURBUJA PARA ORDENAR RESULTADOS:
    for recorrido in range(len(lista_jugadores)):
            for posicion in range(len(lista_jugadores) - recorrido -1):
                if lista_jugadores[posicion][2] < lista_jugadores[posicion + 1][2]:
                     lista_jugadores[posicion], lista_jugadores[posicion + 1] = lista_jugadores[posicion + 1], lista_jugadores[posicion]



    # print(lista_jugadores)
    # break

print("Jugador ganador es:", lista_jugadores)


