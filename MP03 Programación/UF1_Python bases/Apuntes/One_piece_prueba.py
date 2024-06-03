dict_characters = { 1 : {"name" : "Luffy","category": 1, "weapons": [1, 1],"strength" : 6, "speed" : 7,"experience": 0},
                    2 : {"name" : "Zoro","category": 1, "weapons" : [4],"strength" : 5, "speed" : 6,"experience": 0},
                    3 : {"name" : "Sanji", "category" : 1, "weapons" : [1,3],"strength" : 4, "speed" : 6,"experience": 0 },
                    4 : {"name" : "Buggy", "category" : 2, "weapons" : [3], "strength" : 2, "speed" : 4, "experience" : 0},
                    5 : {"name" : "Mr3", "category" : 2, "weapons" : [5], "strength" : 3, "speed" : 2, "experience": 0},
                    6 : {"name" : "Xebec", "category" : 3, "weapons" : [1,3], "strength" : 6, "speed" : 5, "experience" : 0},
                    7 : {"name" : "Kaido", "category" : 3, "weapons" : [4], "strength" : 8, "speed" : 3, "experience" : 0},
                    8 : {"name" : "Mama grande", "category" : 3, "weapons" : [5], "strength" : 7, "speed" : 1, "experience" : 0},
                    9 : {"name" : "Akainu", "category" : 4, "weapons" : [2], "strength" : 6, "speed" : 4, "experience" : 0},
                    10 : {"name" : "Kizaru", "category" : 4, "weapons" : [1,3], "strength" : 5, "speed" : 8, "experience" : 0},
                    11 : {"name" : "Fujitora", "category" : 4, "weapons" : [5], "strength" : 5, "speed" : 4, "experience" : 0},
                    12 : {"name" : "Garp", "category" : 5, "weapons" : [2], "strength" : 6, "speed" : 3, "experience" : 0},
                    13 : {"name" : "Smoker", "category" : 5, "weapons" : [5], "strength" : 5, "speed" : 5, "experience" : 0},
                    14 : {"name" : "Koby", "category" : 6, "weapons" : [4], "strength" : 3, "speed" : 4, "experience" : 0},
                    15 : {"name" : "Tashigi", "category" : 6, "weapons" : [3], "strength" : 4, "speed" : 4, "experience" : 0},
                  }
dict_weapons = { 1 : {"name" : "Sword","strength": 3,"speed": 5,"two_hand":False},
               2 : {"name" : "Greatsword","strength": 5,"speed": 3,"two_hand":True},
               3 : {"name" : "Gun","strength": 2,"speed": 6,"two_hand":False},
               4: {"name": "Rifle", "strength": 3, "speed": 4,"two_hand":True},
               5: {"name": "Chuchi", "strength": 4, "speed": 4,"two_hand":True},
               }
dict_crews = { 1 : {"name" : "Straw hat","members": [8,6]},
                       2 : {"name" : "Pirates Buggy","members": [1,3,5]},
                       3: {"name": "Pirates Rocks","members": [2,4,7,]}
               }
dict_ranks = { 1 : {"name" : "Admiral","members": [9,10,11]},
               2 : {"name" : "ViceAdmiral","members": [12,13]},
               3: {"name": "Lieutenant","members": [14,15]}
               }
dict_categorys = {1:"Straw hat",2:"Pirates Buggy",3:"PiratesRocks",4:"Admiral",5:"ViceAdmiral",6:"Lieutenant"}

#####Menus#####
menu00 = "One Piece".center(30,"*") + "\n\n1)Jugar\n2)Crear\n3)Editar\n4)Listar\n5)Salir\n"

#Creacion
menu02 = "Menu02 ".center(30,"*") + "\n \n1)Crear personaje \n2)Crear arma \n3)Salir\n"
menu02Bandos= "Pirata".center(30,"*") + "\n1)Straw hat\n2)Pirates Buggy\n3)PiratesRocks)\n\n"+ "Marina".center(30,"*") + "\n4)Admiral\n5)ViceAdmiral\n6)Lieutenant\n" + '*'*30
Menu02Arma = "Armas ".center(30,"*")

#Edicion
menu03 = "Menu 03 (Editar Menu)".center(30,"*") + "\n\n1)Editar personajes\n2)Editar armas\n3)Atras\n"
menu031 = "Menu 031 (Selecciona el Personaje a Editar)".center(60,"*") + "\n"
menu032 = "Menu 032 (Selecciona el Arma a Editar)".center(60,"*") + "\n"
menu032x = "Menu 032X (Caracteristica del Arma a Editar)".center(60,"*") + "\n\n1)Nombre\n2)Plus Fuerza\n3)Plus Velocidad\n4)Atras"


while True:
    while True:
        print(menu00)
        opc = input("Opcion: ")
        if not opc.isdigit():
            print("ERROR, esto no es un digito")
        elif int(opc) < 1 or int(opc)>5:
            print("ERROR, este numero no esta en el rango")
        else:
            break
        input("Pulsar para continuar\n")
    #Jugar
    if opc == "1":
        print("Proximamente...")
        input("Pulsar para continuar\n")
    #Creacion de personajes
    elif opc == "2":
        import random
        while True:
            print(menu02)
            opc = input("Opcion: ")
            if not opc.isdigit():
                print("ERROR, esto no es un digito")
            elif int(opc) < 1 or int(opc) > 3:
                print("ERROR, este numero no esta en el rango")
            else:
                print(' ')
                input("Pulsar para continuar\n")
            # opciones
            # 1 personaje
            if opc == '1':

                print('Vamos a crear un nuevo personaje')
                print('*' * 30)
                # nombre

                nombre = input('Nombre del nuevo personaje\n > ')
                input("Pulsar para continuar\n")

                # bando
                print('Vamos a elejir su bando ')
                print('*' * 30)
                print()
                while True:
                    print(menu02Bandos)
                    bando = input('> ')
                    if not bando.isdigit():
                        print('Eso no es un digito')
                    elif int(bando) < 1 or int(bando) > len(dict_categorys):
                        print('No es el rango adecuado')
                    else:
                        bando = int(bando)
                        bando_texto = dict_categorys[bando]
                        break

                print('Tu bando es', bando_texto)

                # armas
                lista_armasd = []
                lista_armas_personaje = []
                while True:
                    armas_disponibles = 2
                    for i in lista_armas_personaje:
                        if dict_weapons[i]["two_hand"] == False:
                            armas_disponibles -= 1
                        elif dict_weapons[i]["two_hand"] == True:
                            armas_disponibles -= 2

                    print("Armas disponibles".center(35, "="))
                    if armas_disponibles == 0:
                        print("Ninguna".center(35, "-"))
                    elif armas_disponibles == 1:
                        for i in dict_weapons:
                            if not dict_weapons[i]["two_hand"]:
                                lista_armasd.append(i)
                                print("{}) {}, Fuerza: {}, Velocidad: {}".format(i, dict_weapons[i]["name"],
                                                                                 dict_weapons[i]["strength"],
                                                                                 dict_weapons[i]["speed"]))
                    elif armas_disponibles == 2:
                        for i in dict_weapons:
                            lista_armasd.append(i)
                            print("{}) {}, Fuerza: {}, Velocidad: {}".format(i, dict_weapons[i]["name"],
                                                                             dict_weapons[i]["strength"],
                                                                             dict_weapons[i]["speed"]))
                    print("Armas actuales".center(35, "="))
                    if len(lista_armas_personaje) == 0:
                        print("Ninguna".center(35, "-"))
                    else:
                        for i in lista_armas_personaje:
                            print("{}) {}, Fuerza: {}, Velocidad: {}".format(i, dict_weapons[i]["name"],
                                                                             dict_weapons[i]["strength"],
                                                                             dict_weapons[i]["speed"]))

                    print("\nInserte:\nID Arma para añadir arma\n0 para salir\n-ID Arma para quitar arma")
                    opc_edt_wp = input("->Opcion: ")
                    if opc_edt_wp == "0":
                        if len(lista_armas_personaje) != 0:
                            break
                        else:
                            print('Añade un arma ')
                    elif len(opc_edt_wp) > 1:
                        if opc_edt_wp[0] == "-":
                            if opc_edt_wp[1:].isdigit():
                                if lista_armas_personaje.count(int(opc_edt_wp[1:])) != 0:
                                    if len(lista_armas_personaje) != 0:
                                        lista_armas_personaje.remove(int(opc_edt_wp[1:]))
                                else:
                                    print("Esas armas no son validas")
                            else:
                                print("Opcion no valida")
                        elif opc_edt_wp.isdigit():
                            if armas_disponibles != 0:
                                lista_armas_personaje.append(int(opc_edt_wp))
                        else:
                            print("Opcion no valida")
                    elif not opc_edt_wp.isdigit():
                        print("Opcion no valida")
                    else:
                        if armas_disponibles != 0:
                            lista_armas_personaje.append(int(opc_edt_wp))
                    print("\n\n")

                # fuerza
                strength = random.randint(1, 9)

                # velocidad
                speed = random.randint(1, 9)

                # experecia
                experience = 0

                print('-' * 30)
                print('Resumen del personaje ')
                print('-' * 30)
                print('Nombre : ', nombre)
                print('Categoria: ', bando_texto)
                if len(lista_armas_personaje) == 1:
                    print('Armas : ', dict_weapons[lista_armas_personaje[0]]['name'])
                elif len(lista_armas_personaje) == 2:
                    print('Armas : ', dict_weapons[lista_armas_personaje[0]]['name'] + ',',
                          dict_weapons[lista_armas_personaje[1]]['name'])
                print('Fuerza: ', strength)
                print('Velocidad: ', speed)
                print('-' * 30)

                while True:
                    gaurdado = input('Quieres guardar el personaje \nS/N \n> ')

                    if gaurdado == 'S' or gaurdado == 's':
                        dict_characters[len(dict_characters) + 1] = {"name": nombre, "category": bando,
                                                                     "weapons": lista_armas_personaje, "strength": 4,
                                                                     "speed": 4, "experience": 0}
                        print('Personaje creado ')
                        break
                    else:
                        print('No se han guardado los datos \n')
                        break


            # creacion de armas
            elif opc == '2':
                print(Menu02Arma)
                print('Vamos a crear una nueva arma')

                nombre = input('Nombre del arma: \n')

                # Fuerza
                while True:
                    print('Fuerza de 1 - 9')
                    fuerzarma = input('> ')
                    if not fuerzarma.isdigit():
                        print('Valor incorrecto')
                    elif int(fuerzarma) < 1 or int(fuerzarma) > 9:
                        print('Es un valor incorrecto')
                    else:
                        fuerzarma = int(fuerzarma)
                        break

                # velocidad
                while True:
                    print('Velocidad de 1 - 9')
                    velocidadarma = input('> ')
                    if not velocidadarma.isdigit():
                        print('Valor incorrecto')
                    elif int(velocidadarma) < 1 or int(velocidadarma) > 9:
                        print('Es un valor incorrecto')
                    else:
                        velocidadarma = int(velocidadarma)
                        break
                while True:
                    # Arma de dos o una mano
                    print('Tipo de arma ')
                    print('1) Una mano \n2) Dos manos')
                    opcarma = input('> ')
                    if not opcarma.isdigit():
                        print("ERROR, esto no es un digito")
                    elif int(opcarma) < 1 or int(opcarma) > 2:
                        print("ERROR, este numero no esta en el rango")
                    else:
                        break

                opcarma = opcarma == "2"

                print('-' * 30)
                print('Resumen del arma ')
                print('-' * 30)
                print('Nombre : ', nombre)
                print('Fuerza: ', fuerzarma)
                print('Velocidad: ', velocidadarma)
                print('Dos manos: ', opcarma)

                while True:
                    gaurdado = input('Quieres guardar el Arma \nS/N \n> ')

                    if gaurdado == 'S' or gaurdado == 's':
                        dict_weapons[len(dict_weapons) + 1] = {"name": nombre, "category": 2, 'strength': fuerzarma,
                                                               'speed': velocidadarma, 'two_hand': opcarma}
                        print('Arma creada ')
                        break
                    else:
                        print('No se han guardado los datos \n')
                        break
            elif opc == '3':
                break

    #Edicion de personajes
    elif opc == "3":
        general = True
        edicion = True
        edicion_1 = False
        edicion_1_1 = False
        edicion_1_2 = False
        editando = False
        edicion_2 = False
        while general:
            while edicion:
                print(menu03)
                opc_edit = input("Opcion: ")
                if not opc_edit.isdigit():
                    print("ERROR, esto no es un digito")
                elif int(opc_edit) < 1 or int(opc_edit) > 3:
                    print("ERROR, este numero no esta en el rango")
                else:
                    input("Pulsar para continuar\n")
                    if opc_edit == "1":
                        edicion_1 = True
                        edicion = False
                    elif opc_edit == "2":
                        edicion_2 = True
                        edicion = False
                    elif opc_edit == "3":
                        edicion = False
                        general = False


            while edicion_1:
                print(menu031)
                for i in dict_characters:
                    lista = []
                    for j in dict_characters[i]["weapons"]:
                        lista.append(dict_weapons[j]["name"])
                    x = str(lista)
                    arma = x.replace("'", "").strip("[]")
                    print(
                        "ID: {}, Nombre: {}, Categoria: {}, Armas: {}, Fuerza: {}, Velocidad: {}, Experiencia: {}".format(
                            i, dict_characters[i]["name"], dict_characters[i]["category"], arma,
                            dict_characters[i]["strength"], dict_characters[i]["speed"],
                            dict_characters[i]["experience"]))
                while True:
                    opc = input("ID a editar: ")
                    if not opc.isdigit():
                        print("ERROR, esto no es un digito")
                    elif int(opc) < 1 or int(opc) > len(dict_characters):
                        print("ERROR, este numero no esta en el rango")
                    else:
                        input("Pulsar para continuar\n")
                        editando = True
                        edicion_1 = False
                        break
            while editando:
                print("Selecciona la caracteristica que quieres editar del personaje ID: {}, Nombre: {}".format(
                    opc, dict_characters[int(opc)]["name"]))
                print("\n1)Nombre\n2)Armas\n3)Atras\n")
                opc_char = input("Opcion: ")
                if not opc_char.isdigit():
                    print("ERROR, esto no es un digito")
                elif int(opc_char) < 1 or int(opc_char) > 3:
                    print("ERROR, este numero no esta en el rango")
                else:
                    if opc_char == "1":
                        edicion_1_1 = True
                        editando = False
                    elif opc_char == "2":
                        edicion_1_2 = True
                        editando = False
                    elif opc_char == "3":
                        input("Pulsar para continuar\n")
                        editando = False
                        edicion = True
                    break

            while edicion_1_1:
                pers_nw_nombre = input("Dime el nuevo nombre: ")
                pregunta = input("Estas seguro que quieres cambiar el nombre de {} a {}?  S/N ".format(dict_characters[int(opc)]["name"],pers_nw_nombre))
                if pregunta == "s" or pregunta == "S":
                    dict_characters[int(opc)]["name"] = pers_nw_nombre
                editando = True
                edicion_1_1 = False


            while edicion_1_2:
                opc = int(opc)
                armas_disponibles = 2
                lista_armasd = []
                lista_armasp = []
                for i in dict_characters[opc]["weapons"]:
                    if dict_weapons[i]["two_hand"] == False:
                        armas_disponibles -= 1
                    elif dict_weapons[i]["two_hand"] == True:
                        armas_disponibles -= 2

                print("Armas disponibles".center(35, "="))
                if armas_disponibles == 0:
                    print("Ninguna".center(35, "-"))
                elif armas_disponibles == 1:
                    for i in dict_weapons:
                        if not dict_weapons[i]["two_hand"]:
                            lista_armasd.append(i)
                            print("{}) {}, Fuerza: {}, Velocidad: {}".format(i, dict_weapons[i]["name"],
                                                                             dict_weapons[i]["strength"],
                                                                             dict_weapons[i]["speed"]))
                elif armas_disponibles == 2:
                    for i in dict_weapons:
                        lista_armasd.append(i)
                        print("{}) {}, Fuerza: {}, Velocidad: {}".format(i, dict_weapons[i]["name"],
                                                                         dict_weapons[i]["strength"],
                                                                         dict_weapons[i]["speed"]))
                print("Armas actuales".center(35, "="))
                for i in dict_characters[opc]["weapons"]:
                    lista_armasp.append(i)
                    print("{}) {}, Fuerza: {}, Velocidad: {}".format(i, dict_weapons[i]["name"],
                                                                     dict_weapons[i]["strength"],
                                                                     dict_weapons[i]["speed"]))

                print("\nInserte:\nID Arma para añadir arma\n0 para salir\n-ID Arma para quitar arma")
                opc_edt_wp = input("->Opcion: ")
                if opc_edt_wp == "0":
                    if len(lista_armasp) != 0:
                        editando = True
                        edicion_1_2 = False
                    else:
                        print("Inserta por lo menos un arma")
                elif len(opc_edt_wp) > 1:
                    if opc_edt_wp[0] == "-":
                        if opc_edt_wp[1:].isdigit():
                            if lista_armasp.count(int(opc_edt_wp[1:])) != 0:
                                if len(dict_characters[opc]["weapons"]) != 0:
                                    dict_characters[opc]["weapons"].remove(int(opc_edt_wp[1:]))
                            else:
                                print("Esas armas no son validas")
                        else:
                            print("Opcion no valida")
                    elif opc_edt_wp.isdigit():
                        if armas_disponibles != 0:
                            dict_characters[opc]["weapons"].append(int(opc_edt_wp))
                    else:
                        print("Opcion no valida")
                elif not opc_edt_wp.isdigit():
                    print("Opcion no valida")
                else:
                    if armas_disponibles != 0:
                        dict_characters[opc]["weapons"].append(int(opc_edt_wp))
                print("\n\n")

            while edicion_2:
                while True:
                    print(menu032)
                    for i in dict_weapons:
                        print("{}) {}, Fuerza: {}, Velocidad: {}".format(i, dict_weapons[i]["name"],
                                                                         dict_weapons[i]["strength"],
                                                                         dict_weapons[i]["speed"]))
                    opc_wp = input("ID arma a editar: ")
                    if not opc_wp.isdigit():
                        print("ERROR, esto no es un digito")
                    elif int(opc_wp) < 1 or int(opc_wp) > len(dict_weapons):
                        print("ERROR, este numero no esta en el rango")
                    else:
                        input("Pulsa para continuar\n")
                        break
                    input("Pulsa para continuar\n")
                while True:
                    print(menu032x)
                    print("Selecciona la caracteristica a editar del arma con ID: {}, Nombre: {}".format(opc_wp,dict_weapons[int(opc_wp)]["name"]))
                    opc_wp_car = input("->Opcion: ")
                    if not opc_wp_car.isdigit():
                        print("ERROR, esto no es un digito")
                    elif int(opc_wp_car) < 1 or int(opc_wp_car) > 4:
                        print("ERROR, este numero no esta en el rango")
                    else:
                        if opc_wp_car == "1":
                            arma_nw_nombre = input("Dime el nuevo nombre: ")
                            pregunta = input("Estas seguro que quieres cambiar el nombre de {} a {}?  S/N ".format(dict_weapons[int(opc_wp)]["name"],arma_nw_nombre))
                            if pregunta == "s" or pregunta == "S":
                                dict_weapons[int(opc_wp)]["name"] = arma_nw_nombre

                        elif opc_wp_car == "2":
                            while True:
                                arma_nw_fuerza = input("Inserta la nueva fuerza: ")
                                if not arma_nw_fuerza.isdigit():
                                    print("ERROR, esto no es un digito")
                                elif int(arma_nw_fuerza) < 1 or int(arma_nw_fuerza) > 9:
                                    print("ERROR, la fuerza no puede ser inferior a 1 o superior a 9")
                                else:
                                    break
                            pregunta = input("Estas seguro que quieres cambiar la fuerza de {} a {} en el arma {}?  S/N ".format(
                                dict_weapons[int(opc_wp)]["strength"],arma_nw_fuerza,dict_weapons[int(opc_wp)]["name"]))
                            if pregunta == "s" or pregunta == "S":
                                dict_weapons[int(opc_wp)]["strength"] = int(arma_nw_fuerza)
                        elif opc_wp_car == "3":
                            while True:
                                arma_nw_velocidad = input("Inserta la nueva velocidad: ")
                                if not arma_nw_velocidad.isdigit():
                                    print("ERROR, esto no es un digito")
                                elif int(arma_nw_velocidad) < 1 or int(arma_nw_velocidad) > 9:
                                    print("ERROR, la fuerza no puede ser inferior a 1 o superior a 9")
                                else:
                                    break
                            pregunta = input(
                                "Estas seguro que quieres cambiar la velocidad de {} a {} en el arma {}?  S/N ".format(
                                    dict_weapons[int(opc_wp)]["speed"], arma_nw_velocidad,
                                    dict_weapons[int(opc_wp)]["name"]))
                            if pregunta == "s" or pregunta == "S":
                                dict_weapons[int(opc_wp)]["speed"] = int(arma_nw_velocidad)
                        elif opc_wp_car == "4":
                            input("Pulsa para continuar\n")
                            edicion = True
                            edicion_2 = False
                            break

    elif opc == "4":
        flag4 = True
        flag41 = False
        flag42 = False
        menu00 = "One Piece".center(30, "*") + "\n\n1)Jugar\n2)Crear\n3)Editar\n4)Listar\n5)Salir\n"
        menu04 = 'Menu04'.center(30,
                                 '*') + "\n\n1)Listar personajes\n2)Listar armas\n3)Listar bando\n4)Listar rango\n5)Salir\n"
        menu041 = 'Menu041'.center(30,
                                   '*') + "\n\n1)Listar por ID\n2)Listar por nombre\n3)Listar por fuerza\n4)Listar por velocidad\n5)Salir\n"
        menu042 = 'Menu042'.center(30,
                                   '*') + "\n\n1)Listar por ID\n2)Listar por nombre\n3)Listar por fuerza\n4)Listar por velocidad\n5)Salir\n"
        menu043 = 'Menu043'.center(30, '*') + '\n\n'
        menu044 = 'Menu044'.center(30, '*') + '\n\n'
        lista0 = list(dict_characters.items())
        lista1 = list(dict_weapons.items())
        while flag4:
            while True:
                print(menu04)
                opc_g = input('Opcion: ')
                if not opc_g.isdigit():
                    print("ERROR, esto no es un digito")
                elif int(opc_g) < 1 or int(opc_g) > 5:
                    print("ERROR, este numero no esta en el rango")
                else:
                    break
                input("Pulsar para continuar\n")
            if opc_g == "1":
                flag41 = True
                while flag41:
                    listaIds = list(dict_characters.keys())
                    while True:
                        print(menu041)
                        opc_p = input('Opcion: ')
                        if not opc_p.isdigit():
                            print("ERROR, esto no es un digito")
                        elif int(opc_p) < 1 or int(opc_p) > 5:
                            print("ERROR, este numero no esta en el rango")
                        else:
                            break
                        input("Pulsa ENTER para continuar")
                    if opc_p == '1':  # listar personajes por id
                        for i in range(len(listaIds) - 1):
                            for j in range(len(listaIds) - 1 - i):
                                if listaIds[j] < listaIds[j + 1]:
                                    listaIds[j], listaIds[j + 1] = listaIds[j + 1], listaIds[j]
                        print('=' * 24 + 'Personaje listado por ID' + '=' * 23)
                        print('ID'.ljust(10), 'name'.ljust(15), "category".ljust(10), 'strength'.ljust(10),
                              'speed'.ljust(10),
                              'experience'.ljust(16))
                        print('*' * 71)
                        for key in listaIds:
                            plusStrenght = 0
                            plusSpeed = 0
                            for i in range(len(dict_characters[key]["weapons"])):
                                plusStrenght += dict_weapons[dict_characters[key]["weapons"][i]]["strength"]
                                plusSpeed += dict_weapons[dict_characters[key]["weapons"][i]]["speed"]
                            print(str(key).ljust(10), dict_characters[key]["name"].ljust(15),
                                  str(dict_characters[key]["category"]).ljust(10),
                                  str(dict_characters[key]["strength"] + plusStrenght).center(13),
                                  str(dict_characters[key]["speed"] + plusSpeed).ljust(10),
                                  str(dict_characters[key]["experience"]).ljust(16))
                        input("Pulsa ENTER para continuar")
                    elif opc_p == '2':  # listar personajes por nombre
                        print('=' * 22 + 'Personaje listado por nombre' + '=' * 21)
                        print('ID'.ljust(10), 'name'.ljust(15), "category".ljust(10), 'strength'.ljust(10),
                              'speed'.ljust(10),
                              'experience'.ljust(16))
                        print('*' * 71)
                        for i in range(len(dict_characters) - 1):
                            for j in range(len(dict_characters) - 1 - i):
                                if dict_characters[listaIds[j]]['name'] > dict_characters[listaIds[j + 1]]['name']:
                                    listaIds[j], listaIds[j + 1] = listaIds[j + 1], listaIds[j]
                        for key in listaIds:
                            plusStrenght = 0
                            plusSpeed = 0
                            for i in range(len(dict_characters[key]["weapons"])):
                                plusStrenght += dict_weapons[dict_characters[key]["weapons"][i]]["strength"]
                                plusSpeed += dict_weapons[dict_characters[key]["weapons"][i]]["speed"]
                            print(str(key).ljust(10), dict_characters[key]["name"].ljust(15),
                                  str(dict_characters[key]["category"]).ljust(10),
                                  str(dict_characters[key]["strength"] + plusStrenght).center(13),
                                  str(dict_characters[key]["speed"] + plusSpeed).ljust(10)
                                  , str(dict_characters[key]["experience"]).ljust(16))
                        input("Pulsa ENTER para continuar")
                    elif opc_p == '3':  # listar personajes por fuerza
                        print('=' * 22 + 'Personaje listado por fuerza' + '=' * 21)
                        print('ID'.ljust(10), 'name'.ljust(15), "category".ljust(10), 'strength'.ljust(10),
                              'speed'.ljust(10),
                              'experience'.ljust(16))
                        print('*' * 71)
                        for i in range(len(listaIds) - 1):
                            for j in range(len(listaIds) - 1 - i):
                                plusP1 = 0
                                plusP2 = 0
                                for t in range(len(dict_characters[listaIds[j]]["weapons"])):
                                    plusP1 += dict_weapons[dict_characters[listaIds[j]]["weapons"][t]]["strength"]
                                for t in range(len(dict_characters[listaIds[j + 1]]["weapons"])):
                                    plusP2 += dict_weapons[dict_characters[listaIds[j + 1]]["weapons"][t]]["strength"]

                                if dict_characters[listaIds[j]]["strength"] + plusP1 > dict_characters[listaIds[j + 1]][
                                    "strength"] + plusP2:
                                    listaIds[j], listaIds[j + 1] = listaIds[j + 1], listaIds[j]
                        for key in listaIds:
                            plusStrenght = 0
                            plusSpeed = 0
                            for i in range(len(dict_characters[key]["weapons"])):
                                plusStrenght += dict_weapons[dict_characters[key]["weapons"][i]]["strength"]
                                plusSpeed += dict_weapons[dict_characters[key]["weapons"][i]]["speed"]
                            print(str(key).ljust(10), dict_characters[key]["name"].ljust(15),
                                  str(dict_characters[key]["category"]).ljust(10),
                                  str(dict_characters[key]["strength"] + plusStrenght).center(13),
                                  str(dict_characters[key]["speed"] + plusSpeed).ljust(10)
                                  , str(dict_characters[key]["experience"]).ljust(16))
                        input("Pulsa ENTER para continuar")
                    elif opc_p == '4':  # listar personajes por velocidad
                        print('=' * 20 + 'Personaje listado por velocidad' + '=' * 20)
                        print('ID'.ljust(10), 'name'.ljust(15), "category".ljust(10), 'strength'.ljust(10),
                              'speed'.ljust(10),
                              'experience'.ljust(16))
                        print('*' * 71)
                        for i in range(len(listaIds) - 1):
                            for j in range(len(listaIds) - 1 - i):
                                plusP1 = 0
                                plusP2 = 0
                                for t in range(len(dict_characters[listaIds[j]]["weapons"])):
                                    plusP1 += dict_weapons[dict_characters[listaIds[j]]["weapons"][t]]["speed"]
                                for t in range(len(dict_characters[listaIds[j + 1]]["weapons"])):
                                    plusP2 += dict_weapons[dict_characters[listaIds[j + 1]]["weapons"][t]]["speed"]

                                if dict_characters[listaIds[j]]["speed"] + plusP1 > dict_characters[listaIds[j + 1]][
                                    "speed"] + plusP2:
                                    listaIds[j], listaIds[j + 1] = listaIds[j + 1], listaIds[j]
                        for key in listaIds:
                            plusStrenght = 0
                            plusSpeed = 0
                            for i in range(len(dict_characters[key]["weapons"])):
                                plusStrenght += dict_weapons[dict_characters[key]["weapons"][i]]["strength"]
                                plusSpeed += dict_weapons[dict_characters[key]["weapons"][i]]["speed"]
                            print(str(key).ljust(10), dict_characters[key]["name"].ljust(15),
                                  str(dict_characters[key]["category"]).ljust(10),
                                  str(dict_characters[key]["strength"] + plusStrenght).center(13),
                                  str(dict_characters[key]["speed"] + plusSpeed).ljust(10)
                                  , str(dict_characters[key]["experience"]).ljust(16))
                        input("Pulsa ENTER para continuar")
                    elif opc_p == '5':
                        flag41 = False
            if opc_g == "2":
                flag4 = False
                flag42 = True
                while flag42:
                    listaIdsarmas = list(dict_weapons.keys())
                    while True:
                        print(menu042)
                        opc_a = input('Opcion: ')
                        if not opc_a.isdigit():
                            print("ERROR, esto no es un digito")
                        elif int(opc_a) < 1 or int(opc_a) > 5:
                            print("ERROR, este numero no esta en el rango")
                        else:
                            break
                        input("Pulsar para continuar\n")
                    if opc_a == '1':  # listar armas por id
                        print('=' * 18 + 'Armas listadas por ID' + '=' * 18)
                        print('ID'.ljust(10), 'name'.ljust(15), 'strength'.ljust(10),
                              'speed'.ljust(10),
                              'two hands'.ljust(16))
                        print('*' * 59)
                        for i in range(len(listaIdsarmas) - 1):
                            for j in range(len(listaIdsarmas) - 1 - i):
                                if listaIdsarmas[j] < listaIdsarmas[j + 1]:
                                    listaIdsarmas[j], listaIdsarmas[j + 1] = listaIdsarmas[j + 1], listaIdsarmas[j]
                        for key in listaIdsarmas:
                            print(str(key).ljust(10), dict_weapons[key]["name"].ljust(15),
                                  str(dict_weapons[key]["strength"]).center(13),
                                  str(dict_weapons[key]["speed"]).ljust(10),
                                  str(dict_weapons[key]["two_hand"]).ljust(16))
                        input("Pulsa ENTER para continuar")
                    elif opc_a == '2':  # listar arma por nombre
                        print('=' * 18 + 'Arma listado por nombre' + '=' * 18)
                        print('ID'.ljust(10), 'name'.ljust(15), 'strength'.ljust(10),
                              'speed'.ljust(10),
                              'two hands'.ljust(16))
                        print('*' * 59)
                        for i in range(len(listaIdsarmas) - 1):
                            for j in range(len(listaIdsarmas) - 1 - i):
                                if dict_weapons[listaIdsarmas[j]]['name'] > dict_weapons[listaIdsarmas[j + 1]]['name']:
                                    listaIdsarmas[j], listaIdsarmas[j + 1] = listaIdsarmas[j + 1], listaIdsarmas[j]
                        for key in listaIdsarmas:
                            print(str(key).ljust(10), dict_weapons[key]["name"].ljust(15),
                                  str(dict_weapons[key]["strength"]).center(13),
                                  str(dict_weapons[key]["speed"]).ljust(10),
                                  str(dict_weapons[key]["two_hand"]).ljust(16))
                        input("Pulsa ENTER para continuar")
                    elif opc_a == '3':  # listar armas por fuerza
                        print('=' * 20 + 'Arma listada por fuerza' + '=' * 20)
                        print('ID'.ljust(10), 'name'.ljust(15), 'strength'.ljust(10),
                              'speed'.ljust(10),
                              'two hand'.ljust(16))
                        print('*' * 59)
                        for i in range(len(listaIdsarmas) - 1):
                            for j in range(len(listaIdsarmas) - 1 - i):
                                if dict_weapons[listaIdsarmas[j]]['strength'] > dict_weapons[listaIdsarmas[j + 1]][
                                    'strength']:
                                    listaIdsarmas[j], listaIdsarmas[j + 1] = listaIdsarmas[j + 1], listaIdsarmas[j]
                        for key in listaIdsarmas:
                            print(str(key).ljust(10), dict_weapons[key]["name"].ljust(15),
                                  str(dict_weapons[key]["strength"]).center(13),
                                  str(dict_weapons[key]["speed"]).ljust(10),
                                  str(dict_weapons[key]["two_hand"]).ljust(16))
                        input("Pulsa ENTER para continuar")
                    elif opc_a == '4':  # listar armas por velocidad
                        print('=' * 20 + 'Arma listada por velocidad' + '=' * 20)
                        print('ID'.ljust(10), 'name'.ljust(15), 'strength'.ljust(10),
                              'speed'.ljust(10),
                              'two hand'.ljust(16))
                        print('*' * 59)
                        for i in range(len(listaIdsarmas) - 1):
                            for j in range(len(listaIdsarmas) - 1 - i):
                                if dict_weapons[listaIdsarmas[j]]['speed'] > dict_weapons[listaIdsarmas[j + 1]][
                                    'speed']:
                                    listaIdsarmas[j], listaIdsarmas[j + 1] = listaIdsarmas[j + 1], listaIdsarmas[j]
                        for key in listaIdsarmas:
                            print(str(key).ljust(10), dict_weapons[key]["name"].ljust(15),
                                  str(dict_weapons[key]["strength"]).center(13),
                                  str(dict_weapons[key]["speed"]).ljust(10),
                                  str(dict_weapons[key]["two_hand"]).ljust(16))
                        input("Pulsa ENTER para continuar")
                    elif opc_a == '5':
                        flag42 = False
                        flag4 = True
            elif opc_g == '3':
                print(menu043)
                print('Aun se esta configurando')
                input('enter para continuar')
            elif opc_g == '4':
                print(menu044)
                print('Aun se esta configurando')
                input('enter para continuar')
            elif opc_g == '5':
                flag4 = False
                break
    elif opc == "5":
        print("Saliendo...")
        break