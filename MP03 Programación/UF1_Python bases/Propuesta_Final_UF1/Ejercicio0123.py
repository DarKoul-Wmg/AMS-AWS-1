import random
name_list = ["Mario Torres Cuesta","Patricia RoblesFonseca","Miranda Lopez Castaño","Pablo Aguirre Santacana","Laura Trimiño Serra","Esteban Flores Jimenez"]
code_list = ["634SUV-76","939CFO-44","274MAR-43","389JHL-36","993PRZ-12","834ASD-86","783JHM-54","945GZT-75"]
game_list = ["Tennis","Ping-Pong","Indoor Football","Chess","Basketball","Swimming"]
letrasDni = ['T','R','W','A','G','M','Y','F','P','D','X','B','N','J','Z','S','Q','V','H','L','C','K','E']

summer_camp_students = {}
student_data = {}

cabecera = "***Welcome to the Casal WeWantLearnProgramming***\n" + "\n1)Init Data\n2)Find Users\n3)List Users\n4)dni\n5)Exit\n"
cabeceraL = "Casal WeWantLearnProgramming".center(70,"*")+"\n"+"code".ljust(10)+"DNI".ljust(15)+"Name".rjust(15)+"games".rjust(20)\
                                  +"\n"+"*"*70+"\n"
flg_00 = True
flg_01 = False
flg_02 = False
flg_03 = False
flg_04 = False
Salir = False

while not Salir == True:
    while flg_00:

        print(cabecera)

        opc = input("Option:\n")

        if not opc.isdigit():
            print("Numeric Entries Only")
        elif int(opc) not in range(1, 6):
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
                flg_03 = True
                flg_00 = False

            if opc == 4:
                flg_04 = True
                flg_00 = False

            if opc == 5:
                Salir = True
                flg_00 = False

    while flg_01:
        code_elegido = []
        nombre_elegido = []
        for i in range (5):
            code_random = random.randint(0,len(code_list)-1)
            code = code_list[code_random]
            if code in code_elegido:
                code_random = random.randint(0,len(code_list)-1)
                code = code_list[code_random]
                code_elegido.append(code)

            else:
                code_elegido.append(code)

            #print(code_list)

            dni_num =''
            for i in range(8):
                dni_num += str(random.randint(1,9))

            dni = dni_num + letrasDni[int(dni_num)%23]
            #print(dni)



            nom_random = random.randint(0,len(name_list)-1)
            name = name_list[nom_random]

            if name in nombre_elegido:
                nom_random = random.randint(0,len(name_list)-1)
                name = name_list[nom_random]
                nombre_elegido.append(name)
            else:
                nombre_elegido.append(name)

                #print(name_list)

            antiquity = random.randint(1,10)

            games = []
            cant_games = random.randint(1,len(game_list)-1)

            for cantidad in range(cant_games):
                if len(game_list) == 1:
                    game_random = 0
                else:
                    game_random = random.randint(0,len(game_list)-1)

                if not game_list[game_random] in games:
                    game = game_list[game_random]
                    games.append(game)
                else:
                    game_random = random.randint(0,len(game_list))
            #print(games)
            student_data = {'dni':dni,'name':name,'antiquity':antiquity,'games':games}
            summer_camp_students [code] = student_data
        print(summer_camp_students)
        print("\n")
        flg_00 = True
        flg_01 = False


    while flg_02:

        cabecera2 = "Find Users".center(60,"*")+"\n\n1)Find by DNI\n2)Find by Name\n3)Find by Game\n4)Exit\n"

        print(cabecera2)

        opc = input("Option:\n")

        if not opc.isdigit():
            print("Numeric Entries Only")
        elif int(opc) not in range(1, 5):
            print("Incorrect Option")
        else:
            opc = int(opc)
            if opc == 4:
                flg_00 = True
                flg_02 = False
            if opc == 1:
                datos = ''
                dni_buscar = input("Enter dni to find\n")
                for code in summer_camp_students:
                    if dni_buscar in summer_camp_students[code]["dni"]:
                        datos += "-"*70 +"\n"+code.ljust(10) + summer_camp_students[code]["dni"].ljust(15) + summer_camp_students[code]["name"].rjust(20) \
                                 + summer_camp_students[code]["games"][0].rjust(25) + "\n"
                        if len(summer_camp_students[code]["games"]) > 1:
                            for i in range(1, len(summer_camp_students[code]["games"])):
                                datos += " ".ljust(50) + summer_camp_students[code]["games"][i].rjust(20) + "\n"

                print(cabeceraL + datos)




            if opc == 2:
                datos = ''
                nom_buscar = input("Enter name to find\n")
                for code in summer_camp_students:
                    if nom_buscar.lower() in summer_camp_students[code]["name"].lower():
                        datos += "-"*70 +"\n"+code.ljust(10) + summer_camp_students[code]["dni"].ljust(15) + summer_camp_students[code]["name"].rjust(20) \
                                 + summer_camp_students[code]["games"][0].rjust(25) + "\n"
                        if len(summer_camp_students[code]["games"]) > 1:
                            for i in range(1, len(summer_camp_students[code]["games"])):
                                datos += " ".ljust(50) + summer_camp_students[code]["games"][i].rjust(20) + "\n"

                print(cabeceraL + datos)



            if opc == 3:
                datos = ''
                joc_buscar = input("Enter game to find\n")

                for code in summer_camp_students:
                    for game in range(len(summer_camp_students[code]["games"])):
                        if joc_buscar in summer_camp_students[code]["games"][game]:
                            datos += "-"*70 +"\n"+code.ljust(10) + summer_camp_students[code]["dni"].ljust(15) + summer_camp_students[code]["name"].rjust(20) \
                                     + summer_camp_students[code]["games"][0].rjust(25) + "\n"

                            if len(summer_camp_students[code]["games"]) > 1:
                                for i in range(1, len(summer_camp_students[code]["games"])):
                                    datos += " ".ljust(50) + summer_camp_students[code]["games"][i].rjust(20) + "\n"

                print(cabeceraL + datos)


    while flg_03:
        cabecera3 = "List Users".center(60,"*")+"\n\n1)List by Code Letters\n2)List by DNI\n3)List by amount of Games\n4)Exit\n"


        print(cabecera3)
        opc = input("Option:\n")

        if not opc.isdigit():
            print("Numeric Entries Only")
        elif int(opc) not in range(1, 5):
            print("Incorrect Option")
        else:
            opc = int(opc)
            if opc == 4:
                flg_00 = True
                flg_03 = False

            code_alumn = list(summer_camp_students.keys())
            if opc == 1:
                datos = ''
                # print(code_alumn)

                for pasada in range(len(code_alumn)-1):
                    for i in range(len(code_alumn)-1-pasada):
                        if (code_alumn[i])[3:] > (code_alumn[i+1])[3:]:
                            aux = code_alumn[i]
                            code_alumn[i] = code_alumn[i+1]
                            code_alumn[i+1] = aux

                for code in code_alumn:
                    datos += "-"*70 +"\n"+code.ljust(10) + summer_camp_students[code]["dni"].ljust(15) + summer_camp_students[code]["name"].rjust(18) \
                                     + summer_camp_students[code]["games"][0].rjust(23) + "\n"

                    if len(summer_camp_students[code]["games"]) > 1:
                        for i in range(1, len(summer_camp_students[code]["games"])):
                            datos += " ".ljust(50) + summer_camp_students[code]["games"][i].rjust(20) + "\n"

                print(cabeceraL + datos)




            if opc == 2:
                datos = ''
                # print(code_alumn)
                for pasada in range(len(code_alumn)-1):
                    for j in range(len(code_alumn)-1 -pasada):
                        if summer_camp_students[code_alumn[j]]["dni"] > summer_camp_students[code_alumn[j+1]]["dni"]:
                            aux = code_alumn[j]
                            code_alumn[j] = code_alumn[j+1]
                            code_alumn[j+1] = aux
                # print(code_alumn)

                for code in code_alumn:
                    datos += "-"*70 +"\n"+code.ljust(10) + summer_camp_students[code]["dni"].ljust(15) + summer_camp_students[code]["name"].rjust(20) \
                                     + summer_camp_students[code]["games"][0].rjust(25) + "\n"

                    if len(summer_camp_students[code]["games"]) > 1:
                        for i in range(1, len(summer_camp_students[code]["games"])):
                            datos += " ".ljust(50) + summer_camp_students[code]["games"][i].rjust(20) + "\n"
                print(cabeceraL + datos)


            if opc == 3:
                datos = ''
                #print(code_alumn)
                for pasada in range(len(code_alumn)-1):
                    for j in range(len(code_alumn)-1 -pasada):
                        if len(summer_camp_students[code_alumn[j]]["games"]) > len(summer_camp_students[code_alumn[j+1]]["games"]):
                            aux = code_alumn[j]
                            code_alumn[j] = code_alumn[j+1]
                            code_alumn[j+1] = aux
                #print(code_alumn)

                for code in code_alumn:
                    datos += "-"*70 +"\n"+code.ljust(10) + summer_camp_students[code]["dni"].ljust(15) + summer_camp_students[code]["name"].rjust(20) \
                                     + summer_camp_students[code]["games"][0].rjust(25) + "\n"

                    if len(summer_camp_students[code]["games"]) > 1:
                        for i in range(1, len(summer_camp_students[code]["games"])):
                            datos += " ".ljust(50) + summer_camp_students[code]["games"][i].rjust(20) + "\n"
                print(cabeceraL + datos)


    while flg_04:
        #OTRA FORMA DE HACERLO ES GENERAR DNIS EN UNA LISTA Y USAR ESA EN EL CODIGO PRINCIPAL
        while True:
            opc = input("Enter per generar el dni, s para salir:")
            if opc.lower() == "s":
                break

            dni_num =''

            for i in range(8):
                dni_num += str(random.randint(1,9))
                dni = dni_num + letrasDni[int(dni_num)%23]
            print(dni)

        if opc.lower() == "s":
            flg_00 = True
            flg_04 = False










