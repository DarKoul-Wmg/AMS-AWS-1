# William Molina
# 9/11/2023
# 48142524M

import random
import os
import platform

#Nombres
jugadorVermell = ""
jugadorBlau = ""
jugadorVerd = ""
jugadorGroc = ""
# cadenaJug = ""

#Contadores:
num_jugadores = 0
rep_mensaje = 0
jugador_winner = 0
#Cadena de prints:
cadena =''
mensajes = ''
jugadores_terminados =''

#VARIABLES PARA CONTROL DE TURNOS
turnos_inactivosV = 0
turnos_inactivosB = 0
turnos_inactivosD = 0
turnos_inactivosG = 0

#POSICIONES:
posicionV = 0
posicionB = 0
posicionD = 0
posicionG = 0

#POSICION EN TABLERO:
jugadorV = '-V'
jugadorB = '-B'
jugadorD = '-D'
jugadorG = '-G'

#Booleanos
Vermell = False
Blau = False
Verd = False
Groc = False

#Función para limpiar pantalla:
def clear_screen():
 sistema = platform.system()
 if sistema == "Windows":
    os.system('cls')
 else:
    os.system('clear')



tablero = '''
+------+------+------+------+------+------+------+------+
|00    |01    |02    |03    |04    |05*   |06P   |07    |
+------+------+------+------+------+------+------+------+
|25*   |26    |27    |28    |29U   |30*   |31    |08    |
+------+------+------+------+------+------+------+------+
|24D   |43    |44    |45    |46*   |47    |32    |09*   |
+------+------+------+------+------+------+------+------+
|23    |42    |53    |LaOca 54     |48    |33    |10D   |
+------+------+------+------+------+------+------+------+
|22    |41*   |52C   |51    |50    |49    |34*   |11    |
+------+------+------+------+------+------+------+------+
|21*   |40    |39    |38L   |37*   |36    |35    |12    |
+------+------+------+------+------+------+------+------+
|20    |19P   |18    |17H   |16*   |15    |14    |13    |
+------+------+------+------+------+------+------+------+
'''

while True:
    #Actualizar cabecera:
    cabecera = 'La Oca\n'+'-'*20 + '\n1) Assignar jugador Vermell'+(f'({jugadorVermell})' if jugadorVermell
    else '(no assignat)').rjust(17) + '\n2) Assignar jugador Blau'+(f'({jugadorBlau})' if jugadorBlau
    else '(no assignat)').rjust(20) + '\n3) Assignar jugador Verd'+(f'({jugadorVerd})' if jugadorVerd
    else '(no assignat)').rjust(20) + '\n4) Assignar jugador Groc'+(f'({jugadorGroc})' if jugadorGroc
    else '(no assignat)').rjust(20) + '\n5) Començar partida'+('(no disponible)' if num_jugadores < 2
    else "").rjust(25)+'\n0) Sortir'



    print(cabecera)

    opcion = input("Escull una opció [0 - 5]: ")
    if opcion.isdigit():
        opcion = int(opcion)


        if opcion == 1:

            jugadorVermell = input("Introdueix el nom del jugador Vermell: ")
            while not jugadorVermell.replace(" ","").isalpha():
                print(f'"{jugadorVermell}" no és un nom vàlid, introdueix només lletres')
                jugadorVermell = input("Introdueix el nom del jugador Vermell: ")

            else:
                print(f'"{jugadorVermell}" és un nom vàlid')
                num_jugadores += 1
                Vermell = True


        elif opcion == 2:

            jugadorBlau = input("Introdueix el nom del jugador Blau: ")
            while not jugadorBlau.replace(" ","").isalpha():
                print(f'"{jugadorBlau}" no és un nom vàlid, introdueix només lletres')
                jugadorBlau = input("Introdueix el nom del jugador Blau: ")
            else:
                print(f'"{jugadorBlau}" és un nom vàlid')
                num_jugadores += 1
                Blau = True



        elif opcion == 3:

            jugadorVerd = input("Introdueix el nom del jugador Verd: ")
            while not jugadorVerd.replace(" ","").isalpha():
                print(f'"{jugadorVerd}" no és un nom vàlid, introdueix només lletres')
                jugadorVerd = input("Introdueix el nom del jugador Verd: ")
            else:
                print(f'"{jugadorVerd}" és un nom vàlid')
                num_jugadores += 1
                Verd = True



        elif opcion == 4:

            jugadorGroc = input("Introdueix el nom del jugador Groc: ")
            while not jugadorGroc.replace(" ","").isalpha():
                print(f'"{jugadorGroc}" no és un nom vàlid, introdueix només lletres')
                jugadorGroc = input("Introdueix el nom del jugador Groc: ")
            else:
                print(f'"{jugadorGroc}" és un nom vàlid')
                num_jugadores += 1
                Groc = True



        elif opcion == 5:
            if num_jugadores < 2:
                print("Tens que afegir almenys 2 jugadors per poder començar")

            else:


                clear_screen()
                print("\nLA PARTIDA COMENÇA\n")
                print("Tots els jugadors comencen en la posició inicial 0")
                print("")

                while True:
                    #TABLERO: (uso de 02d para dar formato)
                    if posicionV > 54:
                        posicionV = 54

                    if posicionB > 54:
                        posicionB = 54

                    if posicionD > 54:
                        posicionD = 54

                    if posicionG > 54:
                        posicionG = 54

                    tablero_con_jugadores = tablero.replace(f"{posicionV:02d}", f"{posicionV}{jugadorV}") \
                    .replace(f"{posicionB:02d}", f"{posicionB}{jugadorB}") \
                    .replace(f"{posicionD:02d}", f"{posicionD}{jugadorD}") \
                    .replace(f"{posicionG:02d}", f"{posicionG}{jugadorG}")

                    print(tablero_con_jugadores)

                    casilla_Oca = "5, 9, 16, 21, 25, 30, 34, 37, 41, 46, 54"
                    casilla_Daus = 10,24
                    casilla_Pont = 6,19
                    casilla_Hotel = 17
                    casilla_Pou = 29
                    casilla_Laberint = 38
                    casilla_Calavera = 52




                    if Vermell == True:


                        print(f"Torn del la fitxa vermella ({jugadorVermell}):")
                        print("")
                        while True:
                            opcpre = 0
                            opcpos = 0
                            resultado = 0
                            oca = False
                            turno_extra = False
                            print("Opcions:\n"+"1)Tirar dau\n"+"2)Trampa\n"+"3)Sortir\n")
                            opcion = input("Escull una opció: ")
                            if opcion.isdigit():
                                opcion = int(opcion)

                                if opcion == 1:
                                    if turnos_inactivosV > 0:
                                        print(f"{jugadorVermell}  no pot llençar fins que passin: {turnos_inactivosV}\n")
                                        turnos_inactivosV -= 1
                                        break
                                    else:
                                        dadoV = random.randint(1,6)
                                        posicionV += dadoV
                                        mensajes = "- Es llença un dau.\n"+f"- El resultat es {dadoV}. \n" + \
                                                    f"- {jugadorVermell} passa a la casella {posicionV}.\n"
                                        Vermell = False

                                        print(mensajes)

                                    #CASILLA OCA
                                        for casilla in range(len(casilla_Oca)):
                                            if opcpre == 0:
                                                if casilla_Oca[casilla] == " ":
                                                    resultado = int(casilla_Oca[:casilla -1])
                                                    opcpre = casilla
                                                    if resultado == posicionV:
                                                        posicionV = 9
                                                        oca = True
                                                        break
                                            else:
                                                if casilla_Oca[casilla] == " ":
                                                    opcpos = casilla
                                                    resultado = int(casilla_Oca[opcpre:opcpos-1])
                                                    opcpre = opcpos
                                                    if oca == True:
                                                        posicionV = resultado
                                                        break
                                                    if resultado == posicionV:
                                                        oca = True
                                        if oca == True:
                                            print(f"La fitxa vermella {jugadorVermell} passa a la seguent oca {posicionV} i"
                                              f"torna a tirar.\n")
                                            turno_extra = True

                                    #CASILLA DAUS
                                        if posicionV in casilla_Daus:
                                            turno_extra = True

                                            if posicionV == 10:
                                                print(f"Casella 10, Daus, la fitxa vermella {jugadorVermell} "
                                                  f"avança cap a l'altre dau, 24 i torna a tirar\n")
                                                posicionV = 24
                                                break

                                            if posicionV == 24:
                                                print(f"Casella 24, Daus, la fitxa vermella {jugadorVermell} "
                                                  f"avança cap a l'altre dau, 10 i torna a tirar\n")
                                                posicionV = 10
                                                break

                                    #PONT
                                        elif posicionV in casilla_Pont:
                                            if posicionV == 6:
                                                print(f"Casella 6, Pont, la fitxa vermella {jugadorVermell} va a l'altre pont 19\n")
                                                posicionV = 19
                                                break
                                            if posicionV == 19:
                                                print(f"Casella 19, Pont, la fitxa vermella {jugadorVermell} va a l'altre pont 6\n")
                                                posicionV = 6
                                                break
                                    #HOTEL
                                        elif posicionV == casilla_Hotel:
                                            print(f"Casella 17, Hotel, la fitxa vermella {jugadorVermell} no pot jugar, ha d'esperar 1\n")
                                            turnos_inactivosV = 1
                                            break
                                    #POU
                                        elif posicionV == casilla_Pou:
                                            print(f"Casella 29, Pou, la fitxa vermella {jugadorVermell} no pot jugar, ha d'esperar 3\n")
                                            turnos_inactivosV = 3
                                            break
                                    #LABERINT
                                        elif posicionV == casilla_Laberint:
                                            print(f"Casella 38, Laberint, la fitxa vermella {jugadorVermell} no pot jugar, ha d'esperar 3\n")
                                            turnos_inactivosV = 3
                                            break
                                    #CALAVERA
                                        elif posicionV == casilla_Calavera:
                                            posicionV = 0
                                            print(f"La fitxa vermella ({jugadorVermell}) ha caigut en la Calavera, torna a la "
                                                  f"posició inicial 0\n")
                                            break
                                        if turno_extra == False:
                                            break
                                elif opcion == 2:
                                    if turnos_inactivosV > 0:
                                        print(f"{jugadorVermell}  no pot llençar fins que passin: {turnos_inactivosV}\n")
                                        turnos_inactivosV -= 1
                                        break
                                    else:
                                        posicionV = int(input("Trampa, a quina casella vols anar?:\n"))
                                        mensajes = f"- Trampa, a quina casella vols anar?:{posicionV}.\n" + \
                                            f"- {jugadorVermell} passa a la casella {posicionV}.\n"
                                        Vermell = False

                                        print(mensajes)

                                    #CASILLA OCA
                                        for casilla in range(len(casilla_Oca)):
                                            if opcpre == 0:
                                                if casilla_Oca[casilla] == " ":
                                                    resultado = int(casilla_Oca[:casilla -1])
                                                    opcpre = casilla
                                                    if resultado == posicionV:
                                                        posicionV = 9
                                                        oca = True
                                                        break
                                            else:
                                                if casilla_Oca[casilla] == " ":
                                                    opcpos = casilla
                                                    resultado = int(casilla_Oca[opcpre:opcpos-1])
                                                    opcpre = opcpos
                                                    if oca == True:
                                                        posicionV = resultado
                                                        break
                                                    if resultado == posicionV:
                                                        oca = True
                                        if oca == True:
                                            print(f"La fitxa vermella {jugadorVermell} passa a la seguent oca {posicionV} i"
                                              f"torna a tirar.\n")

                                    #CASILLA DAUS
                                        if posicionV in casilla_Daus:
                                            turno_extra = True
                                            if posicionV == 10:
                                                print(f"Casella 10, Daus, la fitxa vermella {jugadorVermell} "
                                                  f"avança cap a l'altre dau, 24 i torna a tirar\n")
                                                posicionV = 24
                                                break

                                            if posicionV == 24:
                                                print(f"Casella 24, Daus, la fitxa vermella {jugadorVermell} "
                                                  f"avança cap a l'altre dau, 10 i torna a tirar\n")
                                                posicionV = 10
                                                break
                                    #PONT
                                        elif posicionV in casilla_Pont:
                                            if posicionV == 6:
                                                print(f"Casella 6, Pont, la fitxa vermella {jugadorVermell} va a l'altre pont 19\n")
                                                posicionV = 19
                                                break
                                            if posicionV == 19:
                                                print(f"Casella 19, Pont, la fitxa vermella {jugadorVermell} va a l'altre pont 6\n")
                                                posicionV = 6
                                                break
                                    #HOTEL
                                        elif posicionV == casilla_Hotel:
                                            print(f"Casella 17, Hotel, la fitxa vermella {jugadorVermell} no pot jugar, ha d'esperar 1\n")
                                            turnos_inactivosV = 1
                                            break
                                    #POU
                                        elif posicionV == casilla_Pou:
                                            print(f"Casella 29, Pou, la fitxa vermella {jugadorVermell} no pot jugar, ha d'esperar 3\n")
                                            turnos_inactivosV = 3
                                            break
                                    #LABERINT
                                        elif posicionV == casilla_Laberint:
                                            print(f"Casella 38, Laberint, la fitxa vermella {jugadorVermell} no pot jugar, ha d'esperar 3\n")
                                            turnos_inactivosV = 3
                                            break
                                    #CALAVERA
                                        elif posicionV == casilla_Calavera:
                                            posicionV = 0
                                            print(f"La fitxa vermella ({jugadorVermell}) ha caigut en la Calavera, torna a la "
                                                  f"posició inicial 0\n")
                                            break
                                        if turno_extra == False:
                                            break
                                elif opcion == 3:
                                    print("Gracies per jugar a la Oca")
                                    break

                                else:
                                    print("Introdueix una de les opcions")

                            else:
                                print("L'opció ha de ser numérica")


                    elif Blau == True:

                        print(f"Torn del la fitxa blava ({jugadorBlau}):")
                        print("")
                        while True:
                            opcpre = 0
                            opcpos = 0
                            resultado = 0
                            oca = False
                            turno_extra = False
                            print("Opcions:\n"+"1)Tirar dau\n"+"2)Trampa\n"+"3)Sortir\n")
                            opcion = input("Escull una opció: ")
                            if opcion.isdigit():
                                opcion = int(opcion)

                                if opcion == 1:
                                    if turnos_inactivosB > 0:
                                        print(f"{jugadorBlau} no pot llençar fins que passin: {turnos_inactivosB}\n")
                                        turnos_inactivosB -= 1
                                        break
                                    else:
                                        dadoB = random.randint(1,6)
                                        posicionB += dadoB
                                        mensajes = "- Es llença un dau.\n"+f"- El resultat es {dadoB}. \n" + \
                                                    f"- {jugadorBlau} passa a la casella {posicionB}.\n"
                                        Blau = False

                                        print(mensajes)

                                    #CASILLA OCA
                                        for casilla in range(len(casilla_Oca)):
                                            if opcpre == 0:
                                                if casilla_Oca[casilla] == " ":
                                                    resultado = int(casilla_Oca[:casilla -1])
                                                    opcpre = casilla
                                                    if resultado == posicionB:
                                                        posicionB = 9
                                                        oca = True
                                                        break
                                            else:
                                                if casilla_Oca[casilla] == " ":
                                                    opcpos = casilla
                                                    resultado = int(casilla_Oca[opcpre:opcpos-1])
                                                    opcpre = opcpos
                                                    if oca == True:
                                                        posicionB = resultado
                                                        break
                                                    if resultado == posicionB:
                                                        oca = True
                                        if oca == True:
                                            print(f"La fitxa blava {jugadorBlau} passa a la seguent oca {posicionB} i"
                                              f"torna a tirar.\n")
                                            turno_extra = True
                                    #CASILLA DAUS
                                        if posicionB in casilla_Daus:
                                            turno_extra = True
                                            if posicionB == 10:
                                                print(f"Casella 10, Daus, la fitxa Blava {jugadorBlau} "
                                                  f"avança cap a l'altre dau, 24 i torna a tirar\n")
                                                posicionB = 24
                                                break

                                            if posicionB == 24:
                                                print(f"Casella 24, Daus, la fitxa Blava {jugadorBlau} "
                                                  f"avança cap a l'altre dau, 10 i torna a tirar\n")
                                                posicionB = 10
                                                break
                                    #PONT
                                        elif posicionB in casilla_Pont:
                                            if posicionB == 6:
                                                print(f"Casella 6, Pont, la fitxa Blava {jugadorBlau} va a l'altre pont 19\n")
                                                posicionB = 19
                                                break
                                            if posicionB == 19:
                                                print(f"Casella 19, Pont, la fitxa Blava {jugadorBlau} va a l'altre pont 6\n")
                                                posicionB = 6
                                                break
                                    #HOTEL
                                        elif posicionB == casilla_Hotel:
                                            print(f"Casella 17, Hotel, la fitxa Blava {jugadorBlau} no pot jugar, ha d'esperar 1\n")
                                            turnos_inactivosB = 1
                                            break
                                    #POU
                                        elif posicionB == casilla_Pou:
                                            print(f"Casella 29, Pou, la fitxa Blava {jugadorBlau} no pot jugar, ha d'esperar 3\n")
                                            turnos_inactivosB = 3
                                            break
                                    #LABERINT
                                        elif posicionB == casilla_Laberint:
                                            print(f"Casella 38, Laberint, la fitxa Blava {jugadorBlau} no pot jugar, ha d'esperar 3\n")
                                            turnos_inactivosB = 3
                                            break
                                    #CALAVERA
                                        elif posicionB == casilla_Calavera:
                                            posicionB = 0
                                            print(f"La fitxa Blava ({jugadorBlau}) ha caigut en la Calavera, torna a la "
                                                  f"posició inicial 0\n")
                                            break
                                        if turno_extra == False:
                                            break

                                elif opcion == 2:
                                    if turnos_inactivosB > 0:
                                        print(f"{jugadorBlau} no pot llençar fins que passin: {turnos_inactivosB}\n")
                                        turnos_inactivosB -= 1
                                        break
                                    else:
                                        posicionB = int(input("Trampa, a quina casella vols anar?:\n"))
                                        mensajes = f"- Trampa, a quina casella vols anar?:{posicionB}.\n" + \
                                            f"- {jugadorBlau} passa a la casella {posicionB}.\n"
                                        Blau = False

                                        print(mensajes)

                                    #CASILLA OCA
                                        for casilla in range(len(casilla_Oca)):
                                            if opcpre == 0:
                                                if casilla_Oca[casilla] == " ":
                                                    resultado = int(casilla_Oca[:casilla -1])
                                                    opcpre = casilla
                                                    if resultado == posicionB:
                                                        posicionB = 9
                                                        oca = True
                                                        break
                                            else:
                                                if casilla_Oca[casilla] == " ":
                                                    opcpos = casilla
                                                    resultado = int(casilla_Oca[opcpre:opcpos-1])
                                                    opcpre = opcpos
                                                    if oca == True:
                                                        posicionB = resultado
                                                        break
                                                    if resultado == posicionB:
                                                        oca = True
                                        if oca == True:
                                            print(f"La fitxa blava {jugadorBlau} passa a la seguent oca {posicionB} i"
                                              f"torna a tirar.\n")
                                            turno_extra = True
                                    #CASILLA DAUS
                                        if posicionB in casilla_Daus:
                                            turno_extra = True
                                            if posicionB == 10:
                                                print(f"Casella 10, Daus, la fitxa Blava {jugadorBlau} "
                                                  f"avança cap a l'altre dau, 24 i torna a tirar\n")
                                                posicionB = 24
                                                break

                                            if posicionB == 24:
                                                print(f"Casella 24, Daus, la fitxa Blava {jugadorBlau} "
                                                  f"avança cap a l'altre dau, 10 i torna a tirar\n")
                                                posicionB = 10
                                                break
                                    #PONT
                                        elif posicionB in casilla_Pont:
                                            if posicionB == 6:
                                                print(f"Casella 6, Pont, la fitxa Blava {jugadorBlau} va a l'altre pont 19\n")
                                                posicionB = 19
                                                break
                                            if posicionB == 19:
                                                print(f"Casella 19, Pont, la fitxa Blava {jugadorBlau} va a l'altre pont 6\n")
                                                posicionB = 6
                                                break
                                    #HOTEL
                                        elif posicionB == casilla_Hotel:
                                            print(f"Casella 17, Hotel, la fitxa Blava {jugadorBlau} no pot jugar, ha d'esperar 1\n")
                                            turnos_inactivosB = 1
                                            break
                                    #POU
                                        elif posicionB == casilla_Pou:
                                            print(f"Casella 29, Pou, la fitxa Blava {jugadorBlau} no pot jugar, ha d'esperar 3\n")
                                            turnos_inactivosB = 3
                                            break
                                    #LABERINT
                                        elif posicionB == casilla_Laberint:
                                            print(f"Casella 38, Laberint, la fitxa Blava {jugadorBlau} no pot jugar, ha d'esperar 3\n")
                                            turnos_inactivosB = 3
                                            break
                                    #CALAVERA
                                        elif posicionB == casilla_Calavera:
                                            posicionB = 0
                                            print(f"La fitxa Blava ({jugadorBlau}) ha caigut en la Calavera, torna a la "
                                                  f"posició inicial 0\n")
                                            break
                                        if turno_extra == False:

                                            break
                                elif opcion == 3:
                                    print("Gracies per jugar a la Oca")
                                    break

                                else:
                                    print("Introdueix una de les opcions")

                            else:
                                print("L'opció ha de ser numérica")

                    elif Verd == True:


                        print(f"Torn del la fitxa verda ({jugadorVerd}):")
                        print("")
                        while True:
                            opcpre = 0
                            opcpos = 0
                            resultado = 0
                            oca = False
                            turno_extra = False
                            print("Opcions:\n"+"1)Tirar dau\n"+"2)Trampa\n"+"3)Sortir\n")
                            opcion = input("Escull una opció: ")
                            if opcion.isdigit():
                                opcion = int(opcion)

                                if opcion == 1:
                                    if turnos_inactivosD > 0:
                                        print(f"{jugadorVerd} no pot llençar fins que passin: {turnos_inactivosD}\n")
                                        turnos_inactivosD -= 1
                                        break
                                    else:
                                        dadoD = random.randint(1,6)
                                        posicionD += dadoD
                                        mensajes = "- Es llença un dau.\n"+f"- El resultat es {dadoD}. \n" + \
                                                    f"- {jugadorVerd} passa a la casella {posicionD}.\n"
                                        Verd = False

                                        print(mensajes)

                                    #CASILLA OCA
                                        for casilla in range(len(casilla_Oca)):
                                            if opcpre == 0:
                                                if casilla_Oca[casilla] == " ":
                                                    resultado = int(casilla_Oca[:casilla -1])
                                                    opcpre = casilla
                                                    if resultado == posicionD:
                                                        posicionD = 9
                                                        oca = True
                                                        break
                                            else:
                                                if casilla_Oca[casilla] == " ":
                                                    opcpos = casilla
                                                    resultado = int(casilla_Oca[opcpre:opcpos-1])
                                                    opcpre = opcpos
                                                    if oca == True:
                                                        posicionD = resultado
                                                        break
                                                    if resultado == posicionD:
                                                        oca = True
                                        if oca == True:
                                            print(f"La fitxa verda {jugadorVerd} passa a la seguent oca {posicionD} i"
                                              f"torna a tirar.\n")
                                            turno_extra = True
                                    #CASILLA DAUS
                                        if posicionD in casilla_Daus:
                                            turno_extra = True
                                            if posicionD == 10:
                                                print(f"Casella 10, Daus, la fitxa verda {jugadorVerd} "
                                                  f"avança cap a l'altre dau, 24 i torna a tirar\n")
                                                posicionD = 24
                                                break

                                            if posicionD == 24:
                                                print(f"Casella 24, Daus, la fitxa verda {jugadorVerd} "
                                                  f"avança cap a l'altre dau, 10 i torna a tirar\n")
                                                posicionD = 10
                                                break
                                    #PONT
                                        elif posicionD in casilla_Pont:
                                            if posicionD == 6:
                                                print(f"Casella 6, Pont, la fitxa Verda {jugadorVerd} va a l'altre pont 19\n")
                                                posicionD = 19
                                                break
                                            if posicionD == 19:
                                                print(f"Casella 19, Pont, la fitxa Verda {jugadorVerd} va a l'altre pont 6\n")
                                                posicionD = 6
                                                break
                                    #HOTEL
                                        elif posicionD == casilla_Hotel:
                                            print(f"Casella 17, Hotel, la fitxa Verda {jugadorVerd} no pot jugar, ha d'esperar 1\n")
                                            turnos_inactivosD = 1
                                            break
                                    #POU
                                        elif posicionD == casilla_Pou:
                                            print(f"Casella 29, Pou, la fitxa Verda {jugadorVerd} no pot jugar, ha d'esperar 3\n")
                                            turnos_inactivosD = 3
                                            break
                                    #LABERINT
                                        elif posicionD == casilla_Laberint:
                                            print(f"Casella 38, Laberint, la fitxa Verda {jugadorVerd} no pot jugar, ha d'esperar 3\n")
                                            turnos_inactivosD = 3
                                            break
                                    #CALAVERA
                                        elif posicionD == casilla_Calavera:
                                            posicionD = 0
                                            print(f"La fitxa Verda ({jugadorVerd}) ha caigut en la Calavera, torna a la "
                                                  f"posició inicial 0\n")
                                            break
                                        if turno_extra == False:
                                            break
                                elif opcion == 2:
                                    if turnos_inactivosD > 0:
                                        print(f"{jugadorVerd} no pot llençar fins que passin: {turnos_inactivosD}")
                                        turnos_inactivosD -= 1
                                        break
                                    else:
                                        posicionD = int(input("Trampa, a quina casella vols anar?:\n"))
                                        mensajes = f"- Trampa, a quina casella vols anar?:{posicionD}.\n" + \
                                            f"- {jugadorVerd} passa a la casella {posicionD}.\n"
                                        Verd = False

                                        print(mensajes)

                                    #CASILLA OCA
                                        for casilla in range(len(casilla_Oca)):
                                            if opcpre == 0:
                                                if casilla_Oca[casilla] == " ":
                                                    resultado = int(casilla_Oca[:casilla -1])
                                                    opcpre = casilla
                                                    if resultado == posicionD:
                                                        posicionD = 9
                                                        oca = True
                                                        break
                                            else:
                                                if casilla_Oca[casilla] == " ":
                                                    opcpos = casilla
                                                    resultado = int(casilla_Oca[opcpre:opcpos-1])
                                                    opcpre = opcpos
                                                    if oca == True:
                                                        posicionD = resultado
                                                        break
                                                    if resultado == posicionD:
                                                        oca = True

                                        if oca == True:
                                            print(f"La fitxa verda {jugadorVerd} passa a la seguent oca {posicionD} i"
                                                          f"torna a tirar.\n")
                                            turno_extra = True

                                    #CASILLA DAUS
                                        if posicionD in casilla_Daus:
                                            turno_extra = True
                                            if posicionD == 10:
                                                print(f"Casella 10, Daus, la fitxa verda {jugadorVerd} "
                                                  f"avança cap a l'altre dau, 24 i torna a tirar\n")
                                                posicionD = 24
                                                break

                                            if posicionD == 24:
                                                print(f"Casella 24, Daus, la fitxa verda {jugadorVerd} "
                                                  f"avança cap a l'altre dau, 10 i torna a tirar\n")
                                                posicionD = 10
                                                break
                                    #PONT
                                        elif posicionD in casilla_Pont:
                                            if posicionD == 6:
                                                print(f"Casella 6, Pont, la fitxa Verda {jugadorVerd} va a l'altre pont 19\n")
                                                posicionD = 19
                                                break
                                            if posicionD == 19:
                                                print(f"Casella 19, Pont, la fitxa Verda {jugadorVerd} va a l'altre pont 6\n")
                                                posicionD = 6
                                                break
                                    #HOTEL
                                        elif posicionD == casilla_Hotel:
                                            print(f"Casella 17, Hotel, la fitxa Verda {jugadorVerd} no pot jugar, ha d'esperar 1\n")
                                            turnos_inactivosD = 1
                                            break
                                    #POU
                                        elif posicionD == casilla_Pou:
                                            print(f"Casella 29, Pou, la fitxa Verda {jugadorVerd} no pot jugar, ha d'esperar 3\n")
                                            turnos_inactivosD = 3
                                            break
                                    #LABERINT
                                        elif posicionD == casilla_Laberint:
                                            print(f"Casella 38, Laberint, la fitxa Verda {jugadorVerd} no pot jugar, ha d'esperar 3\n")
                                            turnos_inactivosD = 3
                                            break
                                    #CALAVERA
                                        elif posicionD == casilla_Calavera:
                                            posicionD = 0
                                            print(f"La fitxa Verda ({jugadorVerd}) ha caigut en la Calavera, torna a la "
                                                  f"posició inicial 0\n")
                                            break
                                        if turno_extra == False:
                                            break
                                elif opcion == 3:
                                    print("Gracies per jugar a la Oca")
                                    break

                                else:
                                    print("Introdueix una de les opcions\n")

                            else:
                                print("L'opció ha de ser numérica\n")
                    elif Groc == True:


                        print(f"Torn del la fitxa groga ({jugadorGroc}):")
                        print("")
                        while True:
                            opcpre = 0
                            opcpos = 0
                            resultado = 0
                            oca = False
                            turno_extra = False
                            print("Opcions:\n"+"1)Tirar dau\n"+"2)Trampa\n"+"3)Sortir\n")
                            opcion = input("Escull una opció: ")
                            if opcion.isdigit():
                                opcion = int(opcion)

                                if opcion == 1:
                                    if turnos_inactivosG > 0:
                                        print(f"{jugadorGroc} no pot llençar fins que passin: {turnos_inactivosG}")
                                        turnos_inactivosG -= 1
                                        break
                                    else:
                                        dadoG = random.randint(1,6)
                                        posicionG += dadoG
                                        mensajes = "- Es llença un dau.\n"+f"- El resultat es {dadoG}. \n" + \
                                                    f"- {jugadorGroc} passa a la casella {posicionG}.\n"
                                        Groc = False

                                        print(mensajes)

                                    #CASILLA OCA
                                        for casilla in range(len(casilla_Oca)):
                                            if opcpre == 0:
                                                if casilla_Oca[casilla] == " ":
                                                    resultado = int(casilla_Oca[:casilla -1])
                                                    opcpre = casilla
                                                    if resultado == posicionG:
                                                        posicionG = 9
                                                        oca = True
                                                        break
                                            else:
                                                if casilla_Oca[casilla] == " ":
                                                    opcpos = casilla
                                                    resultado = int(casilla_Oca[opcpre:opcpos-1])
                                                    opcpre = opcpos
                                                    if oca == True:
                                                        posicionG = resultado
                                                        break
                                                    if resultado == posicionG:
                                                        oca = True
                                        if oca == True:
                                            print(f"La fitxa groga {jugadorGroc} passa a la seguent oca {posicionG} i"
                                              f"torna a tirar.\n")
                                            turno_extra = True

                                    #CASILLA DAUS
                                        if posicionG in casilla_Daus:
                                            turno_extra = True
                                            if posicionG == 10:
                                                print(f"Casella 10, Daus, la fitxa groga {jugadorGroc} "
                                                  f"avança cap a l'altre dau, 24 i torna a tirar\n")
                                                posicionG = 24
                                                break

                                            if posicionG == 24:
                                                print(f"Casella 24, Daus, la fitxa groga {jugadorGroc} "
                                                  f"avança cap a l'altre dau, 10 i torna a tirar\n")
                                                posicionG = 10
                                                break
                                    #PONT
                                        elif posicionG in casilla_Pont:
                                            if posicionG == 6:
                                                print(f"Casella 6, Pont, la fitxa Groga {jugadorGroc} va a l'altre pont 19\n")
                                                posicionG = 19
                                                break
                                            if posicionG == 19:
                                                print(f"Casella 19, Pont, la fitxa Groga {jugadorGroc} va a l'altre pont 6\n")
                                                posicionG = 6
                                                break
                                    #HOTEL
                                        elif posicionG == casilla_Hotel:
                                            print(f"Casella 17, Hotel, la fitxa Groga {jugadorGroc} no pot jugar, ha d'esperar 1\n")
                                            turnos_inactivosG = 1
                                            break
                                    #POU
                                        elif posicionG == casilla_Pou:
                                            print(f"Casella 29, Pou, la fitxa Groga {jugadorGroc} no pot jugar, ha d'esperar 3\n")
                                            turnos_inactivosG = 3
                                            break
                                    #LABERINT
                                        elif posicionG == casilla_Laberint:
                                            print(f"Casella 38, Laberint, la fitxa Groga {jugadorGroc} no pot jugar, ha d'esperar 3\n")
                                            turnos_inactivosG = 3
                                            break
                                    #CALAVERA
                                        elif posicionG == casilla_Calavera:
                                            posicionG = 0
                                            print(f"La fitxa Groga ({jugadorGroc}) ha caigut en la Calavera, torna a la "
                                                  f"posició inicial 0\n")
                                            break
                                        if turno_extra == False:
                                            break
                                elif opcion == 2:
                                    if turnos_inactivosG > 0:
                                        print(f"{jugadorGroc} no pot llençar fins que passin: {turnos_inactivosG}")
                                        turnos_inactivosG -= 1
                                        break
                                    else:
                                        posicionG = int(input("Trampa, a quina casella vols anar?:\n"))
                                        mensajes = f"- Trampa, a quina casella vols anar?:{posicionG}.\n" + \
                                            f"- {jugadorGroc} passa a la casella {posicionG}.\n"
                                        Groc = False

                                        print(mensajes)

                                    #CASILLA OCA
                                        for casilla in range(len(casilla_Oca)):
                                            if opcpre == 0:
                                                if casilla_Oca[casilla] == " ":
                                                    resultado = int(casilla_Oca[:casilla -1])
                                                    opcpre = casilla
                                                    if resultado == posicionG:
                                                        posicionG = 9
                                                        oca = True
                                                        break
                                            else:
                                                if casilla_Oca[casilla] == " ":
                                                    opcpos = casilla
                                                    resultado = int(casilla_Oca[opcpre:opcpos-1])
                                                    opcpre = opcpos
                                                    if oca == True:
                                                        posicionG = resultado
                                                        break
                                                    if resultado == posicionG:
                                                        oca = True
                                        if oca == True:
                                            print(f"La fitxa groga {jugadorGroc} passa a la seguent oca {posicionG} i"
                                            f"torna a tirar.")
                                            turno_extra = True

                                    #CASILLA DAUS
                                        if posicionG in casilla_Daus:
                                            turno_extra = True
                                            if posicionG == 10:
                                                print(f"Casella 10, Daus, la fitxa groga {jugadorGroc} "
                                                  f"avança cap a l'altre dau, 24 i torna a tirar\n")
                                                posicionG = 24
                                                break

                                            if posicionG == 24:
                                                print(f"Casella 24, Daus, la fitxa groga {jugadorGroc} "
                                                  f"avança cap a l'altre dau, 10 i torna a tirar\n")
                                                posicionG = 10
                                                break
                                    #PONT
                                        elif posicionG in casilla_Pont:
                                            if posicionG == 6:
                                                print(f"Casella 6, Pont, la fitxa Groga {jugadorGroc} va a l'altre pont: 19\n")
                                                posicionG = 19
                                                break
                                            if posicionG == 19:
                                                print(f"Casella 19, Pont, la fitxa Groga {jugadorGroc} va a l'altre pont: 6\n")
                                                posicionG = 6
                                                break
                                    #HOTEL
                                        elif posicionG == casilla_Hotel:
                                            print(f"Casella 17, Hotel, la fitxa Groga {jugadorGroc} no pot jugar, ha d'esperar 1\n")
                                            turnos_inactivosG = 1
                                            break
                                    #POU
                                        elif posicionG == casilla_Pou:
                                            print(f"Casella 29, Pou, la fitxa Groga {jugadorGroc} no pot jugar, ha d'esperar 3\n")
                                            turnos_inactivosG = 3
                                            break
                                    #LABERINT
                                        elif posicionG == casilla_Laberint:
                                            print(f"Casella 38, Laberint, la fitxa Groga {jugadorGroc} no pot jugar, ha d'esperar 3\n")
                                            turnos_inactivosG = 3
                                            break
                                    #CALAVERA
                                        elif posicionG == casilla_Calavera:
                                            posicionG = 0
                                            print(f"La fitxa Groga ({jugadorGroc}) ha caigut en la Calavera, torna a la "
                                                  f"posició inicial 0\n")
                                            break
                                        if turno_extra == False:
                                            break

                                elif opcion == 3:
                                    print("Gracies per jugar a la Oca")
                                    break

                                else:
                                    print("Introdueix una de les opcions")

                            else:
                                print("L'opció ha de ser numérica")

                    if Vermell == Blau == Verd == Groc == False:
                        if jugadorVermell != "":
                            if posicionV >= 54:
                                jugador_winner +=1
                                cadena += f"El jugador vermell {jugadorVermell} ha arribat al final. En la posición {jugador_winner}.\n"
                                Vermell = False

                            else:
                                Vermell = True

                        if jugadorBlau != "":
                            if posicionB >= 54:
                                jugador_winner +=1
                                cadena += f"El jugador blau {jugadorBlau} ha arribat al final. En la posición {jugador_winner}.\n"
                                Blau = False
                            else:
                                Blau = True

                        if jugadorVerd != "":
                            if posicionD >= 54:
                                jugador_winner +=1
                                cadena += f"El jugador verd {jugadorVerd} ha arribat al final. En la posición {jugador_winner}.\n"
                                Verd = False
                            else:
                                Verd = True

                        if jugadorGroc != "":
                            if posicionG >= 54:
                                jugador_winner +=1
                                cadena += f"El jugador groc {jugadorGroc} ha arribat al final. En la posición {jugador_winner}.\n"
                                Groc = False
                            else:
                                Groc = True
                        if jugador_winner == num_jugadores -1:
                            print("FIN DEL JUEGO!!!\n")

                            if posicionV < 54 and jugadorVermell != "":
                                cadena+= f"El jugador vermell {jugadorVermell} ha perdut."

                            if posicionB < 54 and jugadorBlau != "":
                                cadena+= f"El jugador blau {jugadorBlau} ha perdut."

                            if posicionD < 54 and jugadorVerd != "":
                                cadena+= f"El jugador verd {jugadorVerd} ha perdut."
                            if posicionG < 54 and jugadorGroc != "":
                                cadena+= f"El jugador groc {jugadorGroc} ha perdut."

                            print(cadena)
                            break

        elif opcion == 0:
            print("Gracies por jugar!")
            break


        else:
            print("Selecciona una de les opcions que s'indiquen")
    else:
        print("Has d'ingresar un numero")
