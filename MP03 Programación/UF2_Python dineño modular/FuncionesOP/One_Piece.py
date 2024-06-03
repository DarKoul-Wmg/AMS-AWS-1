from FuncionesOP.FuncionesEditarCh import *
from FuncionesOP.FuncionesEditarWeap import *
from MenusDicc.cabeceras_menus import *
from FuncionesOP.FuncionesCrearCh import *
from FuncionesOP.FuncionesCrearWeap import *
from FuncionesOP.FuncionesListarCh import *
from FuncionesOP.FuncionesListarWeap import *

salir = False
flg_00 = True
flg_03 = False
flg_02 = False
flg_04 = False
flg_05 = False


# VARIABLES MENU 2
flg_06 = False             # MENU CREATE
creacionCharacter = False  # FLAG MENU CREAR PERSONAJE
creacionArmas = False      # FLAG MENU CREAR ARMA



while salir != True:
    ##menu principal(00)
    while flg_00:

        opc = menus(menu00)
        #print("opc: " + str(opc))

        if opc == 1:
            print('Not implemented yet')
            flg_00 = True


        elif opc == 2:
            flg_06 = True
            flg_00 = False
            # para menu 2

        elif opc == 3:
            flg_05 = True
            flg_00 = False
            # para menu03

        elif opc == 4:
            flg_02 = True
            flg_00 = False
            # para menu04

        elif opc == 5:
            exit() # eliminar proceso del programa


############### menu create (2)###############
    while flg_06:
        opc = menus(menu02)

        if opc == 3:
            flg_00 = True
            flg_06 = False
        else:
            if opc == 1:
                creacionCharacter = True
                flg_06 = False

            elif opc == 2:

                creacionArmas = True
                flg_06 = False

    while creacionCharacter:
        if crearJugador(): #vovler a menu create
            flg_06 = True
            creacionCharacter = False

    while creacionArmas:
        if crearArma():
            flg_06 = True
            creacionArmas = False



    ######## menu04 #########
    while flg_02:
        opc = menus(menu04)
        # comprobar opciones menu correctas

        if opc == 1:
            flg_03 = True
            flg_02 = False
            # para menu041
        elif opc == 2:
            flg_04 = True
            flg_02 = False
            # para menu042
        elif opc == 3 or opc == 4:
            print("Not implemented yet")
        elif opc == 5:
            flg_00 = True
            flg_02 = False

            # atras
    ############# menu041 ####################
    while flg_03:
        opc = menus(menu041)
        if opc == 5:
            flg_03 = False
            flg_02 = True
            # back

        elif opc == 1:
            # LISTAR ID ============
            print(menuCharactersID)
            listarChID()



        elif int(opc) == 2:
            # LISTAR Name ============
            print(menuCharactersName)
            listarChName()


        elif int(opc) == 3:
            # LISTAR strength
            print(menuCharactersStrength)
            listarChStrength()

        elif int(opc) == 4:
            ##listar speed

            print(menuCharactersSpeed)
            listarChSpeed()


    #############menu042####################
    while flg_04:
        opc = menus(menu042)

        if int(opc) == 5:
            flg_02 = True
            flg_04 = False

            # atras
        elif int(opc) == 1:
            # listar armas por ID
            print(cabecera_list_weapons)
            listarWeapID()


        elif int(opc) == 2:
            ##ordenar por NOMBRE
            print(cabecera_list_weapons)
            listarWeapName()

        elif int(opc) == 3:
            ##ordenar por STRENGTH
            print(cabecera_list_weapons)
            listarWeapStrength()

        elif int(opc) == 4:
            ##ordenar por SPEED
            print(cabecera_list_weapons)
            listarWeapSpeed()


    #####################menu03######################
    while flg_05:
        opc = menus(menu03)
        # comprobar opciones menu correctas
        if int(opc) == 3:
            flg_05 = False
            flg_00 = True
            # atras al menu 0

        elif int(opc) == 1:
            ####menu031
            print('===Menu 031 (Select Caracter to Edit) ===')
            editarCh()

        elif int(opc) == 2:
            # menu32
            print('===Menu 032 (Select Weapon to Edit) ===')
            editarWeap()

