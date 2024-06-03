from MenusDicc.diccionarios import *
from FuncionesUtils.funcionesUtils import *
import random
from MenusDicc.cabeceras_menus import *


#Crea a u character nuevo
def crearJugador():

    while True:
        print("****** Menu 21 - Create Character**")
        name = input("Name of the new character:\n")
        cat = catJugador()
        id = len(dict_characters) + 1
        strenght = random.randint(1, 9)
        speed = random.randint(1, 9)
        #input("Armas")
        weapons = armasJugador()
        #input("Guardar")
        guardarJugador(id, name, cat, weapons, strenght, speed)
        return True


# Proceso de seleccionar categoria
def catJugador():
    while True:
        cat = 0
        opc = 0
        crearCharacter = 0
        print(cabecera_side)

        opc = validarOpc(input("Option >\n"),1,2) #RECUPERAR OPCION VALIDA

        if opc == 1: #MARINES
            print(cabecera_range_marine)
            opc = validarOpc(input("Option >\n"),1,3)

            if opc == 1:  # admirant
                cat = 4
                return cat
            elif opc == 2:  # viceadmirant
                cat = 5
                return cat
            elif opc == 3:  # Lieutenant
                cat = 6
                return cat

        elif opc == 2: #PIRATAS

            print(cabecera_crew_pirate)
            opc = validarOpc(input("Option >\n"),1,3)

            if opc == 1:
                cat = 1
                return cat
            elif opc == 2:
                cat = 2
                return cat
            elif opc == 3:
                cat = 3
                return cat



def quitarArma(opc,weapons):
    opc = int(opc)
    if len(weapons) == 1:
        weapons.remove(opc)  # Eliminar un elemento
    else:
        for i in range(len(weapons)):  # recorre weapons para eliminar arma
            if opc == weapons[i]:
                weapons.remove(opc)
                break

#Proceso de seleccionar arma del jugador
def armasJugador():
    weapons = []

    while True:
        cadenaAvalible = "=" * 10 + "Available Weapons" + "=" * 10 + "\n"
        cadenaInUse = "=" * 10 + "Character Weapons" + "=" * 10 + "\n"

        if len(weapons) == 0:  # MOSTRAR PRINT SIN ARMAS
            cadenaInUse += "\n" + "-" * 15 + " None " + "-" * 15 + "\n" * 4
            for weapon in range(len(dict_weapons)):
                cadenaAvalible += str(weapon + 1) + ") name " + dict_weapons[weapon + 1]["name"] \
                                + " Strength " + str(dict_weapons[weapon + 1]["strength"]) + \
                                  " Speed " + str(dict_weapons[weapon + 1]["speed"]) + "\n"

        if len(weapons) >= 1:  # MOSTRAR PRINT ARMAS
            if dict_weapons[weapons[0]]["two_hand"] == True or len(weapons) == 2:  # COMPROBAR QUE ARMA TENGA 2 MANOS 0 QUE SEAN 2 DE UNA MANO
                cadenaAvalible += "-" * 15 + " None " + "-" * 15 + "\n" * 4

            if dict_weapons[weapons[0]]["two_hand"] == False and len(weapons) <= 1:  # SEGUNDA COMPROBACIÓN DE ARMA 2 MANOS
                for weapon in range(len(dict_weapons)):
                    if dict_weapons[weapon + 1]["two_hand"] == False:  # PASAR ARMAS 2 MANOS A FALSO PARA QUE NO SE MUESTREN
                        cadenaAvalible += str(weapon + 1) + ") name " + dict_weapons[weapon + 1][
                            "name"] + " Strength " + str(dict_weapons[weapon + 1]["strength"]) + \
                                          " Speed " + str(dict_weapons[weapon + 1]["speed"]) + "\n"

            for weapon in range(len(weapons)):  # MUESTRA ARMAS PERSONAJES
                cadenaInUse += str(weapons[weapon]) + ") name " + dict_weapons[weapons[weapon]]["name"] \
                            + " Strength " + str(dict_weapons[weapons[weapon]]["strength"])+" Speed " + \
                               str(dict_weapons[weapons[weapon]]["speed"]) + "\n"

        while True:
            print(cadenaAvalible)
            print(cadenaInUse)
            print(cabecera2)
            deleteWeapon = False
            opc = input("Option >\n")
            if opc.isspace() or opc == "":  # EVITAR QUE PETE CON ENTER
                print("Enter a numeric option\n")
            elif opc[0] == "-":  # ELIMINAR ARMA COMPROBANDO SI TIENE "-"
                if opc[1:].isdigit():  # Comprueba la id de arma conforme existe
                    opc = int(opc[1:])
                    deleteWeapon = True
                    if opc in weapons:  # Salir del While
                        break
                else:
                    print("====Invalid Option====.\n")
            elif opc.isdigit():
                opc = int(opc)

                if opc == 0:
                    return weapons


                if opc in range(len(dict_weapons) + 1):  # Comprueba la id de arma conforme existe

                    if len(weapons) == 0:
                        break
                    elif len(weapons) == 2 or dict_weapons[weapons[0]]["two_hand"] == True:
                        print("Ya tienes dos armas o un arma de dos manos\n")
                    elif len(weapons) >= 0:
                        if dict_weapons[opc]["two_hand"] == False:
                            break

                else:
                    print("====Invalid Option====.\n")
            else:
                print("Enter a numeric option\n")

        if deleteWeapon == True:
            if len(weapons) == 1:
                weapons.remove(opc)  # Eliminar un elemento
            else:
                for i in range(len(weapons)):  # recorre weapons para eliminar arma
                    if opc == weapons[i]:
                        weapons.remove(opc)
                        break
        if opc != 0 and deleteWeapon == False:
            weapons.append(opc)


# Guardar jugador en diccionario
def guardarJugador(id,name,cat,weapons,strenght,speed):
    while True:
        cadena = ""
        for key in weapons:  #ARMAS PERSONAJE
            cadena += dict_weapons[key]["name"] + ", "
            cadena = cadena[: len(cadena) - 2]
        cabeceraNewPersonaje = "The new player will be:\n\nName: {}\nCategory: {}\nWeapons: {}\nStrength:{}\n" \
                                    "Speed:{}\nExperience: 0\n".format(name,dict_categorys[cat],cadena,strenght,speed)
        print(cabeceraNewPersonaje)
        save = input("Save this player? S/N")
        if save.lower() == "s":
            dict_characters[id] = {"name": name, "category": cat, "weapons": weapons, "strength": strenght,
                                           "speed": speed, "experience": 0}
            return
        elif save.lower() == "n":
            return
        else:
            print("====Invalid option====")
