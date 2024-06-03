letrasDni = ['T','R','W','A','G','M','Y','F','P','D','X','B','N','J','Z','S','Q','V','H','L','C','K','E']
usuario1 = {"nombre":"Pedro Javier Morales",  "direccion": "Flores 36 8º 2º", "tfn":["+0034345345345"],"compras":[1234,423,23]}
usuario2 = {"nombre":"Maite Lopez Miravet", "direccion":"Balames 31 1º 2º","tfn":["+0034234234235","+0034239999235"],"compras":[12344]}
usuario3 = {"nombre":"Marta Garcia Suarez",  "direccion":"Valencia 21 3º 1º","tfn": ["+0075766576575"],"compras":[34,423,23,6]}
usuarios = {"47474747X":usuario1,"24536425T":usuario2,"76767676H":usuario3}

menu00 = "1)Crear usuario\n2)Ver usuarios\n3)Buscar\n4)Listar Usuarios\n5)Salir"
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
        print("\n"+"Welcome to the User Management Program".center(50,"*")+"\n")
        print(menu00)
        opc = input("Option:\n")
        if not opc.isdigit():
            print("Numeric Entries Only")
        elif int(opc) not in range(1, 7):
            print("Incorrect Option")
        else:
            opc = int(opc)
            if opc == 1:
                dni, name, surname, address = "", "", "", ""
                tfn_list = []
                flg_01 = True
                flg_00 = False
            # Modify User
            if opc == 2:
                flg_02 = True
                flg_00 = False
            #Show Users
            if opc == 3:
                for dni in usuarios:
                    #print(dni)
                    datos = ""
                    datos += "DNI:".ljust(10)+dni.rjust(20)+"\n"+"Nombre:".ljust(10)+\
                        usuarios[dni]["nombre"].rjust(20)+"\n"+"TFN:".ljust(10)

                    for i in range(len(usuarios[dni]["tfn"])):
                        if i == 0:
                            datos += usuarios[dni]["tfn"][i].rjust(20)+"\n"
                        else:
                            datos += usuarios[dni]["tfn"][i].rjust(30) + "\n"
                    #if len(usuarios[dni]["tfn"]) == 1:
                    print(datos)
                    input("Enter to continue")

                # dni:                                          44444444A
                # nombre:                                          Pepito
                # tfn:                                     +0034239999235
                #                                          +0034234234235
                print("Opcion2")
            # Find Users
            if opc == 4:
                flg_00 = False
                flg_04 = True
            # List Users
            if opc == 5:
                flg_05 = True
                flg_00 = False
            # Exit
            if opc == 6:
                salir = True
                flg_00 = False
        #Create User
        while flg_01:

            data = "\n"+"\n"+"Dni:*".ljust(10)+dni.ljust(25)+"\n"+"Name:*".ljust(10)+name.ljust(25)+"\n"+\
                   "Surname:*".ljust(10)+surname.ljust(25)+"\n"+"Address:*".ljust(10)+address.ljust(25)+"\n"+\
                   "tfn:".ljust(10)
            for i in range(len(tfn_list)):
                if i == 0:
                    data += tfn_list[i].ljust(15) + "\n"
                else:
                    data += " ".ljust(10)+tfn_list[i].ljust(15) + "\n"
            print(data+"\n")
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
                    dni_ok = False
                    while not dni_ok:
                        dni = input("DNI:\n")
                        if not len(dni) == 9:
                            print("Incorrect DNI length")
                        elif not dni[0:8].isdigit():
                            print("Incorrect DNI Number")
                        elif not dni[8].upper() == letrasDni[int(dni[0:8]) % 23]:
                            print("Incorrect DNI letter")
                        elif dni in usuarios:
                            print("Dni {} Already Exists".format(dni))
                        else:
                            dni = dni.upper()
                            dni_ok = True
                # Enter Name
                if opc == 2:
                    name = input("Enter New Name:\n")
                    while not name.replace(" ","").isalpha():
                        print("Wrong name")
                        name = input("Enter New Name:\n")
                #Enter Surname
                if opc == 3:
                    surname = input("Enter New Surname:\n")
                    while not surname.replace(" ","").isalpha():
                        print("Wrong surname")
                        surname = input("Enter New Surname:\n")
                # Enter Address
                if opc == 4:
                    address = input("Enter New Address:\n")
                    while address.replace(" ", "") == "":
                        address = input("Enter New Address:\n")
                # Enter new Tfn
                if opc == 5:
                    new_tfn = input("Enter the New Tfn:\n")
                    while not new_tfn[0] == "+" or len(new_tfn) != 14 or not new_tfn[1:].isdigit():
                        print("Incorrect TFN")
                        new_tfn = input("Enter the New Tfn:\n")
                    tfn_list.append(new_tfn)
                # Save data
                if opc == 6:
                    if dni=="" or name == "" or surname == "" or address =="":
                        print("Fields With * are Mandatory")
                    else:
                        usuarios[dni] =  {"nombre":name + " " +surname,  "direccion":address,"tfn": tfn_list,"compras":[]}
                        print("New User Saved")
                        flg_01 = False
                        flg_00 = True
                # usuario3 = {"nombre":"Marta Garcia Suarez",  "direccion":"Valencia 21 3º 1º","tfn": ["+0075766576575"],"compras":[34,423,23,6]}
                        input("Enter to Continue")
                if opc == 7:
                    flg_01 = False
                    flg_00 = True
        #Find Users
        while flg_04:
            cabecera = "*" * 110 + "\n" + "DNI".ljust(15) + "Name".ljust(30) + "Address".ljust(30) + "Tfn".rjust(
                20) + "Total Purchases".rjust(15) + "\n" + "*" * 110 + "\n"
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
                else:
                    to_find = input("Enter the Text to Find:\n")
                    # print(dnis_usuarios)
                    datos = ""
                    for dni in usuarios:
                        if (opc == 1 and to_find in dni) or (opc == 2 and to_find.lower() in usuarios[dni]["nombre"].lower()):
                            total_compras = 0
                            for compra in usuarios[dni]["compras"]:
                                total_compras += compra
                            datos += dni.ljust(15) + usuarios[dni]["nombre"].ljust(30) + usuarios[dni]["direccion"].ljust(
                                30) + usuarios[dni]["tfn"][0].rjust(20) + str(total_compras).rjust(15) + "\n"
                            if len(usuarios[dni]["tfn"]) > 1:
                                for i in range(1, len(usuarios[dni]["tfn"])):
                                    datos += " ".ljust(75) + usuarios[dni]["tfn"][i].rjust(20) + "\n"
                                    # usuario3 = {"nombre":"Marta Garcia Suarez",  "direccion":"Valencia 21 3º 1º","tfn": ["+0075766576575"],"compras":[34,423,23,6]}
                    print(cabecera + datos)
        #modify user
        while flg_02:
            print("Enter the DNI of the Client you want to modify:\n")
            dni = ""
            dni_ok = False
            while not dni_ok:
                dni = input("DNI:\n")
                if not len(dni) == 9:
                    print("Incorrect DNI length")
                elif not dni[0:8].isdigit():
                    print("Incorrect DNI Number")
                elif not dni[8].upper() == letrasDni[int(dni[0:8]) % 23]:
                    print("Incorrect DNI letter")
                elif not dni in usuarios:
                    print("DNI {} does not exists!".format(dni))
                else:
                    dni = dni.upper()
                    dni_ok = True
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
                        purchase = input("Enter the amount of the purchase:\n")
                        while not purchase.isdigit():
                            print("Incorrect Amount")
                            purchase = input("Enter the amount of the purchase:\n")
                        print("Added the {} purchase to {} - {}".format(purchase,dni,usuarios[dni]["nombre"]))
                        usuarios[dni]["compras"].append(int(purchase))
                    if opc == 2:
                        tfn = input("Enter the New Tfn")
                        while not tfn[0] == "+" or len(tfn) != 14 or not tfn[1:].isdigit():
                            print("Incorrect TFN")
                            tfn = input("Enter the New Tfn")
                        print("Added the {} Tfn to {} - {}".format(tfn, dni, usuarios[dni]["nombre"]))
                        usuarios[dni]["tfn"].append(tfn)
                    if opc == 3:
                        tfn = input("Enter the Tfn to Delete")
                        while not tfn[0] == "+" or len(tfn) != 14 or not tfn[1:].isdigit():
                            print("Incorrect TFN")
                            tfn = input("Enter the Tfn to Delete")
                        if not tfn in usuarios[dni]["tfn"]:
                            print("The phone {} does not belong to the user {}".format(tfn,usuarios[dni]["nombre"]))
                        else:
                            print("Deleted the {} Tfn to {} - {}".format(tfn, dni, usuarios[dni]["nombre"]))
                            usuarios[dni]["tfn"].remove(tfn)
                    if opc == 4:
                        address = input("Enter the New Address:\n")
                        print("Changed the {} Address to {} ".format(usuarios[dni]["nombre"], address))
                        usuarios[dni]["direccion"] = address
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

                cabecera = "*" * 110 + "\n" + "DNI".ljust(15) + "Name".ljust(30) + "Address".ljust(30) + "Tfn".rjust(
                    20) + "Total Purchases".rjust(15) + "\n" + "*" * 110 + "\n"
                dnis_usuarios = list(usuarios.keys())
                if opc == 5:
                    flg_00 = True
                    flg_05 = False
                if opc == 1:
                    print("List Users by DNI dni")
                    for pasadas in range(len(dnis_usuarios)-1):
                        for i in range(len(dnis_usuarios)-1-pasadas):
                            if dnis_usuarios[i] > dnis_usuarios[i+1]:
                                dnis_usuarios[i] , dnis_usuarios[i + 1] = dnis_usuarios[i+1] , dnis_usuarios[i ]
                    #print(dnis_usuarios)
                    datos = ""
                    for dni in dnis_usuarios:
                        total_compras = 0
                        for compra in usuarios[dni]["compras"]:
                            total_compras += compra
                        if len(usuarios[dni]["tfn"]) == 0:
                            datos += dni.ljust(15) + usuarios[dni]["nombre"].ljust(30) + usuarios[dni][
                                "direccion"].ljust(30) + " ".rjust(20) + str(total_compras).rjust(
                                15) + "\n"
                        else:
                            datos += dni.ljust(15)+usuarios[dni]["nombre"].ljust(30)+usuarios[dni]["direccion"].ljust(30)+usuarios[dni]["tfn"][0].rjust(20)+str(total_compras).rjust(15)+"\n"
                        if len(usuarios[dni]["tfn"]) > 1:
                            for i in range(1,len(usuarios[dni]["tfn"])):
                                datos += " ".ljust(75)+usuarios[dni]["tfn"][i].rjust(20) + "\n"
                                #usuario3 = {"nombre":"Marta Garcia Suarez",  "direccion":"Valencia 21 3º 1º","tfn": ["+0075766576575"],"compras":[34,423,23,6]}
                    print(cabecera+datos)
                if opc == 2:
                    print("List Users by Name")
                    for pasadas in range(len(dnis_usuarios) - 1):
                        for i in range(len(dnis_usuarios) - 1 - pasadas):

                            if usuarios[dnis_usuarios[i]]["nombre"] > usuarios[dnis_usuarios[i+1]]["nombre"]:
                                dnis_usuarios[i], dnis_usuarios[i + 1] = dnis_usuarios[i + 1], dnis_usuarios[i]

                    datos = ""
                    for dni in dnis_usuarios:
                        total_compras = 0
                        for compra in usuarios[dni]["compras"]:
                            total_compras += compra
                        if len(usuarios[dni]["tfn"]) == 0:
                            datos += dni.ljust(15) + usuarios[dni]["nombre"].ljust(30) + usuarios[dni][
                                "direccion"].ljust(30) + " ".rjust(20) + str(total_compras).rjust(
                                15) + "\n"
                        else:
                            datos += dni.ljust(15) + usuarios[dni]["nombre"].ljust(30) + usuarios[dni][
                                "direccion"].ljust(30) + usuarios[dni]["tfn"][0].rjust(20) + str(total_compras).rjust(
                                15) + "\n"
                        if len(usuarios[dni]["tfn"]) > 1:
                            for i in range(1, len(usuarios[dni]["tfn"])):
                                datos += " ".ljust(75) + usuarios[dni]["tfn"][i].rjust(20) + "\n"
                                # usuario3 = {"nombre":"Marta Garcia Suarez",  "direccion":"Valencia 21 3º 1º","tfn": ["+0075766576575"],"compras":[34,423,23,6]}
                    print(cabecera + datos)
                if opc == 3:
                    print("List Users by Address")
                    for pasadas in range(len(dnis_usuarios) - 1):
                        for i in range(len(dnis_usuarios) - 1 - pasadas):

                            if usuarios[dnis_usuarios[i]]["direccion"] > usuarios[dnis_usuarios[i+1]]["direccion"]:
                                dnis_usuarios[i], dnis_usuarios[i + 1] = dnis_usuarios[i + 1], dnis_usuarios[i]

                    datos = ""
                    for dni in dnis_usuarios:
                        total_compras = 0
                        for compra in usuarios[dni]["compras"]:
                            total_compras += compra
                        if len(usuarios[dni]["tfn"]) == 0:
                            datos += dni.ljust(15) + usuarios[dni]["nombre"].ljust(30) + usuarios[dni][
                                "direccion"].ljust(30) + " ".rjust(20) + str(total_compras).rjust(
                                15) + "\n"
                        else:
                            datos += dni.ljust(15) + usuarios[dni]["nombre"].ljust(30) + usuarios[dni][
                                "direccion"].ljust(30) + usuarios[dni]["tfn"][0].rjust(20) + str(total_compras).rjust(
                                15) + "\n"
                        if len(usuarios[dni]["tfn"]) > 1:
                            for i in range(1, len(usuarios[dni]["tfn"])):
                                datos += " ".ljust(75) + usuarios[dni]["tfn"][i].rjust(20) + "\n"
                    print(cabecera + datos)

                if opc == 4:
                    print("List Users by Total Purchases")

                    #usuarios = {"47474747R": usuario1, "24536425T": usuario2, "76767676H": usuario3}
                    total_compras = {}
                    for nif in usuarios:
                        total_compras[nif] = 0
                        for compra in usuarios[nif]["compras"]:
                            total_compras[nif] += compra
                    #print(total_compras)
                    input("Enter")
                    for pasadas in range(len(dnis_usuarios) - 1):
                        for i in range(len(dnis_usuarios) - 1 - pasadas):
                            if total_compras[dnis_usuarios[i]] < total_compras[dnis_usuarios[i+1]]:
                                dnis_usuarios[i], dnis_usuarios[i + 1] = dnis_usuarios[i + 1], dnis_usuarios[i]
                    datos = ""
                    for dni in dnis_usuarios:
                        total_compras = 0
                        for compra in usuarios[dni]["compras"]:
                            total_compras += compra
                        if len(usuarios[dni]["tfn"]) == 0:
                            datos += dni.ljust(15) + usuarios[dni]["nombre"].ljust(30) + usuarios[dni][
                                "direccion"].ljust(30) + " ".rjust(20) + str(total_compras).rjust(
                                15) + "\n"
                        else:
                            datos += dni.ljust(15) + usuarios[dni]["nombre"].ljust(30) + usuarios[dni][
                                "direccion"].ljust(30) + usuarios[dni]["tfn"][0].rjust(20) + str(total_compras).rjust(
                                15) + "\n"
                        if len(usuarios[dni]["tfn"]) > 1:
                            for i in range(1, len(usuarios[dni]["tfn"])):
                                datos += " ".ljust(75) + usuarios[dni]["tfn"][i].rjust(20) + "\n"
                    print(cabecera + datos)



