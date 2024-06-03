import random
dicc_players = {1:{"nombre":"Luffy","categoria":1,"armas":[1,1],"fuerza":6,"velocidad":7,"experiencia":0},
                2:{"nombre":"Zoro","categoria":1,"armas":[4],"fuerza":5,"velocidad":6,"experiencia":0},
                3:{"nombre":"Sanji","categoria":1,"armas":[1,3],"fuerza":4,"velocidad":6,"experiencia":0},
                4: {"nombre": "Buggy", "categoria": 2, "armas": [3], "fuerza": 2, "velocidad": 4, "experiencia": 0},
                5: {"nombre": "Mr3", "categoria": 2, "armas": [5], "fuerza": 3, "velocidad": 2, "experiencia": 0},
                6: {"nombre": "Xebec", "categoria": 3, "armas": [1, 3], "fuerza": 6, "velocidad": 5, "experiencia": 0},
                7: {"nombre": "Kaido", "categoria": 3, "armas": [4], "fuerza": 8, "velocidad": 3, "experiencia": 0},
                8: {"nombre": "Mama grande", "categoria": 3, "armas": [5], "fuerza": 7, "velocidad": 1, "experiencia": 0},
                9: {"nombre": "Akainu", "categoria": 4, "armas": [2], "fuerza": 6, "velocidad": 4, "experiencia": 0},
                10: {"nombre": "Kizaru", "categoria": 4, "armas": [1, 3], "fuerza": 5, "velocidad": 8, "experiencia": 0},
                11: {"nombre": "Fujitora", "categoria": 4, "armas": [5], "fuerza": 5, "velocidad": 4, "experiencia": 0},
                12: {"nombre": "Garp", "categoria": 5, "armas": [2], "fuerza": 6, "velocidad": 3, "experiencia": 0},
                13: {"nombre": "Smoker", "categoria": 5, "armas": [5], "fuerza": 5, "velocidad": 5, "experiencia": 0},
                14: {"nombre": "Koby", "categoria": 6, "armas": [4], "fuerza": 3, "velocidad": 4, "experiencia": 0},
                15: {"nombre": "Tashigi", "categoria": 6, "armas": [3], "fuerza": 4, "velocidad": 4, "experiencia": 0},
                }
dicc_weapons = {1:{"nombre":"Espada","fuerza":3,"velocidad":5,"dos_manos":False},
                2:{"nombre":"Gran Espada","fuerza":5,"velocidad":3,"dos_manos":True},
                3: {"nombre": "Pistola", "fuerza": 2, "velocidad": 6, "dos_manos": False},
                4: {"nombre": "Rifle", "fuerza": 3, "velocidad": 4, "dos_manos": True},
                5: {"nombre": "Chuchi", "fuerza": 4, "velocidad": 4, "dos_manos": True}
                }
dicc_crews = {1:{"nombre":"Straw Hat","miembros":[8,6]},
              2: {"nombre": "Pirates Buggy", "miembros": [1,3,5]},
              3: {"nombre": "Pirates Rocks", "miembros": [2,4,7]}
              }
dicc_ranks = {1:{"nombre":"Admiral","miembros":[9,10,11]},
              2:{"nombre":"ViceAdmiral","miembros":[12,13]},
              3:{"nombre":"Lieutenant","miembros":[14,15]}
              }
dicc_categorys = {1:"Straw hat",2:"Pirates Buggy",3:"Pirates Rocks",4:"Admiral",5:"ViceAdmiral",6:"Lieutenant"}

menu0 = "======Menu0 (One Piece)======" "\n1)Jugar\n2)Crear\n3)Editar\n4)Listar\n5)Salir"
menu02 = "======Menu02 Crear======" "\n1)Crear personaje\n2)Crear arma\n3)Atrás"
menu021 = "======Menu021 (Nuevo Personaje)======"
menu0211 = "Side of the new character:\n1)Marine\n2)Piratas"
menu02111 = "Rango o banda del nuevo personaje\n1)Admiral\n2)ViceAdmiral\n3)Liutenant"
menu02112 = "Rango o banda del nuevo personaje\n1)Straw hat\n2)Pirates Buggy\n3)Pirates Rocks"
menuarmas = "===============Armas disponibles==============="
menueleccionarmas = "===============Armas del personaje==============="
menu022 = "======Menu021 (Nueva arma)======"
menu0222 = "Fuerza del arma 1-9"
menu02222 = "Velocidad del arma 1-9"
menu022222 = "Tipo de arma\n1)Una mano\n2)Dos manos"
menu03 = "="*10+"Menu 03 (Editar)"+"="*10+"\n1)Editar Personaje\n2)Editar Armas\n3)Atras"
menu031 = "="*10+"Menu 031 (Seleccionar Personaje a Editar)"+"="*10+"\n"
menu032 = "="*10+"Menu 031 (Seleccionar Arma a Editar)"+"="*10+"\n"
menu04 = "======Menu04 (Listar)======" "\n1)Listar personajes\n2)Listar armas\n3)Listar bandos\n4)Listar rangos\n5)Go back"
menu041 = "======Menu041 (Listar Personajes)======" "\n1)Listar por ID\n2)Listar por nombre\n3)Listar por fuerza\n4)Listar por velocidad\n5)Atrás"
menu042 = "======Menu042 (Listar Armas)======" "\n1)Listar por ID\n2)Listar por nombre\n3)Listar por fuerza\n4)Listar por velocidad\n5)Atrás"
menu043 = "="*10+"Menu 043 (Listar Bandos)"+"="*10+"\n1)Listar por ID\n2)Listar por Nombre\n3)Atras\n"
menu044 = "="*10+"Menu 044 (Listar Rangos)"+"="*10+"\n1)Listar por ID\n2)Listar por Nombre\n3)Atras\n"

for i in dicc_players:
    for j in dicc_players[i]["armas"]:
        dicc_players[i]["fuerza"] += dicc_weapons[j]["fuerza"]
        dicc_players[i]["velocidad"] += dicc_weapons[j]["velocidad"]

flag0 = True
flag00 = True
flag04 = False
flag041 = False
flag042 = False
flag043 = False
flag044 = False
flag02 = False
flag03 = False
flag021 = False
flag0211 = False
flag02111 = False
flag02112 = False
flag022 = False
flag0222 = False
flag02222 = False
flag022221 = False
flag022222 = False
flagnombre = False
flagnombrearma = False
flagfinalarma = False


while flag00:
    while flag0:
        print(menu0)
        opcion = input("->Opcion: ")
        if opcion.isdigit() == False or opcion >= "6":
            print("====Opcion invalida====")
            print(menu0)
        else:
            if int(opcion) == 1:
                flag0 = False
                flag00 = False
            if int(opcion) == 2:
                #flag00 = False
                flag02 = True
            if int(opcion) == 3:
                flag03 = True
            if int(opcion) == 4:
                #lag00 = False
                flag04 = True
            if int(opcion) == 5:
                flag00 = False
            flag0 = False
    while flag02:
        print(menu02)
        opcion = input("->Opcion: ")
        if opcion.isdigit() == False or opcion >= "4":
            print("====Opcion invalida====")
            print(menu02)
        else:
            if opcion == "1":
                flag021 = True
                flag02 = False
            if opcion == "2":
                flag022 = True
                flag02 = False
            if opcion == "3":
                flag02 = False
                flag0 = True

    # Creacion nuevo personaje
    while flag021:
        print(menu021)
        nombre = input("Escribe el nombre de tu personaje: \n")
        nombre = nombre.capitalize()
        while True:
            print(menu0211)
            opcion = input("->Opcion: ")
            if opcion.isdigit() == False:
                print("====Opcion invalida====")
            if opcion >= "3":
                print("====Opcion invalida====")
            else:
                if opcion == "1":
                    bando = "Marine"
                    while True:
                        print(menu02111)
                        # 1)Admiral\n2)ViceAdmiral\n3)Liutenant
                        rango = input("->Opcion: ")
                        cat = rango
                        if rango.isdigit() == False or rango >= "4":
                            print("====Opcion invalida====")
                        else:
                            rango = int(rango)
                            if (rango+3) in dicc_categorys:
                                rango= dicc_categorys[rango+3]
                                print("El personaje", nombre, "pertenece al bando", bando, "y su rango es", rango,"\n")

                            opc = input("Guardar este personaje S/N ")
                            if opc.upper() == "S":
                                print("\n")
                                vel = random.randint(1, 9)
                                stre = random.randint(1, 9)
                                new_char = dicc_players[len(dicc_players) + 1] = {}
                                new_char['nombre'] = nombre
                                new_char['categoria'] = cat
                                new_char['velocidad'] = vel
                                new_char['fuerza'] = stre
                                print(dicc_players)
                                input("presiona enter para seguir")
                                flag021 = False
                                print("El codigo a partir de aqui se queda en bucle en la ultima opcion")
                            else:
                                print("\n")
                                print("El codigo a partir de aqui se queda en bucle en la ultima opcion")
                                flag021 = False
                            flag0 = True
                                #                         while True:
                                    # while True:
                                    #     while True:
                                    #         print(menuarmas)
                                    #         listaID = []
                                    #         for i in dicc_weapons:
                                    #             listaID.append(i)
                                    #         for i in range(len(listaID) - 1):
                                    #             for j in range(len(listaID) - i - 1):
                                    #                 if listaID[j] > listaID[j + 1]:
                                    #                     numero = listaID[j]
                                    #                     listaID[j] = listaID[j + 1]
                                    #                     listaID[j + 1] = numero
                                    #
                                    #         for i in listaID:
                                    #             if dicc_weapons[i]["dos_manos"] == True:
                                    #                 dosm = "True"
                                    #             else:
                                    #                 dosm = "False"
                                    #             id = "{})".format(i).ljust(5) + dicc_weapons[i]["nombre"]+",".ljust(2) + "Fuerza:" + str(
                                    #                 dicc_weapons[i]["fuerza"])+",".ljust(2)\
                                    #                  + "Velocidad:" + str(dicc_weapons[i]["velocidad"])
                                    #             print(id)
                                    #
                                    #         else:
                                    #             listaarmas = []
                                    #             slots = 2
                                    #             print("\nAdd Weapons\nWeapon ID) To add weapon ID\n0) Finish add weapons\n-Weapon ID) To delete weapon")
                                    #             while True:
                                    #                 idarma = input("Option-> ")
                                    #                 listaarmadisp = []
                                    #                 for idarma in dicc_weapons:
                                    #                     if slots == 2 or (slots == 1 and dicc_weapons["dos_manos"] == False):
                                    #                         listaarmadisp.append(idarma)
                                    #                 print(listaarmadisp)
                                    #                 print(listaarmas)
                                    #                 if idarma > 0:
                                    #                     listaarmas.append(idarma)
                                    #                     if dicc_weapons[idarma]["dos_manos"] == False:
                                    #                         slots -= 1
                                    #                     else:
                                    #                         slots -= 2
                                    #                 if idarma < 0:
                                    #                     listaarmas.remove(idarma)
                                    #                     if dicc_weapons[idarma]["dos_manos"] == False:
                                    #                         slots += 1
                                    #                     else:
                                    #                         slots += 2
                if opcion == "2":
                    bando = "Piratas"
                    while True:
                        while True:
                            print(menu02112)
                            # 1)Admiral\n2)ViceAdmiral\n3)Liutenant
                            rango = input("->Opcion: ")
                            if rango.isdigit() == False or rango >= "4":
                                print("====Opcion invalida====")
                            else:
                                rango = int(rango)
                                cat = rango
                                if (rango) in dicc_categorys:
                                    rango = dicc_categorys[rango]
                                print("El personaje", nombre, "pertenece al bando", bando, "y su rango es", rango,
                                      "\n")
                                opc = input("Guardar este personaje S/N ")
                                if opc.upper() == "S":
                                    print("\n")
                                    vel = random.randint(1, 9)
                                    stre = random.randint(1, 9)
                                    new_char = dicc_players[len(dicc_players) + 1] = {}
                                    new_char['nombre'] = nombre
                                    new_char['categoria'] = cat
                                    new_char['velocidad'] = vel
                                    new_char['fuerza'] = stre
                                    print(dicc_players)
                                    input("presiona enter para seguir")
                                    flag021 = False
                                    print("El codigo a partir de aqui se queda en bucle en la ultima opcion")
                                else:
                                    print("\n")
                                    print("El codigo a partir de aqui se queda en bucle en la ultima opcion")
                                    flag021 = False
                                flag0 = True
    #                         while True:
    #                             while True:
    #                                 print(menuarmas)
    #                                 listaID = []
    #                                 for i in dicc_weapons:
    #                                     listaID.append(i)
    #                                 for i in range(len(listaID) - 1):
    #                                     for j in range(len(listaID) - i - 1):
    #                                         if listaID[j] > listaID[j + 1]:
    #                                             numero = listaID[j]
    #                                             listaID[j] = listaID[j + 1]
    #                                             listaID[j + 1] = numero
    #
    #                                 for i in listaID:
    #                                     if dicc_weapons[i]["dos_manos"] == True:
    #                                         dosm = "True"
    #                                     else:
    #                                         dosm = "False"
    #                                     id = "{})".format(i).ljust(5) + dicc_weapons[i]["nombre"] + ",".ljust(
    #                                         2) + "Fuerza:" + str(
    #                                         dicc_weapons[i]["fuerza"]) + ",".ljust(2) \
    #                                          + "Velocidad:" + str(dicc_weapons[i]["velocidad"])
    #                                     print(id)
    #
    #                                 else:
    #                                     while True:
    #                                         while True:
    #                                             print("\n")
    #                                             print(menueleccionarmas)
    #                                             input()
    #                                 break
    #

    #creación de armas
    while flag022:
        print(menu022)
        nombrearma = input("Escribe el nombre de tu arma: \n")
        nombrearma = nombrearma.capitalize()
        print(nombrearma)
        while True:
            print(menu0222)
            stre = input("->Opcion: ")
            if stre.isdigit() == False:
                print("Invalid weapon strength")
            elif int(stre) > 9 or int(stre) < 1:
                print("Invalid weapon strength")
            else:
                break
        while True:
            print(menu02222)
            vel = input(" ")
            if vel.isdigit() == False:
                print("Invalid weapon speed")
            if int(vel) > 9 or int(vel) < 1:
                print("Invalid weapon speed")
            else:
                break
        while True:
            print(menu022222)
            type_weap = input("")
            if type_weap.isdigit() == False:
                print("Invalid weapon option")
            if type_weap >= "3" or type_weap < "1":
                print("Invalid weapon option")
            else:
                if type_weap == "1":
                    two_hands = False
                if type_weap == "2":
                    two_hands = True
                break

        print("Name:", nombrearma, "\nStrenght:", stre, "\nSpeed:", vel, "\nTwo Hands Type:", type_weap)
        opc = input("Save this weapon S/N ")
        if opc.upper() == "S":
            print("\n")
            new_weapon = dicc_weapons[len(dicc_weapons)+1] = {}
            new_weapon['nombre']=nombrearma
            new_weapon['fuerza'] = stre
            new_weapon['velocidad'] = vel
            new_weapon['dos_manos'] = two_hands
            print("Hemos guardado el arma")
            input("presiona ENTER para seguir")
            flag022 = False
        else:
            print("No hemos guardamos el arma")
            print("\n")
            flag022 = False
        flag02 = True


    while flag03:
        # Menu editar
            while True:
                # Print menu 03 + elegir opcion
                print(menu03)
                opcion = input("->Opcion: ")
                if not opcion.isdigit():
                    print("\n", "=" * 5, "Valor no valido", "=" * 5, "\n")
                elif int(opcion) < 1 or int(opcion) > 3:
                    print("\n", "=" * 5, "Valor no valido", "=" * 5, "\n")
                else:
                    opcion = int(opcion)
                    break

            if opcion == 1:
                # Editar un Personaje
                print(menu031)
                for i in dicc_players:
                    armitas = []
                    for j in dicc_players[i]["armas"]:
                        armitas.append(dicc_weapons[j]["nombre"])
                    menu0311 = "ID: {},Nombre: {}, Categoria: {}, Armas: {}, Fuerza: {}, Velocidad: {}, Experiencia: {}" \
                        .format(i, dicc_players[i]["nombre"], dicc_players[i]["categoria"], armitas,
                                dicc_players[i]["fuerza"], dicc_players[i]["velocidad"], dicc_players[i]["experiencia"])
                    print(menu0311)
                while True:
                    opcionid = input("ID del Personaje: ")
                    if not opcionid.isdigit():
                        print("\n", "=" * 5, "Valor no valido", "=" * 5, "\n")
                    elif int(opcionid) <= (len(dicc_players) - len(dicc_players)) or int(opcionid) > len(dicc_players):
                        print("\n", "=" * 5, "Valor no valido", "=" * 5, "\n")
                    else:
                        opcionid = int(opcionid)
                        break
                while True:
                    print(
                        "Selecciona la caracteristica a editar del personaje ID: {}, Nombre: {}\n\n1)Nombre\n2)Arma\n3)Atras".format(
                            opcionid, dicc_players[opcionid]["nombre"]))
                    while True:
                        opcioned = input("->Opcion: ")
                        if not opcioned.isdigit():
                            print("\n", "=" * 5, "Valor no valido", "=" * 5, "\n")
                        elif int(opcioned) < 1 or int(opcioned) > 3:
                            print("\n", "=" * 5, "Valor no valido", "=" * 5, "\n")
                        else:
                            opcioned = int(opcioned)
                            break
                    if opcioned == 1:
                        while True:
                            # Introducir nuevo nombre
                            nwnombre = input("Introduce el nuevo nombre (20 Crt):\n")
                            nwnombre = nwnombre.capitalize()
                            if not nwnombre.isalpha():
                                print("Valor no valido")
                            elif not len(nwnombre) < 20:
                                print("El nombre es demasiado largo")
                            elif not len(nwnombre) > 0:
                                print("El nombre es demasiado corto")
                            else:
                                break
                        opcion = input("Estas seguro de que quieres cambiar el nombre de {} por {}?(S/N)".format(
                            dicc_players[opcionid]["nombre"], nwnombre))
                        if opcion == "S" or opcion == "s":
                            dicc_players[opcionid]["nombre"] = nwnombre
                            print("Nombre Actualizado")
                    elif opcioned == 2:
                        print("="*10 + "Opcion no completada" + "="*10)
                    elif opcioned == 3:
                        break

            if opcion == 2:
                # Editar un Arma
                print(menu032)
                for i in dicc_weapons:
                    menu0321 = "{}) {}, Fuerza: {}, Velocidad: {}" \
                        .format(i, dicc_weapons[i]["nombre"], dicc_weapons[i]["fuerza"], dicc_weapons[i]["velocidad"])
                    print(menu0321)
                while True:
                    opcionid = input("ID del Arma: ")
                    if not opcionid.isdigit():
                        print("\n", "=" * 5, "Valor no valido", "=" * 5, "\n")
                    elif int(opcionid) <= (len(dicc_weapons) - len(dicc_weapons)) or int(opcionid) > len(dicc_weapons):
                        print("\n", "=" * 5, "Valor no valido", "=" * 5, "\n")
                    else:
                        opcionid = int(opcionid)
                        break
                while True:
                    print("=" * 10, "Menu 032X (Caracteristica del Arma a Editar)", "=" * 10,
                          "\n\n1)Nombre\n2)Plus Fuerza\n3)Plus Velocidad\n4)Atras\nElige la caracteristica a cambiar del arma ID: {}, Nombre: {}"
                          .format(opcionid, dicc_weapons[opcionid]["nombre"]))
                    while True:
                        opcioned = input("->Opcion: ")
                        if not opcioned.isdigit():
                            print("\n", "=" * 5, "Valor no valido", "=" * 5, "\n")
                        elif int(opcioned) < 1 or int(opcioned) > 4:
                            print("\n", "=" * 5, "Valor no valido", "=" * 5, "\n")
                        else:
                            opcioned = int(opcioned)
                            break
                    if opcioned == 1:
                        while True:
                            # Introducir nuevo nombre
                            nwnombre = input("Introduce el nuevo nombre (20 Crt):\n")
                            nwnombre = nwnombre.capitalize()
                            if not nwnombre.isalpha():
                                print("Valor no valido")
                            elif not len(nwnombre) < 20:
                                print("El nombre es demasiado largo")
                            elif not len(nwnombre) > 0:
                                print("El nombre es demasiado corto")
                            else:
                                break
                        opcion = input("Estas seguro de que quieres cambiar el nombre de {} por {}?(S/N)".format(
                            dicc_weapons[opcionid]["nombre"], nwnombre))
                        if opcion == "S" or opcion == "s":
                            dicc_weapons[opcionid]["nombre"] = nwnombre
                            print("Nombre Actualizado")
                    elif opcioned == 2:
                        while True:
                            # Introducir nueva Fuerza
                            nwfuerza = input("Introduce la nueva fuerza (9 Max):\n")
                            if not nwfuerza.isdigit():
                                print("Valor no valido")
                            elif not int(nwfuerza) < 10:
                                print("Demasiada fuerza")
                            elif not int(nwfuerza) > 0:
                                print("Poca fuerza")
                            else:
                                break
                        opcion = input("Estas seguro de que quieres cambiar la fuerza de {} a {}?(S/N)".format(
                            dicc_weapons[opcionid]["fuerza"], nwfuerza))
                        if opcion == "S" or opcion == "s":
                            dicc_weapons[opcionid]["fuerza"] = nwfuerza
                            print("Fuerza Actualizada")
                    elif opcioned == 3:
                        while True:
                            # Introducir nueva Velocidad
                            nwvelocidad = input("Introduce la nueva velocidad (9 Max):\n")
                            if not nwvelocidad.isdigit():
                                print("Valor no valido")
                            elif not int(nwvelocidad) < 10:
                                print("Demasiada velocidad")
                            elif not int(nwvelocidad) > 0:
                                print("Poca velocidad")
                            else:
                                break
                        opcion = input("Estas seguro de que quieres cambiar la velocidad de {} a {}?(S/N)".format(
                            dicc_weapons[opcionid]["velocidad"], nwvelocidad))
                        if opcion == "S" or opcion == "s":
                            dicc_weapons[opcionid]["velocidad"] = nwvelocidad
                            print("Velocidad Actualizada")
                    elif opcioned == 4:
                        break
                    elif opcion == 3:
                        break
            if opcion == 3:
                flag0 = True
                flag03 = False
    # menu listar
    while flag04:
        while True:
            print(menu04)
            opcion = input("->Opcion: ")
            if not opcion.isdigit():
                print("\n", "=" * 5, "Valor no valido", "=" * 5, "\n")
            elif int(opcion) < 1 or int(opcion) > 5:
                print("\n", "=" * 5, "Valor no valido", "=" * 5, "\n")
            else:
                if int(opcion) == 1:
                    flag04 = False
                    flag041 = True
                if int(opcion) == 2:
                    flag04 = False
                    flag042 = True
                if int(opcion) == 3:
                    flag04 = False
                    flag043 = True
                if int(opcion) == 4:
                    flag04 = False
                    flag044 = True
                if int(opcion) == 5:
                    flag04 = False
                    flag0 = True
                break
    # Listar Personajes
    while flag041:
        while True:
            print(menu041)
            opcion = input("->Opcion: ")
            if not opcion.isdigit():
                print("\n", "=" * 5, "Valor no valido", "=" * 5, "\n")
            elif int(opcion) < 1 or int(opcion) > 5:
                print("\n", "=" * 5, "Valor no valido", "=" * 5, "\n")
            else:
                opcion = int(opcion)
                break
        if opcion == 1:
            # Listar por ID
            menu0411 = "=" * 17 + "Personajes ordenados por ID" + "=" * 17 + "\n" + "ID".ljust(10) + "Nombre".ljust(15) \
                       + "Fuerza".ljust(10) + "Velocidad".ljust(15) + "Experiencia\n" + "*" * 61
            print(menu0411)
            listaID = []
            for i in dicc_players:
                listaID.append(i)

            for i in range(len(listaID) - 1):
                for j in range(len(listaID) - i - 1):
                    if listaID[j] > listaID[j + 1]:
                        numero = listaID[j]
                        listaID[j] = listaID[j + 1]
                        listaID[j + 1] = numero

            for i in listaID:
                id = "{}".format(i).ljust(10) + dicc_players[i]["nombre"].ljust(20) + str(
                    dicc_players[i]["fuerza"]).ljust(13) \
                     + str(dicc_players[i]["velocidad"]).ljust(17) + str(dicc_players[i]["experiencia"])
                print(id)
            input()
        elif opcion == 2:
            # Listar por Nombre
            menu0412 = "=" * 15 + "Personajes ordenados por Nombre" + "=" * 15 + "\n" + "ID".ljust(10) + "Nombre".ljust(
                15) \
                       + "Fuerza".ljust(10) + "Velocidad".ljust(15) + "Experiencia\n" + "*" * 61
            print(menu0412)
            listaName = []
            for i in dicc_players:
                listaName.append(dicc_players[i]["nombre"])

            for i in range(len(listaName) - 1):
                for j in range(len(listaName) - i - 1):
                    if listaName[j] > listaName[j + 1]:
                        numero = listaName[j]
                        listaName[j] = listaName[j + 1]
                        listaName[j + 1] = numero
            for i in listaName:
                for j in dicc_players:
                    if i == dicc_players[j]["nombre"]:
                        string_nombre = str("{}".format(j)).ljust(10) + str("{}".format(i)).ljust(20) + str(
                            dicc_players[j]["fuerza"]).ljust(13) \
                                        + str(dicc_players[j]["velocidad"]).ljust(17) + str(
                            dicc_players[j]["experiencia"])
                        print(string_nombre)
            input()

        elif opcion == 3:
            # Listar por Fuerza
            menu0413 = "=" * 15 + "Personajes ordenados por Fuerza" + "=" * 15 + "\n" + "ID".ljust(
                10) + "Nombre".ljust(15) \
                       + "Fuerza".ljust(10) + "Velocidad".ljust(15) + "Experiencia\n" + "*" * 61
            print(menu0413)
            listaStg = []
            listaKys = []
            for i in dicc_players:
                listaStg.append(dicc_players[i]["fuerza"])
                listaKys.append(i)
            for i in range(len(listaStg) - 1):
                for j in range(len(listaStg) - i - 1):
                    if listaStg[j] < listaStg[j + 1]:
                        numero = listaStg[j]
                        listaStg[j] = listaStg[j + 1]
                        listaStg[j + 1] = numero

                        numero = listaKys[j]
                        listaKys[j] = listaKys[j + 1]
                        listaKys[j + 1] = numero
            for n in listaKys:
                string_fuerza = str("{}".format(n)).ljust(10) + str(dicc_players[n]["nombre"]).ljust(
                    20) + str(
                    dicc_players[n]["fuerza"]).ljust(13) \
                                + str(dicc_players[n]["velocidad"]).ljust(17) + str(
                    dicc_players[n]["experiencia"])
                print(string_fuerza)
            input()
        elif opcion == 4:
            # Listar por Velocidad
            menu0414 = "=" * 14 + "Personajes ordenados por Velocidad" + "=" * 13 + "\n" + "ID".ljust(
                10) + "Nombre".ljust(15) \
                       + "Fuerza".ljust(10) + "Velocidad".ljust(15) + "Experiencia\n" + "*" * 61
            print(menu0414)
            listaVlz = []
            listaKys = []
            for i in dicc_players:
                listaVlz.append(dicc_players[i]["velocidad"])
                listaKys.append(i)

            for i in range(len(listaVlz) - 1):
                for j in range(len(listaVlz) - i - 1):
                    if listaVlz[j] < listaVlz[j + 1]:
                        numero = listaVlz[j]
                        listaVlz[j] = listaVlz[j + 1]
                        listaVlz[j + 1] = numero

                        numero = listaKys[j]
                        listaKys[j] = listaKys[j + 1]
                        listaKys[j + 1] = numero
            for n in listaKys:
                string_velocidad = str("{}".format(n)).ljust(10) + str(dicc_players[n]["nombre"]).ljust(
                    20) + str(dicc_players[n]["fuerza"]).ljust(13) \
                                   + str(dicc_players[n]["velocidad"]).ljust(17) + str(
                    dicc_players[n]["experiencia"])
                print(string_velocidad)
            input()
        elif opcion == 5:
            flag041 = False
            flag04 = True

    # Listar Armas
    while flag042:
        while True:
            print(menu042)
            opcion = input("->Opcion: ")
            if not opcion.isdigit():
                print("\n", "=" * 5, "Valor no valido", "=" * 5, "\n")
            elif int(opcion) < 1 or int(opcion) > 5:
                print("\n", "=" * 5, "Valor no valido", "=" * 5, "\n")
            else:
                opcion = int(opcion)
                break

        if int(opcion) == 1:
            # Listar por ID
            menu0421 = "=" * 19 + "Armas ordenados por ID" + "=" * 20 + "\n" + "ID".ljust(
                10) + "Nombre".ljust(15) \
                       + "Fuerza".ljust(10) + "Velocidad".ljust(15) + "A dos manos\n" + "*" * 61
            print(menu0421)
            listaID = []
            for i in dicc_weapons:
                listaID.append(i)

            for i in range(len(listaID) - 1):
                for j in range(len(listaID) - i - 1):
                    if listaID[j] > listaID[j + 1]:
                        numero = listaID[j]
                        listaID[j] = listaID[j + 1]
                        listaID[j + 1] = numero

            for i in listaID:
                if dicc_weapons[i]["dos_manos"] == True:
                    dosm = "True"
                else:
                    dosm = "False"
                id = "{}".format(i).ljust(10) + dicc_weapons[i]["nombre"].ljust(20) + str(
                    dicc_weapons[i]["fuerza"]).ljust(13) \
                     + str(dicc_weapons[i]["velocidad"]).ljust(13) + dosm
                print(id)
            input()

        elif int(opcion) == 2:
            # Listar por Nombre
            menu0412 = "=" * 17 + "Armas ordenados por Nombre" + "=" * 18 + "\n" + "ID".ljust(
                10) + "Nombre".ljust(15) \
                       + "Fuerza".ljust(10) + "Velocidad".ljust(15) + "A dos manos\n" + "*" * 61
            print(menu0412)
            listaName = []
            for i in dicc_weapons:
                listaName.append(dicc_weapons[i]["nombre"])

            for i in range(len(listaName) - 1):
                for j in range(len(listaName) - i - 1):
                    if listaName[j] > listaName[j + 1]:
                        numero = listaName[j]
                        listaName[j] = listaName[j + 1]
                        listaName[j + 1] = numero
            for i in listaName:
                for j in dicc_weapons:
                    if i == dicc_weapons[j]["nombre"]:
                        if dicc_weapons[j]["dos_manos"] == True:
                            dosm = "True"
                        else:
                            dosm = "False"
                        string_nombre = str("{}".format(j)).ljust(10) + str("{}".format(i)).ljust(20) + str(
                            dicc_weapons[j]["fuerza"]).ljust(13) + str(dicc_weapons[j]["velocidad"]).ljust(
                            13) + dosm
                        print(string_nombre)
            input()
        elif opcion == 3:
            # Listar por Fuerza
            menu0423 = "=" * 17 + "Armas ordenados por Fuerza" + "=" * 18 + "\n" + "ID".ljust(
                10) + "Nombre".ljust(15) \
                       + "Fuerza".ljust(10) + "Velocidad".ljust(15) + "A dos manos\n" + "*" * 61
            print(menu0423)
            listaStg = []
            listaKys = []

            for i in dicc_weapons:
                listaStg.append(dicc_weapons[i]["fuerza"])
                listaKys.append(i)

            for i in range(len(listaStg) - 1):
                for j in range(len(listaStg) - i - 1):
                    if listaStg[j] < listaStg[j + 1]:
                        numero = listaStg[j]
                        listaStg[j] = listaStg[j + 1]
                        listaStg[j + 1] = numero

                        numero = listaKys[j]
                        listaKys[j] = listaKys[j + 1]
                        listaKys[j + 1] = numero

            for n in listaKys:
                if dicc_weapons[n]["dos_manos"] == True:
                    dosm = "True"
                else:
                    dosm = "False"
                string_stg = str("{}".format(n)).ljust(10) + str(dicc_weapons[n]["nombre"]).ljust(20) + str(
                    dicc_weapons[n]["fuerza"]).ljust(13) \
                             + str(dicc_weapons[n]["velocidad"]).ljust(13) + dosm
                print(string_stg)
            input()
        elif opcion == 4:
            # Listar por Velocidad
            menu0424 = "=" * 17 + "Armas ordenados por Velocidad" + "=" * 18 + "\n" + "ID".ljust(10) + "Nombre".ljust(
                15) \
                       + "Fuerza".ljust(10) + "Velocidad".ljust(15) + "A dos manos\n" + "*" * 61
            print(menu0424)
            listaVlz = []
            listaKys = []

            for i in dicc_weapons:
                listaVlz.append(dicc_weapons[i]["fuerza"])
                listaKys.append(i)

            for i in range(len(listaVlz) - 1):
                for j in range(len(listaVlz) - i - 1):
                    if listaVlz[j] > listaVlz[j + 1]:
                        numero = listaVlz[j]
                        listaVlz[j] = listaVlz[j + 1]
                        listaVlz[j + 1] = numero

                        numero = listaKys[j]
                        listaKys[j] = listaKys[j + 1]
                        listaKys[j + 1] = numero

            for n in listaKys:
                if dicc_weapons[n]["dos_manos"] == True:
                    dosm = "True"
                else:
                    dosm = "False"
                string_vlc = str("{}".format(n)).ljust(10) + str(dicc_weapons[n]["nombre"]).ljust(20) + str(
                    dicc_weapons[n]["fuerza"]).ljust(13) \
                             + str(dicc_weapons[n]["velocidad"]).ljust(13) + dosm
                print(string_vlc)
            input()
        elif opcion == 5:
            flag042 = False
            flag04 = True

    # Listar Bandos
    while flag043:
        while True:
            print(menu043)
            opcion = input("->Opcion: ")
            if not opcion.isdigit():
                print("\n", "=" * 5, "Valor no valido", "=" * 5, "\n")
            elif int(opcion) < 1 or int(opcion) > 5:
                print("\n", "=" * 5, "Valor no valido", "=" * 5, "\n")
            else:
                opcion = int(opcion)
                break
        if opcion == 1:
            # Listar por ID
            menu0431 = "=" * 19 + "Bandos ordenador por ID" + "=" * 19 + "\n" + "ID".ljust(
                10) + "Nombre".ljust(20) + "Miembros".ljust(10) + "\n" + "*" * 61
            print(menu0431)
            for i in dicc_crews:
                cadenambr = ""
                for j in dicc_crews[i]["miembros"]:
                    cadenambr = cadenambr + str(dicc_players[j]["nombre"]) + "\n".ljust(31)
                    string_bando = str("{}".format(i)).ljust(10) + str(dicc_crews[i]["nombre"]).ljust(
                        20) + str(cadenambr).ljust(13)
                print(string_bando)
            input()
        if opcion == 2:
            # Listar por Nombre
            menu0432 = "=" * 17 + "Bandos ordenador por Nombre" + "=" * 17 + "\n" + "ID".ljust(
                10) + "Nombre".ljust(20) + "Miembros".ljust(10) + "\n" + "*" * 61
            print(menu0432)
            listaCrew = []
            for i in dicc_crews:
                listaCrew.append(dicc_crews[i]["nombre"])

            for i in range(len(listaCrew) - 1):
                for j in range(len(listaCrew) - i - 1):
                    if listaCrew[j] > listaCrew[j + 1]:
                        numero = listaCrew[j]
                        listaCrew[j] = listaCrew[j + 1]
                        listaCrew[j + 1] = numero

            for i in listaCrew:
                for j in dicc_crews:
                    if i == dicc_crews[j]["nombre"]:
                        cadenambr = ""
                        for x in dicc_crews[j]["miembros"]:
                            cadenambr = cadenambr + str(dicc_players[x]["nombre"]) + "\n".ljust(31)
                            string_bando = str("{}".format(j)).ljust(10) + str(dicc_crews[j]["nombre"]).ljust(
                                20) + str(cadenambr).ljust(13)
                        print(string_bando)
            input()
        if opcion == 3:
            flag043 = False
            flag04 = True

    while flag044:
        while True:
            print(menu044)
            opcion = input("->Opcion: ")
            if not opcion.isdigit():
                print("\n", "=" * 5, "Valor no valido", "=" * 5, "\n")
            elif int(opcion) < 1 or int(opcion) > 5:
                print("\n", "=" * 5, "Valor no valido", "=" * 5, "\n")
            else:
                opcion = int(opcion)
                break
        if opcion == 1:
            # Listar por ID
            menu0431 = "=" * 19 + "Bandos ordenador por ID" + "=" * 19 + "\n" + "ID".ljust(
                10) + "Nombre".ljust(20) + "Miembros".ljust(10) + "\n" + "*" * 61
            print(menu0431)
            for i in dicc_ranks:
                cadenambr = ""
                for j in dicc_ranks[i]["miembros"]:
                    cadenambr = cadenambr + str(dicc_players[j]["nombre"]) + "\n".ljust(31)
                    string_bando = str("{}".format(i)).ljust(10) + str(dicc_ranks[i]["nombre"]).ljust(
                        20) + str(cadenambr).ljust(13)
                print(string_bando)
            input()
        if opcion == 2:
            # Listar por Nombre
            menu0432 = "=" * 17 + "Bandos ordenador por Nombre" + "=" * 17 + "\n" + "ID".ljust(
                10) + "Nombre".ljust(20) + "Miembros".ljust(10) + "\n" + "*" * 61
            print(menu0432)
            listaCrew = []
            for i in dicc_ranks:
                listaCrew.append(dicc_ranks[i]["nombre"])

            for i in range(len(listaCrew) - 1):
                for j in range(len(listaCrew) - i - 1):
                    if listaCrew[j] > listaCrew[j + 1]:
                        numero = listaCrew[j]
                        listaCrew[j] = listaCrew[j + 1]
                        listaCrew[j + 1] = numero

            for i in listaCrew:
                for j in dicc_ranks:
                    if i == dicc_ranks[j]["nombre"]:
                        cadenambr = ""
                        for x in dicc_ranks[j]["miembros"]:
                            cadenambr = cadenambr + str(dicc_players[x]["nombre"]) + "\n".ljust(31)
                            string_bando = str("{}".format(j)).ljust(10) + str(dicc_ranks[j]["nombre"]).ljust(
                                20) + str(cadenambr).ljust(13)
                        print(string_bando)
            input()
        if opcion == 3:
            flag044= False
            flag04 = True