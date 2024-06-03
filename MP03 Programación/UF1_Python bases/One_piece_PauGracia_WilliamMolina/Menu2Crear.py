import random
dict_characters = { 1 : {"name" : "Luffy","category": 1, "weapons": [1, 1],"strength" : 6, "speed" :7,"experience": 0},
                    2 : {"name" : "Zoro","category": 1, "weapons" : [4],"strength" : 5, "speed" : 6,"experience":0},
                    3 : {"name" : "Sanji", "category" : 1, "weapons" : [1,3],"strength" : 4, "speed" :6,"experience": 0 },
                    4 : {"name" : "Buggy", "category" : 2, "weapons" : [3], "strength" : 2, "speed" : 4, "experience" : 0},
                    5 : {"name" : "Mr3", "category" : 2, "weapons" : [5], "strength" : 3, "speed" : 2, "experience": 0},
                    6 : {"name" : "Xebec", "category" : 3, "weapons" : [1,3], "strength" : 6, "speed" : 5,"experience" : 0},
                    7 : {"name" : "Kaido", "category" : 3, "weapons" : [4], "strength" : 8, "speed" : 3,"experience" : 0},
                    8 : {"name" : "Mama grande", "category" : 3, "weapons" : [5], "strength" : 7, "speed" : 1,"experience" : 0},
                    9 : {"name" : "Akainu", "category" : 4, "weapons" : [2], "strength" : 6, "speed" : 4,"experience" : 0},
                    10 : {"name" : "Kizaru", "category" : 4, "weapons" : [1,3], "strength" : 5, "speed" : 8,"experience" : 0},
                    11 : {"name" : "Fujitora", "category" : 4, "weapons" : [5], "strength" : 5, "speed" : 4,"experience" : 0},
                    12 : {"name" : "Garp", "category" : 5, "weapons" : [2], "strength" : 6, "speed" : 3,"experience" : 0},
                    13 : {"name" : "Smoker", "category" : 5, "weapons" : [5], "strength" : 5, "speed" : 5,"experience" : 0},
                    14 : {"name" : "Koby", "category" : 6, "weapons" : [4], "strength" : 3, "speed" : 4,"experience" : 0},
                    15 : {"name" : "Tashigi", "category" : 6, "weapons" : [3], "strength" : 4, "speed" : 4,"experience" : 0},
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
dict_ranks = { 1: {"name" : "Admiral","members": [9,10,11]},
               2: {"name" : "ViceAdmiral","members": [12,13]},
               3: {"name": "Lieutenant","members": [14,15]}
}
dict_categorys = {1:"Straw hat",2:"Pirates Buggy",3:"Pirates Rocks",4:"Admiral",5:"ViceAdmiral",6:"Lieutenant"}

cabecera2=("***************** Menu 2 - Create*******************\n"+"1)Create Character\n"+"2)Create Weapon\n"+"3)Back\n")

seleccionArma = True
crearCharacter = True
saveCharacter = True
saveWeapon = True

while True:

    print(cabecera2)
    opcion = input("Option >\n")
    if opcion.isdigit():
        opcion = int(opcion)

        if opcion == 1:#CREAR JUGADOR
            name = ""
            cat = 0
            id = len(dict_characters)+1
            weapons = []
            strenght = 0
            speed = 0


            print("****** Menu 21 - Create Character**")
            if name == "" and cat == 0:

                name = input("Name of the new character:\n")
                while crearCharacter:
                    print("SIde of the new character:\n"+"1)Marine\n"+"2)Pirates")
                    opcion = input("Option >\n")
                    if opcion.isdigit():
                        opcion = int(opcion)

                        if opcion == 1:

                            print(
                                "Range or crew of the new character:\n" + "1) Admirant\n" + "2) Viceadmirant\n" +
                                "3)Lieutenant\n")
                            opcion = input("Option >\n")

                            if opcion.isdigit():
                                opcion = int(opcion)

                                if opcion == 1:#admirant
                                    cat = 4
                                    crearCharacter = False


                                elif opcion == 2:#viceadmirant
                                    cat = 5
                                    crearCharacter = False


                                elif opcion == 3:#Lieutenant
                                    cat = 6
                                    crearCharacter = False


                                else:
                                    print("Opción no válida\n")
                            else:
                                print("opción no valida")


                        elif opcion == 2:

                                print(
                                    "Range or crew of the new character:\n" + "1) Straw hat\n" + "2) Pirates Buggy\n" + "3) Pirates Rocks\n")
                                opcion = input("Option >\n")

                                if opcion.isdigit():
                                    opcion = int(opcion)

                                    if opcion == 1:
                                        cat = 1
                                        crearCharacter = False

                                    elif opcion == 2:
                                        cat = 2
                                        crearCharacter = False

                                    elif opcion == 3:
                                        cat = 3
                                        crearCharacter = False

                                    else:
                                        print("Opción no válida\n")
                                else:
                                    print("Introduce una opcion numerica\n")
                        else:
                            print("Opción no válida\n")

                    else:
                        print("Introduce una opcion numerica\n")


            while seleccionArma:
                cadenaAvalible = "="*10 +"Available Weapons"+"="*10 +"\n"
                cadenaInUse = "="*10 +"Character Weapons"+"="*10 + "\n"

                if len(weapons) == 0: #MOSTRAR PRINT SIN ARMAS
                    cadenaInUse += "\n"+"-"*15 + " None " + "-"*15 + "\n"*4
                    for weapon in range(len(dict_weapons)):
                        cadenaAvalible += str(weapon+1) + ") name " + dict_weapons[weapon+1]["name"]+ " Strength "+ str(dict_weapons[weapon+1]["strength"])+ \
                        " Speed "+ str(dict_weapons[weapon+1]["speed"]) + "\n"

                if len(weapons) >= 1: #MOSTRAR PRINT ARMAS
                    if dict_weapons[weapons[0]]["two_hand"] == True or len(weapons)== 2: #COMPROBAR QUE ARMA TENGA 2 MANOS 0 QUE SEAN 2 DE UNA MANO
                        cadenaAvalible += "-"*15 + " None " + "-"*15 + "\n"*4

                    if dict_weapons[weapons[0]]["two_hand"] == False and len(weapons)<=1: #SEGUNDA COMPROBACIÓN DE ARMA 2 MANOS
                        for weapon in range(len(dict_weapons)):
                            if dict_weapons[weapon+1]["two_hand"] == False:#PASAR ARMAS 2 MANOS A FALSO APRA QUE NO SE MUESTREN
                                cadenaAvalible += str(weapon+1) + ") name " + dict_weapons[weapon+1]["name"]+ " Strength "+ str(dict_weapons[weapon+1]["strength"])+ \
                                " Speed "+ str(dict_weapons[weapon+1]["speed"]) + "\n"

                    for weapon in range(len(weapons)): #MUESTRA ARMAS PERSONAJES
                        cadenaInUse += str(weapons[weapon]) + ") name " + dict_weapons[weapons[weapon]]["name"]+ " Strength "+ str(dict_weapons[weapons[weapon]]["strength"])+ \
                        " Speed "+ str(dict_weapons[weapons[weapon]]["speed"]) + "\n"

                cabecera2 = "Add Weapons:\n" + "- Enter Id) to add Weapon\n"+"- Enter 0 to finish add weapons\n"+\
                            "- Enter  '-Id' to delete weapon in character"
                while True:

                    print(cadenaAvalible)
                    print(cadenaInUse)
                    print(cabecera2)
                    deleteWeapon = False
                    opcion = input("Option >\n")
                    if opcion.isspace()or opcion == "": #EVITAR QUE PETE CON ENTER
                        print("Introduce una opcion numerica\n")
                    elif opcion[0] == "-":#ELIMINAR ARMA COMPROBANDO SI TIENE "-"
                        if opcion[1:].isdigit(): #Comprueba la id de arma conforme existe
                            opcion = int(opcion[1:])
                            deleteWeapon = True
                            if opcion in weapons:#Salir del While
                                break
                        else:
                            print("Opción no válida.\n")
                    elif opcion.isdigit():
                        opcion = int(opcion)
                        if opcion == 0:
                            seleccionArma = False
                            break
                        if opcion in range(len(dict_weapons)+1): #Comprueba la id de arma conforme existe

                            if len(weapons) == 0:
                                break
                            elif len(weapons) == 2 or dict_weapons[weapons[0]]["two_hand"] == True:
                                 print("tienes mas de dos armas o un arma de dos manos\n")
                            elif len(weapons) >= 0:
                                if dict_weapons[opcion]["two_hand"] == False:
                                    break

                        else:
                            print("Opción no válida.\n")
                    else:
                        print("Introduce una opcion numerica\n")


                if deleteWeapon == True:
                    if len(weapons) == 1:
                        weapons.remove(opcion)# Eliminar un elemento
                    else:
                        for i in range(len(weapons)):#recorre weapons para eliminar arma
                            if opcion == weapons[i]:
                                weapons.remove(opcion)
                                break
                if opcion != 0 and deleteWeapon == False:
                    weapons.append(opcion)


            strenght = random.randint(1,9)
            speed = random.randint(1,9)
            cadena = ""
            for key in weapons:#MOSTRAR ARMAS PERSONAJE
                cadena += dict_weapons[key]["name"]+", "
                cadena = cadena[: len(cadena)-2]

            while saveCharacter:
                cabeceraPersonaje = "The new player will be:\n"+"\n"+f"Name: {name}\n"+ f"Category: {dict_categorys[cat]}\n" + f"Weapons:{cadena}\n"+\
                f"Strength:{strenght}\n"+f"Speed:{speed}\n"+f"Experience: 0\n"
                print(cabeceraPersonaje)
                save = input("Save this player? S/N")
                if save == "s" or save == "S":
                    dict_characters[id] = {"name" : name,"category": cat, "weapons": weapons ,"strength" : strenght, "speed" : speed,"experience": 0}
                    saveCharacter = False


                elif save == "n" or save == "N":
                    saveCharacter = False

                else:
                    print("Invalid option")
            break

        elif opcion == 2:#CREAR ARMA
            id_weapon = len(dict_weapons)+1

            print("****** Menu 22 - Create Weapon**")
            nameWeapon = input("Name of the new weapon:\n")
            print("Weapon strenght: 1-9 \n")
            strength = int(input("->Strenght: "))

            if not strength in range(10) or strength == 0: #VALOR VALIDO
                print("==== Invalid Option ====")
                input("Press Enter to continue")
                strength = int(input("->Strenght: "))

            print("Weapon speed: 1-9 \n")
            speed = int(input("->Speed: "))

            if not speed in range(10) or speed == 0:
                print("==== Invalid Option ====\n")
                input("Press Enter to continue\n")
                speed = int(input("->Speed: "))

            print("\nKind of weapon\n1)One hand\n2)Two hand")#TIPO DE ARMA
            opcion = input("Option >\n")
            if opcion.isdigit():
                opcion = int(opcion)
                if opcion == 1:
                    two_hands = False

                elif opcion == 2:
                    two_hands = True

                else:
                    print("Opción no válida.\n")
            else:
                print("Opción no válida\n")

            while saveWeapon:
                cabeceraArma = f"Name: {nameWeapon}\n"+f"Strength:{strength}\n"+f"Speed:{speed}\n"+f"Two hands type: {two_hands}\n"
                print(cabeceraArma)

                save = input("Save this weapon? S/N\n")

                if save == "s" or save == "S":
                    dict_weapons[id_weapon] = {"name" : nameWeapon,"strength" : strength, "speed" : speed,f"two_hand" : two_hands}
                    saveWeapon = False

                elif save == "n" or save == "N":
                    saveWeapon = False
            break


        elif opcion == 3:
            print("Cerrando programa...")
            break



        else:
            print("Opción no válida. Por favor, elige una opción válida.\n")
    else:
        print("Introduce una opcion numerica\n")







# opcion = input("Option >\n")
#     if opcion.isdigit():
#         opcion = int(opcion)
#
#         if opcion == 1:#CREAR JUGADOR
#         else:
#             print("Opción no válida. Por favor, elige una opción válida.\n")
#     else:
#         print("Introduce una opcion numerica\n")



# #LISTAR DICCIONARIO PRINCIPAL
# lista = list(dict_characters.keys())
# # print (lista)
# for key in lista:
#     for item in dict_characters[key]:
#         if item == "weapons":
#
#             cadena = ""
#             for weapon in dict_characters[key]["weapons"]:
#                 cadena += dict_weapons[weapon]["name"]+", "
#             cadena = cadena[: len(cadena)-2]
#
#             print("ID: "+ str(key) + " Name " + dict_characters[key]["name"] + ", Category: " + dict_categorys[dict_characters[key]["category"]]+
#                   ", Weapons: "+ cadena +" Strength ,"+ str(dict_characters[key]["strength"]) + " Speed "+ str(dict_characters[key]["speed"]) + " Exp " + str(dict_characters[key]["experience"]))
