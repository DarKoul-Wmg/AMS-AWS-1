from MenusDicc.diccionarios import *
from One_Piece import *

menu031 = "\n1)Name\n2)Weapon\n3)Go Back"

#Funcion pau para editar jugador
def editarCh():
    lista = list(dict_characters.keys())

    for key in lista:
        for item in dict_characters[key]:
            if item == "weapons":
                cadena = ""
                for weapon in dict_characters[key]["weapons"]:
                    cadena += dict_weapons[weapon]["name"] + ", "
                cadena = cadena[: len(cadena) - 2]

                print("ID: " + str(key) + " Name:" + dict_characters[key]["name"] + ", Category: " +
                      dict_categorys[dict_characters[key]["category"]] +
                      ", Weapons: " + cadena + " Strength:" + str(
                    dict_characters[key]["strength"]) + " Speed: " + str(
                    dict_characters[key]["speed"]) + " Experience: " + str(dict_characters[key]["experience"]))
    print()
    id_correcto = False

    while not id_correcto:
        id = input('ID to edit:' + '\n')
        if not id.isdigit():
            print('==================Invalid Option==================')
            input('Press enter to continue') + '\n'
        else:
            # comprobacion de id
            if not int(id) in dict_characters:
                print('==================Invalid Option==================')
                input('Press enter to continue') + '\n'

            else:
                id2 = int(id)

                print('Select feature to edit to character ID:', int(id), ' Name: ',
                      dict_characters[id2]['name'])
                id_correcto = True
                print(menu031)
                opc = input("->Options: " + "\n")
                # comprobar opciones menu correctas
                if not opc.isdigit():
                    print('==================Invalid Option==================')
                    input('Press enter to continue')
                elif not int(opc) in range(1, 4):
                    print('==================Invalid Option==================')
                    input('Press enter to continue')
                    ############menu031

                elif int(opc) == 3:
                    pass

                    # atras al menu 3
                elif int(opc) == 1:
                    # cambio nombre personaje
                    # ops1
                    new_name = input('Enter the new name: ')

                    s_n = str(input('Do you want to change name ' + dict_characters[id2][
                        'name'] + ' by ' + new_name + '? Press y/n' + '\n'))

                    if s_n.lower() == 'n':
                        flg_05 = False
                        flg_00 = True

                    elif s_n.lower() == 'y':
                        dict_characters[id2]['name'] = new_name
                        # se modifica la misma clave
                        flg_05 = False
                        flg_00 = True

                elif int(opc) == 2:
                    # ops 2 menu31
                    print_armas = False
                    while not print_armas:
                        # menu eleccion de armas
                        if len(dict_characters[id2]['weapons']) == 2:
                            # filtro por cantidad de armas por personaje

                            print()
                            print(cabecera_armas)
                            for i in range(len(dict_characters[id2]['weapons'])):
                                print(dict_characters[id2]['weapons'][i], ')',
                                      dict_weapons[dict_characters[id2]['weapons'][i]]['name'], ',',
                                      'Strength: ',
                                      dict_weapons[dict_characters[id2]['weapons'][i]]['strength'], 'Speed: ',
                                      dict_weapons[dict_characters[id2]['weapons'][i]]['speed'])


                        elif len(dict_characters[id2]['weapons']) == 1:
                            if dict_characters[id2]['weapons'][0] == 1 or dict_characters[id2]['weapons'][
                                0] == 3:

                                print()

                                print('===========Available Weapons============1')

                                for clave in dict_weapons.keys():

                                    if dict_weapons[clave]['two_hand'] == False:
                                        print(clave, ')', dict_weapons[clave]['name'], ',', 'Strength: ',
                                              dict_weapons[clave]['strength'],
                                              'Speed: ', dict_weapons[clave]['speed'])
                                print('===========Character weapons:===========')
                                for i in range(len(dict_characters[id2]['weapons'])):
                                    print(dict_characters[id2]['weapons'][i], ')',
                                          dict_weapons[dict_characters[id2]['weapons'][i]]['name'], ',',
                                          'Strength: ',
                                          dict_weapons[dict_characters[id2]['weapons'][i]]['strength'],
                                          'Speed: ',
                                          dict_weapons[dict_characters[id2]['weapons'][i]]['speed'])
                                # print_armas = True
                                print()
                            else:

                                print()
                                print('===========Available Weapons============')
                                print('------------------None------------------')
                                print('===========Character weapons:===========')
                                for i in range(len(dict_characters[id2]['weapons'])):
                                    print(dict_characters[id2]['weapons'][i], ')',
                                          dict_weapons[dict_characters[id2]['weapons'][i]]['name'],
                                          ',',
                                          'Strength: ',
                                          dict_weapons[dict_characters[id2]['weapons'][i]]['strength'],
                                          'Speed: ',
                                          dict_weapons[dict_characters[id2]['weapons'][i]]['speed'])
                                    # print_armas = True
                                print()


                        else:

                            print()

                            print('===========Available Weapons============')
                            for clave in dict_weapons.keys():
                                print(clave, ')', dict_weapons[clave]['name'], ',', 'Strength: ',
                                      dict_weapons[clave]['strength'],
                                      'Speed: ', dict_weapons[clave]['speed'])
                            print('===========Character weapons:===========')
                            print()
                            # print_armas = True

                        print()
                        print(menu_ad_weapon)
                        opcion = input("Option ->\n")

                        if opcion.isspace() or opcion == "":  # incorrecto con espacios
                            print("Enter a numerical option\n")
                        # eliminar arma
                        elif opcion[0] == "-":  # comprobar si tiene "-"
                            if opcion[1:].isdigit():  # Comprueba que sea numerico
                                opcion = int(opcion[1:])
                                if opcion in dict_characters[id2][
                                    'weapons']:  # busca que el numero de arma la tenga el p.
                                    dict_characters[id2]['weapons'].index(opcion)
                                    if dict_characters[id2]['weapons'].index(opcion) == 0:
                                        # si el arma esta en la primera posicion
                                        dict_characters[id2]['weapons'] = dict_characters[id2]['weapons'][1:]
                                        # elimina el arma mediante eliminar la posicion

                                        print('ok1')
                                    else:
                                        # si el arma esta en la segunda
                                        dict_characters[id2]['weapons'] = dict_characters[id2]['weapons'][:-1]
                                        # elimina el arma mediante eliminar la posicion

                                else:
                                    print('==================Invalid Option==================')
                                    input('Press enter to continue')


                            else:
                                print('==================Invalid Option==================')
                                input('Press enter to continue')
                        elif opcion.isdigit():
                            opcion = int(opcion)
                            if int(opcion) == 0:
                                # opcion 0 exit
                                print_armas = True

                            # sumar arma
                            elif opcion == 2 or opcion == 4 or opcion == 5:

                                if len(dict_characters[id2]['weapons']) == 0:

                                    if opcion in dict_weapons:  # Comprueba la id de arma conforme existe
                                        dict_characters[id2]['weapons'].append(opcion)

                                    else:
                                        print('==================Invalid Option==================')
                                        input('Press enter to continue')

                                else:
                                    print('==================Invalid Option==================')
                                    input('Press enter to continue')

                            elif opcion == 1 or opcion == 3:

                                if len(dict_characters[id2]['weapons']) == 0 or len(
                                        dict_characters[id2]['weapons']) == 1:
                                    # una o dos armas
                                    if opcion in dict_weapons:  # Comprueba la id de arma conforme existe
                                        dict_characters[id2]['weapons'].append(opcion)

                                    else:
                                        print('==================Invalid Option==================')
                                        input('Press enter to continue')

                            else:
                                print('==================Invalid Option==================')
                                input('Press enter to continue')
