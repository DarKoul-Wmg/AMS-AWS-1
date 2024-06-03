
menu00 = "1)Create User\n2)Modify user\n3)Show Users\n4)Find Users\n5)List Users\n6)Exit"
menu01 = "1)Enter Dni\n2)Enter Name\n3)Enter Surname\n4)Enter Address\n5)Enter Tfn\n6)Save User\n7)Go Back"
menu02 = "\n"+"Menu 02 - Modify User".center(50,"*")+"\n"+"1)Add purchase\n2)Add tfn number\n3)Del tfn number\n4)Change address\n5)Go Back"
menu05 = "1)List Users by DNI\n2)List Users by Name\n3)List Users by Address\n4)List Users by Total Purchase\n5)Go back"
menu04 = "1)Find Users by DNI\n2)Find Users by Name\n3)Go back"

salir = False
flg_00 = True
flg_01 = False
flg_04 = False
flg_05 = False
flg_02 = False
while not salir:
    while flg_00:
        print(menu00)
        opc = input("Option:\n")
        if not opc.isdigit():
            print("Numeric Entries Only")
        elif int(opc) not in range(1, 7):
            print("Incorrect Option")
        else:
            opc = int(opc)
            if opc == 1:

                flg_01 = True
                flg_00 = False

            if opc == 2:
                flg_02 = True
                flg_00 = False

            if opc == 3:


            if opc == 4:
                flg_00 = False
                flg_04 = True


            if opc == 5:
                flg_05 = True
                flg_00 = False
            #
            if opc == 6:
                salir = True
                flg_00 = False


        while flg_01:
            print(menu01)
            opc = input("Option:\n")
            if not opc.isdigit():
                print("Numeric Entries Only")
            elif int(opc) not in range(1, 8):
                print("Incorrect Option")
            else:
                opc = int(opc)
                #Enter Dni
                if opc == 1:

                if opc == 2:

                if opc == 3:

                if opc == 4:

                if opc == 5:

                if opc == 6:

                if opc == 7: #Salir
                    flg_01 = False
                    flg_00 = True

        while flg_04:

            print(menu04)
            opc = input("Option:\n")
            if not opc.isdigit():
                print("Numeric Entries Only")
            elif int(opc) not in range(1, 4):
                print("Incorrect Option")
            else:
                opc = int(opc)
                if opc == 3:
                    flg_00 = True
                    flg_04 = False


        while flg_02:

            while opc !=5:
                print(menu02)
                opc = input("Option:\n")
                if not opc.isdigit():
                    print("Enter only numeric options")
                elif int(opc) not in range(1, 6):
                    print("Incorrect option")
                else:
                    opc = int(opc)
                    if opc == 1:

                    if opc == 2:

                    if opc == 3:

                    if opc == 4:

                    if opc == 5:
                        flg_00 = True
                        flg_02 = False

        #List Users
        while flg_05:
            print(menu05)
            opc = input("Option:\n")
            if not opc.isdigit():
                print("Numeric Entries Only")
            elif int(opc) not in range(1, 6):
                print("Incorrect Option")
            else:
                opc = int(opc)

                if opc == 1:

                if opc == 2:

                if opc == 3:
