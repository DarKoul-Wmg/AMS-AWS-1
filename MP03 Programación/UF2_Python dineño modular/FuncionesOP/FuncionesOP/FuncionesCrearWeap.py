from MenusDicc.diccionarios import *
from FuncionesUtils.funcionesUtils import *
from MenusDicc.cabeceras_menus import *


# Tipo de arma
def tipoArma():
    while True:
        print(kind_Weapon)  # TIPO DE ARMA
        two_hands = False
        opc = validarOpc(input("Option >\n"),1,2)

        if opc == 1:
            return two_hands

        elif opc == 2:
            two_hands = True
            return two_hands


# Funcion MAIN crear arma
def crearArma():
    print("****** Menu 22 - Create Weapon**")

    id_weapon = len(dict_weapons) + 1
    nameWeapon = input("Name of the new weapon:\n")

    print("Weapon strenght: 1-9 \n")
    strength = limiteStats()
    print("Weapon speed: 1-9 \n")
    speed = limiteStats()
    two_hands = tipoArma()
    input("Guardar")
    guardarArma(id_weapon,nameWeapon,strength,speed,two_hands)

#Guardar arma en diccionario
def guardarArma(id_weapon,nameWeapon,strength,speed,two_hands):
    while True:
        cabeceraArma = "Name: {}\nStrength:{}\nSpeed:{}\nTwo hands type: {}\n".format(nameWeapon,strength,speed,two_hands)
        print(cabeceraArma)

        save = input("Save this weapon? S/N\n")

        if save.lower() == "s":
            dict_weapons[id_weapon] = {"name": nameWeapon, "strength": strength, "speed": speed,
                                       "two_hand": two_hands}
            return

        elif save.lower() == "n":
            return

        else:
            print("Invalid option")


