from MenusDicc.diccionarios import *

# Funciones para listar jugadores segun tipos:
def listarChID():
    table = ""
    listaID = list(dict_characters.keys())

    for pasada in range(len(listaID) - 1):
        for key in range(len(listaID) - 1 - pasada):
            if listaID[key] < listaID[key + 1]:
                opc = listaID[key]
                listaID[key] = listaID[key + 1]
                listaID[key + 1] = opc

    for i in listaID:
        # RECUENTO DE LOS DIFERENTES VALORES DE CADA PARÁMETRO
        total_strength = dict_characters[i]["strength"]
        total_speed = dict_characters[i]["speed"]

        for j in dict_characters[i]["weapons"]:  # BUCLE DE SUMA TOTAL
            total_strength += dict_weapons[j]["strength"]
            total_speed += dict_weapons[j]["speed"]

        table += "{}".format(i).ljust(10) + dict_characters[i]["name"].ljust(13) + " " + str(total_strength).rjust(9) + \
                 " " + str(total_speed).rjust(9) + " " + str(dict_characters[i]["experience"]).rjust(18) + "\n"
    print(table)
    print("\n\n")

def listarChName():
    table = ""
    listaName = []
    for i in dict_characters:
        listaName.append(dict_characters[i]["name"])

    for pasada in range(len(listaName) - 1):
        for name in range(len(listaName) - 1 - pasada):
            if listaName[name] > listaName[name + 1]:
                opc = listaName[name]
                listaName[name] = listaName[name + 1]
                listaName[name + 1] = opc

    for i in listaName:
        for j in range(1, len(dict_characters) + 1):  #
            if dict_characters[j]["name"] == i: #SI NOMBRE EN LISTA COINCIDE CON NOMBRE EN DICT, TOTAL DE VALORES
                total_strength = dict_characters[j]["strength"]
                total_speed = dict_characters[j]["speed"]

                for k in dict_characters[j]["weapons"]:  # BUCLE DE SUMA TOTAL
                    total_strength += dict_weapons[k]["strength"]
                    total_speed += dict_weapons[k]["speed"]

                table += "{}".format(str(j)).ljust(10) + dict_characters[j]["name"].ljust(13) + " " + str(
                    total_strength).rjust(9) + \
                         " " + str(total_speed).rjust(9) + " " + str(dict_characters[j]["experience"]).rjust(
                    18) + "\n"
    print(table)
    print("\n\n")

def listarChStrength():
    table = ""
    listaID = []
    for i in range(1, len(dict_characters) + 1):
        listaID.append(i)
    listaStrength = []
    for i in listaID:
        # RECUENTO DE LOS DIFERENTES VALORES DE CADA PARÁMETRO
        total_strength = dict_characters[i]["strength"]
        for j in dict_characters[i]["weapons"]:  # BUCLE DE SUMA TOTAL
            total_strength += dict_weapons[j]["strength"]
        listaStrength.append(total_strength)

    for pasada in range(len(listaStrength) - 1):
        for j in range(len(listaStrength) - 1 - pasada):
            if listaStrength[j] < listaStrength[j + 1]:
                listaStrength[j], listaStrength[j + 1] = listaStrength[j + 1], listaStrength[j]
                listaID[j], listaID[j + 1] = listaID[j + 1], listaID[j]

    for j in listaID:  # RECUENTO DE LOS DIFERENTES VALORES DE CADA PARÁMETRO
        for i in range(1, len(dict_characters) + 1):
            if i == j:
                total_strength = dict_characters[i]["strength"]
                total_speed = dict_characters[i]["speed"]
                for k in dict_characters[i]["weapons"]:  # BUCLE DE SUMA TOTAL
                    total_strength += dict_weapons[k]["strength"]
                    total_speed += dict_weapons[k]["speed"]
                table += "{}".format(str(i)).ljust(10) + dict_characters[i]["name"].ljust(13) + " " + str(
                    total_strength).rjust(9) + \
                         " " + str(total_speed).rjust(9) + " " + str(dict_characters[i]["experience"]).rjust(
                    18) + "\n"
    print(table)
    print("\n\n")

def listarChSpeed():
    table = ""
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

                table += "{}".format(str(i)).ljust(10) + dict_characters[i]["name"].ljust(13) + " " + str(
                    total_strength).rjust(9) + " " + str(total_speed).rjust(9) + " " + str(
                    dict_characters[i]["experience"]).rjust(
                    18) + "\n"
    print(table)
    print("\n\n")
