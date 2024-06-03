

#CREACIÓN DE MENUS con return de opción validada
def menus(tupla_menus):

    print(tupla_menus[0]) #CABECERA
    str_menu = ""
    for i in range(1,len(tupla_menus)): #OPCIONES
        str_menu += str(i)+")"+tupla_menus[i]+"\n"

    print(str_menu)
    # while not ( opc.isdigit() and opc in range(1,len(tupla_menus)+1)):
    while True:
        opc = input("Option ->:\n")
        if not opc.isdigit():
            print("Only numeric options")

        elif not int(opc) in range(1,len(tupla_menus)):
            print("====Invalid Option====")
        else:
            return int(opc)



# Rango de Velocidad y Fuerza
def limiteStats():
    while True:
        stat = input("value->: ")
        try:
            stat = int(stat)
            if not stat in range(10) or stat == 0:  # VALOR VALIDO
                print("==== Invalid Value ====")
                input("Press Enter to continue")
            else:
                return stat
        except ValueError:
            print("Error, enter a numeric option")

#Funcion auxiliar de validar opciones
def validarOpc(input, min, max):
    if input.isdigit():
        input = int(input)
        if input >= min and input <= max:

            return int(input) #Devolver opcion como INT

        else:
            print("Invalid Option\n")
            return


    else:
        print("Enter a numeric option\n")
        return
