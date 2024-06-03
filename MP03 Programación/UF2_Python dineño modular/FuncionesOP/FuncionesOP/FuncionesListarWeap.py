from MenusDicc.diccionarios import *

#Printea la lisat de armas ya ordenada
def printArmasOrdenadas(weapons_list):
    for clave, character in weapons_list:
        print(str(clave).ljust(10),
              str(character['name']).ljust(11),
              str(character['strength']).rjust(10),
              str(character['speed']).rjust(9),
              str(character['two_hand']).rjust(16))

    print('\n')

# Funciones para listar armas segun tipos:

def listarWeapID():

    weapons_list = list(dict_weapons.items())

    for i in range(len(weapons_list) - 1):
        for j in range(0, len(weapons_list) - i - 1):
            if weapons_list[j][0] > weapons_list[j + 1][0]:
                # comparar posicion de id
                aux = weapons_list[j]
                weapons_list[j] = weapons_list[j + 1]
                weapons_list[j + 1] = aux
    # el motivo del item se ve aqui
    printArmasOrdenadas(weapons_list)

def listarWeapName():
    weapons_list = list(dict_weapons.items())

    for i in range(len(weapons_list) - 1):
        for j in range(0, len(weapons_list) - i - 1):
            if weapons_list[j][1]['name'] > weapons_list[j + 1][1]['name']:
                aux = weapons_list[j]
                weapons_list[j] = weapons_list[j + 1]
                weapons_list[j + 1] = aux

    printArmasOrdenadas(weapons_list)

def listarWeapStrength():
    weapons_list = list(dict_weapons.items())

    for i in range(len(weapons_list) - 1):
        for j in range(0, len(weapons_list) - i - 1):
            if weapons_list[j][1]['strength'] < weapons_list[j + 1][1]['strength']:
                aux = weapons_list[j]
                weapons_list[j] = weapons_list[j + 1]
                weapons_list[j + 1] = aux

    printArmasOrdenadas(weapons_list)

def listarWeapSpeed():
    weapons_list = list(dict_weapons.items())

    for i in range(len(weapons_list) - 1):
        for j in range(0, len(weapons_list) - i - 1):
            if weapons_list[j][1]['speed'] < weapons_list[j + 1][1]['speed']:
                aux = weapons_list[j]
                weapons_list[j] = weapons_list[j + 1]
                weapons_list[j + 1] = aux

    printArmasOrdenadas(weapons_list)
