import random
partida = True

while partida:
    print("Inicia partida")
    jugador_p = 0
    bot_p = 0
    ronda = 0
    while True:
        dadoj = random.randint(1, 6)
        dadob = random.randint(1, 6)
        jugador = dadoj
        bot = dadob
        print(jugador,"y",bot)
        if jugador != bot:
            break
        else:
            print("Salieron iguales")
    if jugador > bot:
        quien = 1
    else:
        quien = 0
    while True:
        if quien == 1:
            while True:
                input("Tira jugador")
                d1 = random.randint(1, 6)
                d2 = random.randint(1, 6)
                d3 = random.randint(1, 6)
                d4 = random.randint(1, 6)
                print("Ha salido {}, {}, {}, y {}.".format(d1,d2,d3,d4))
                if d1 ==d2==d3:
                    jugador_p +=(d1+d2+d3)
                    quien = 0
                    ronda += 1
                    break
                elif d1==d2==d4:
                    jugador_p +=(d1+d2+d4)
                    quien = 0
                    ronda +=1
                    break
                elif d1 == d3 == d4:
                    jugador_p += (d1 + d3 + d4)
                    quien = 0
                    ronda += 1
                    break
                elif d2 == d3 == d4:
                    jugador_p += (d3 + d2 + d4)
                    quien = 0
                    ronda += 1
                    break
                elif d1==d2 or d1==d3 or d1==d4 or d2==d3 or d2==d4 or d3==d4:
                    print("Han salido dados iguales")
                else:
                    print("No ha habido suerte:")
                    quien = 0
                    ronda += 1
                    break
                print("Jugador tiene {} puntos y el bot tiene {} puntos.".format(jugador_p,bot_p))

        if quien == 0:
            while True:
                input("Tira el bot")
                d1 = random.randint(1, 6)
                d2 = random.randint(1, 6)
                d3 = random.randint(1, 6)
                d4 = random.randint(1, 6)
                print("Ha salido {}, {}, {}, y {}.".format(d1,d2,d3,d4))
                if d1 ==d2==d3:
                    bot_p +=(d1+d2+d3)
                    quien = 1
                    ronda += 1
                    break
                elif d1==d2==d4:
                    bot_p +=(d1+d2+d4)
                    quien = 1
                    ronda += 1
                    break
                elif d1 == d3 == d4:
                    bot_p += (d1 + d3 + d4)
                    quien = 1
                    ronda += 1
                    break
                elif d2 == d3 == d4:
                    bot_p += (d3 + d2 + d4)
                    quien = 1
                    ronda += 1
                    break
                elif d1==d2 or d1==d3 or d1==d4 or d2==d3 or d2==d4 or d3==d4:
                    print("Han salido dados iguales")
                else:
                    print("No ha habido suerte:")
                    quien = 1
                    ronda += 1
                    break
                print("Jugador tiene {} puntos y el bot tiene {} puntos.".format(jugador_p, bot_p))
        if ronda >= 20:
            break
        else:
            print("RONDA Nº ",ronda/2," CONCLUIDA")

    if jugador_p > bot_p:
        print("Ha ganado el jugador con ",jugador_p," puntos vs {} puntos del bot".format(bot_p))
    else:
        print("Ha ganado el bot con {} puntos vs {} puntos del jugador".format(bot_p,jugador_p))
    x = input("Quieres volver a jugar? S/N")
    if x == "S":
        input("Pulsa para continuar")
    else:
        break
