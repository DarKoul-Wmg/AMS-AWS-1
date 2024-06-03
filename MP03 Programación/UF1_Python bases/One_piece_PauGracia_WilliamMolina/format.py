# nameWeapon = "Hola"
# strength = 0
# speed = 0
# two_hands = True
# cabeceraArma = "Name: {}\nStrength:{}\nSpeed:{}\nTwo hands type: {}\n".format(nameWeapon,strength,speed,two_hands)
# print(cabeceraArma)

cabecera0 = "MENU0"
cabecera1 = "MENU1"
cabecera2 = "MENU2"
cabecera3 = "MENU3"
cabecera4 = "MENU4"

flg00 = True
flg01 = False
flg02 = False
flg03 = False
flg04 = False
while True:
    while flg00:
        print(cabecera0)
        opcion = input("Option >\n")
        if opcion.isdigit():
            opcion = int(opcion)

            if opcion == 1:
                flg01 = True
                flg00 = False

            elif opcion == 2:
                flg02 = True
                flg00 = False

            elif opcion == 3:
                flg03 = True
                flg00 = False
            elif opcion == 4:
                flg04 = True
                flg00 = False
            else:
                print("Opción no válida. Por favor, elige una opción válida.\n")
        else:
            print("Introduce una opcion numerica\n")

    while flg01:
        print(cabecera1)
        print("keso")
        flg00 = True
        flg01 = False

    while flg02:
        print(cabecera2)
        print("keso2")
        flg00 = True
        flg02 = False

    while flg03:
        print(cabecera3)
        print("keso3")
        flg00 = True
        flg03 = False

    while flg04:
        print(cabecera4)
        print("keso4")
        flg00 = True
        flg04 = False
