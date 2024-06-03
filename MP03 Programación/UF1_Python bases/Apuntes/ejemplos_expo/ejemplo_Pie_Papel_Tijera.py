import random
salir = True
bot = True
name = True
partida = True
while salir:
    while name:
        nombre = input("Introduce tu nombre: ")
        if nombre.isalpha() == False:
            print("Pon un nombre valido")
        else:
            name = False
    while bot:
        jugador_p = 0
        oponente_p = 0
        oponente = random.randint(1,6)
        if oponente == 1:
            oponente = "Carlos"
            bot = False
        elif oponente == 2:
            oponente = "Maria"
            bot = False
        elif oponente == 3:
            oponente = "Ana"
            bot = False
        elif oponente == 4:
            oponente = "Luis"
            bot = False
        elif oponente == 5:
            oponente = "Rosa"
            bot = False
        elif oponente == 6:
            oponente = "Marcos"
            bot = False
        print("Tu oponente sera {}".format(oponente))
        input("Pulsa cualquier tecla para continuar")
    while partida:
        x = random.randint(1, 3)
        y = random.randint(1, 3)
        if x == y:
            print("Empate")
            partida = False
        elif (y == 1 and x == 2) or (y == 2 and x == 3) or (y == 3 and x == 1):
            print("Has perdido")
            oponente_p +=1
            partida = False
        else:
            print("Has ganado")
            jugador_p +=1
            partida = False
    if x == 1:
        x = "Piedra"
    elif x == 2:
        x = "Papel"
    elif x == 3:
        x = "Tijera"
    if y == 1:
        y = "Piedra"
    elif y == 2:
        y = "Papel"
    elif y == 3:
        y = "Tijera"
    print("Tirada de {} = {}".format(nombre,y))
    print("Tirada de {} = {}".format(oponente,x))
    opcion = input("1)Cambiar de Bot\n2)Salir\nCualquier otra opcion seguir jugando\n\nOpcion: ")
    if opcion == "1":
        bot = True
        print("Partidas ganadas por {} = {}\nPartidas ganadas por {} = {}".format(nombre,jugador_p,oponente,oponente_p))
    if opcion == "2":
        print("Partidas ganadas por {} = {}\nPartidas ganadas por {} = {}".format(nombre,jugador_p,oponente,oponente_p))
        salir = False
    else:
        partida = True
        input("Pulsa cualquier tecla para continuar")
