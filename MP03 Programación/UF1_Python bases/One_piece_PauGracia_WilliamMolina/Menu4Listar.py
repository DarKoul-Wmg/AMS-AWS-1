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

menu04 = "============Menu04 (List)=============\n\n1)List Characters\n2)List Weapons\n3)List Side\n4)List Range\n5)Go Back"

menu041 = "\======Menu041 (List Characters)======\n\n1)List by ID\n2)List by Name\n3)List by Strength\n4)List by Speed\n5)Go Back"

menu042 = "======Menu041 (List Weapons)======\n\n1)List by ID\n2)List by Name\n3)List by Strength\n4)List by Speed\n5)Go Back"
salir = False
salir2 = False

flg_00 = True
flg_03 = True#Weapon
flg_02 = False
flg_04 = False#Character


 ######################################menu04####################
while flg_02:
    print(menu04)

    opc = input("->Options: " + "\n")
    # comprobar opciones menu correctas
    if not opc.isdigit():
        print("wrong option")
    elif not int(opc) in range(1, 7):
        print("wrong option")

    elif int(opc) == 1:
        flg_03 = True
        flg_02 = False
        # para menu041
    elif int(opc) == 2:
        flg_04 = True
        flg_02 = False
        # para menu042
    elif int(opc) == 5:
        flg_00 = True
        flg_02 = False

        # atras
#############menu041####################
while flg_03:
    print(menu042)

    opc = input("->Options: " + "\n")
    # comprobar opciones menu correctas
    if not opc.isdigit():
        print("wrong option")
    elif not int(opc) in range(1, 6):
        print("wrong option")

    elif int(opc) == 5:
        flg_00 = True
        flg_04 = False
        # atras


    elif int(opc) == 1:#ID
        table = ""
        menuWeaponsID = "=" * 19 + "Weapons ordered by Id" + "=" * 19 + "\n" + "ID".ljust(10) + "Name".ljust(15) \
                       + "Strength".ljust(13) + "Speed".ljust(14)+ "\n" + "*" * 62
        print(menuWeaponsID)

        listaID = list(dict_weapons.keys())

        for pasada in range(len(listaID)-1):#Ordenar id
            for j in range(len(listaID)-1-pasada):
                if listaID[j] > listaID[j+1]:
                    opc = listaID[j]
                    listaID[j] = listaID[j+1]
                    listaID[j+1] = opc

        for j in listaID:
            for i in range(1,len(dict_weapons)+1):
                if i == j:#Igualar lista ordenada con id diccionario para sacar ID
                    table += f"{str(i)}".ljust(10) + dict_weapons[i]["name"].ljust(13) + " " + str(dict_weapons[i]["strength"]).rjust(9) + \
                         " " + str(dict_weapons[i]["speed"]).rjust(9)+"\n"
        print(table)
        print("\n\n")

    elif int(opc) == 2:#Name

        table = ""
        menuWeaponsName = "=" * 19 + "Weapons ordered by Speed" + "=" * 19 + "\n" + "ID".ljust(10) + "Name".ljust(15) \
                       + "Strength".ljust(13) + "Speed".ljust(14) + "\n" + "*" * 62
        print(menuWeaponsName)
        listaID = []
        listaName = []
        for i in range(1,len(dict_weapons)+1):
            listaID.append(i)
            listaName.append(dict_weapons[i]["name"])

        for pasada in range(len(listaName)-1):#Ordenar id en funcion de speed
            for j in range(len(listaName)-1-pasada):
                if listaName[j] > listaName[j+1]:
                    listaName[j],listaName[j+1]=listaName[j+1] ,listaName[j]
                    listaID[j],listaID[j+1]=listaID[j+1] ,listaID[j]

        for j in listaID:
            for i in range(1,len(dict_weapons)+1):
                if i == j:#Igualar lista ordenada con id diccionario para sacar ID
                    table += f"{str(i)}".ljust(10) + dict_weapons[i]["name"].ljust(13) + " " + str(dict_weapons[i]["strength"]).rjust(9) + \
                         " " + str(dict_weapons[i]["speed"]).rjust(9)+"\n"
        print(table)
        print("\n\n")

    elif int(opc) == 3:#Strength
        table = ""
        menuWeaponsStrength = "=" * 19 + "Weapons ordered by Strength" + "=" * 19 + "\n" + "ID".ljust(10) + "Name".ljust(15) \
                       + "Strength".ljust(13) + "Speed".ljust(14) + "\n" + "*" * 62
        print(menuWeaponsStrength)
        listaID = []
        listaStrength = []
        for i in range(1,len(dict_weapons)+1):
            listaID.append(i)
            listaStrength.append(dict_weapons[i]["strength"])

        for pasada in range(len(listaStrength)-1):#Ordenar id en funcion de strength
            for j in range(len(listaStrength)-1-pasada):
                if listaStrength[j] < listaStrength[j+1]:
                    listaStrength[j],listaStrength[j+1]=listaStrength[j+1] ,listaStrength[j]
                    listaID[j],listaID[j+1]=listaID[j+1] ,listaID[j]

        for j in listaID:
            for i in range(1,len(dict_weapons)+1):
                if i == j:#Igualar lista ordenada con id diccionario para sacar ID
                    table += f"{str(i)}".ljust(10) + dict_weapons[i]["name"].ljust(13) + " " + str(dict_weapons[i]["strength"]).rjust(9) + \
                         " " + str(dict_weapons[i]["speed"]).rjust(9)+"\n"
        print(table)
        print("\n\n")

    elif int(opc) == 4:#Speed
        table = ""
        menuWeaponsSpeed = "=" * 19 + "Weapons ordered by Speed" + "=" * 19 + "\n" + "ID".ljust(10) + "Name".ljust(15) \
                       + "Strength".ljust(13) + "Speed".ljust(14) + "\n" + "*" * 62
        print(menuWeaponsSpeed)
        listaID = []
        listaSpeed = []
        for i in range(1,len(dict_weapons)+1):
            listaID.append(i)
            listaSpeed.append(dict_weapons[i]["speed"])

        for pasada in range(len(listaSpeed)-1):#Ordenar id en funcion de speed
            for j in range(len(listaSpeed)-1-pasada):
                if listaSpeed[j] < listaSpeed[j+1]:
                    listaSpeed[j],listaSpeed[j+1]=listaSpeed[j+1] ,listaSpeed[j]
                    listaID[j],listaID[j+1]=listaID[j+1] ,listaID[j]

        for j in listaID:
            for i in range(1,len(dict_weapons)+1):
                if i == j:#Igualar lista ordenada con id diccionario para sacar ID
                    table += f"{str(i)}".ljust(10) + dict_weapons[i]["name"].ljust(13) + " " + str(dict_weapons[i]["strength"]).rjust(9) + \
                         " " + str(dict_weapons[i]["speed"]).rjust(9)+"\n"
        print(table)
        print("\n\n")


#############menu042####################
while flg_04:
    print(menu041)

    opc = input("->Options: " + "\n")
    # comprobar opciones menu correctas
    if not opc.isdigit():
        print("wrong option")
    elif not int(opc) in range(1, 6):
        print("wrong option")
    elif int(opc) == 5:
        flg_00 = True
        flg_03 = False

        # atras
    elif int(opc) == 1:
        #LISTAR ID ============
        table = ""
        menuCharactersID = "=" * 19 + "Characters ordered by Id" + "=" * 19 + "\n" + "ID".ljust(10) + "Name".ljust(15) \
                       + "Strength".ljust(13) + "Speed".ljust(14) + "Experience\n" + "*" * 62
        print(menuCharactersID)

        listaID = list(dict_characters.keys())

        for pasada in range(len(listaID)-1):
            for key in range(len(listaID)-1-pasada):
                if listaID[key] > listaID[key+1]:
                    opc = listaID[key]
                    listaID[key] = listaID[key+1]
                    listaID[key+1] = opc

        for i in listaID:
            #RECUENTO DE LOS DIFERENTES VALORES DE CADA PARÁMETRO
            total_strength = dict_characters[i]["strength"]
            total_speed = dict_characters [i]["speed"]

            for j in dict_characters[i]["weapons"]:#BUCLE DE SUMA TOTAL
                total_strength += dict_weapons[j]["strength"]
                total_speed += dict_weapons[j]["speed"]

            table += f"{i}".ljust(10) + dict_characters[i]["name"].ljust(13) + " " + str(total_strength).rjust(9) + \
                 " " + str(total_speed).rjust(9) +" "+ str(dict_characters[i]["experience"]).rjust(18)+"\n"
        print(table)
        print("\n\n")

    elif int(opc) == 2:
        #LISTAR Name ============
        table = ""
        menuCharactersName = "=" * 19 + "Characters ordered by Name" + "=" * 19 + "\n" + "ID".ljust(10) + "Name".ljust(15) \
                       + "Strength".ljust(13) + "Speed".ljust(14) + "Experience\n" + "*" * 62
        print(menuCharactersName)
        listaName = []
        for i in dict_characters:
            listaName.append(dict_characters[i]["name"])

        for pasada in range(len(listaName)-1):
            for name in range(len(listaName)-1-pasada):
                if listaName[name] > listaName[name+1]:
                    opc = listaName[name]
                    listaName[name] = listaName[name+1]
                    listaName[name+1] = opc

        for i in listaName:#RECUENTO DE LOS DIFERENTES VALORES DE CADA PARÁMETRO
            for j in range(1,len(dict_characters)+1):#
                if dict_characters[j]["name"] == i:
                    total_strength = dict_characters[j]["strength"]
                    total_speed = dict_characters [j]["speed"]

                    for k in dict_characters[j]["weapons"]:#BUCLE DE SUMA TOTAL
                        total_strength += dict_weapons[k]["strength"]
                        total_speed += dict_weapons[k]["speed"]

                    table += f"{str(j)}".ljust(10) + dict_characters[j]["name"].ljust(13) + " " + str(total_strength).rjust(9) + \
                         " " + str(total_speed).rjust(9) +" "+ str(dict_characters[j]["experience"]).rjust(18)+"\n"
        print(table)
        print("\n\n")

    elif int(opc) == 3:
        table = ""
        menuCharactersStrength = "=" * 19 + "Characters ordered by Strength" + "=" * 19 + "\n" + "ID".ljust(10) + "Name".ljust(15) \
                       + "Strength".ljust(13) + "Speed".ljust(14) + "Experience\n" + "*" * 62
        print(menuCharactersStrength)
        listaID = []
        for i in range(1,len(dict_characters)+1):
            listaID.append (i)
        listaStrength = []
        for i in listaID:
            #RECUENTO DE LOS DIFERENTES VALORES DE CADA PARÁMETRO
            total_strength = dict_characters[i]["strength"]
            for j in dict_characters[i]["weapons"]:#BUCLE DE SUMA TOTAL
                total_strength += dict_weapons[j]["strength"]
            listaStrength.append(total_strength)


        for pasada in range(len(listaStrength)-1):
            for j in range(len(listaStrength)-1-pasada):
                if listaStrength[j] < listaStrength[j+1]:
                    listaStrength[j],listaStrength[j+1]=listaStrength[j+1] ,listaStrength[j]
                    listaID[j],listaID[j+1]=listaID[j+1] ,listaID[j]

        for j in listaID:#RECUENTO DE LOS DIFERENTES VALORES DE CADA PARÁMETRO
            for i in range(1,len(dict_characters)+1):
                if i == j:
                    total_strength = dict_characters[i]["strength"]
                    total_speed = dict_characters [i]["speed"]
                    for k in dict_characters[i]["weapons"]:#BUCLE DE SUMA TOTAL
                        total_strength += dict_weapons[k]["strength"]
                        total_speed += dict_weapons[k]["speed"]
                    table += f"{str(i)}".ljust(10) + dict_characters[i]["name"].ljust(13) + " " + str(total_strength).rjust(9) + \
                         " " + str(total_speed).rjust(9) +" "+ str(dict_characters[i]["experience"]).rjust(18)+"\n"
        print(table)
        print("\n\n")


    elif int(opc) == 4:

        table = ""

        menuCharactersSpeed = "=" * 19 + "Characters ordered by Speed" + "=" * 19 + "\n" + "ID".ljust(

            10) + "Name".ljust(15) \
                              + "Strength".ljust(13) + "Speed".ljust(14) + "Experience\n" + "*" * 62

        print(menuCharactersSpeed)

        listaID = []

        for i in range(1, len(dict_characters) + 1):
            listaID.append(i)

            listaSpeed = []

        for i in listaID:

            # RECUENTO DE LOS DIFERENTES VALORES DE CADA PARÁMETRO

            total_speed = dict_characters[i]["speed"]

            for j in dict_characters[i]["weapons"]:  # BUCLE DE SUMA TOTAL

                total_speed += dict_weapons[j]["speed"]

            listaSpeed.append(total_speed)

        for pasada in range(len(listaSpeed) - 1):

            for j in range(len(listaSpeed) - 1 - pasada):

                if listaSpeed[j] < listaSpeed[j + 1]:
                    listaSpeed[j], listaSpeed[j + 1] = listaSpeed[j + 1], listaSpeed[j]

                    listaID[j], listaID[j + 1] = listaID[j + 1], listaID[j]

        for j in listaID:  # RECUENTO DE LOS DIFERENTES VALORES DE CADA PARÁMETRO

            for i in range(1, len(dict_characters) + 1):

                if i == j:

                    total_strength = dict_characters[i]["strength"]

                    total_speed = dict_characters[i]["speed"]

                    for k in dict_characters[i]["weapons"]:  # BUCLE DE SUMA TOTAL

                        total_strength += dict_weapons[k]["strength"]

                        total_speed += dict_weapons[k]["speed"]

                    table += f"{str(i)}".ljust(10) + dict_characters[i]["name"].ljust(13) + " " + str(

                        total_strength).rjust(9) + " " + str(total_speed).rjust(9) + " " + str(
                        dict_characters[i]["experience"]).rjust(

                        18) + "\n"

            print(table)

            print("\n\n")

    elif int(opc) == 5:
        pass

