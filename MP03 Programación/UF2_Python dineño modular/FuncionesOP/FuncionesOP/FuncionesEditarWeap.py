from One_Piece import *
from FuncionesUtils.funcionesUtils import menus
from FuncionesUtils.funcionesUtils import limiteStats
from MenusDicc.cabeceras_menus import *


# Funcion editar armas
def editarWeap():
    lista = list(dict_weapons.keys())
    for key in lista:
        print(key, ')', str(
            dict_weapons[key]["name"]), ',', " Strength: " + str(
            dict_weapons[key]["strength"]), ',', " Speed: " + str(
            dict_weapons[key]["speed"]))
    print()
    id = input('ID weapon to edit: \n')
    opc = menus(menu032X)

    if opc == 4:
        pass
        # atras al menu 3
    elif opc == 1:
        #NAME
        new_n_w = input('Enter the new name:\n')
        s_n = str(input('Do you want to change name' + dict_weapons[int(id)][
            'name'] + 'by' + new_n_w + '? Press y/n' + '\n'))

        if s_n.lower() == 'n':
            return

        elif s_n.lower() == 'y':
            dict_weapons[int(id)]['name'] = new_n_w
            print(dict_weapons[int(id)])  ###se borra al final

    elif int(opc) == 2:
        # STRENGTH
        strength2 = limiteStats()

        s_n = str(input('Do you want to change strength ' + str(dict_weapons[int(id)][
                                                                    'strength']) + ' by ' + str(
            strength2) + '? Press y/n' + '\n'))

        if s_n.lower() == 'n':
            print('\n')

        elif s_n.lower() == 'y':
            dict_weapons[int(id)]['strength'] = int(strength2)
            print(dict_weapons[int(id)]['strength'])


    elif int(opc) == 3:
        # speed

        speed2 = limiteStats()
        s_n = str(input('Do you want to change speed ' + str(dict_weapons[int(id)][
                                                                 'speed']) + ' by ' + str(
            speed2) + '? Press y/n' + '\n'))

        if s_n.lower() == 'n':
            print()

        elif s_n.lower() == 'y':

            dict_weapons[int(id)]['speed'] = int(speed2)
