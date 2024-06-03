import random
tipus={
    1:{'tipus':"Tipus1","subtipus":'Planta',"Moviment":"Normal",'categoria':'Categoria0' },
    2:{'tipus':"Tipus2","subtipus":'Veri',"Moviment":'Fisic','categoria':'Categoria0'},
    3:{'tipus':"Tipus2","subtipus":'Veri',"Moviment":'Especial','categoria':'Platino'},
    4:{'tipus':"Tipus2", "subtipus":'Veri', "Moviment": 'Especial', 'categoria': 'Rubi'},
    5:{'tipus':"Tipus2", "subtipus":'Veri', "Moviment": 'Especial', 'categoria': 'Zafir'},
    6:{'tipus':"Tipus2","subtipus":'foc',"Moviment":"Normal",'categoria':'Categoria0'},
    7:{'tipus':"Tipus2","subtipus":'volador',"Moviment":"Normal",'categoria':'Categoria0'},
    8:{'tipus':"Tipus3","subtipus":'Aigua',"Moviment":"Normal",'categoria':'Categoria0'},
    9:{'tipus':"Tipus3","subtipus":'Bitxo',"Moviment":"Normal",'categoria':'Categoria0'}
}
participants={
    1:{'nom':'pc','punts':12,'numpartides':7,'pokemon':4,'energia':[145,25,36,256,968,9,546]},
    2:{'nom':'Ana123','punts':3,'numpartides':1, 'pokemon':1,'energia':[335,75,326]},
    3:{'nom':'Marta','punts':10,'numpartides':5,'pokemon':3,'energia':[119,358,471,88,44]},
    4:{'nom':'Marta','punts':23,'numpartides':1,'pokemon':3,'energia':[921]},
    5:{'nom':'Marta','punts':57,'numpartides':1,'pokemon':2,'energia':[43]},
    6:{'nom':'pc','punts':2,'numpartides':1,'pokemon':1,'energia':[26]},
    7:{'nom':'pc','punts':2,'numpartides':5,'pokemon':1, 'energia':[64,712,855,269,358]},
    8:{'nom':'Ana123','punts':33,'numpartides':1, 'pokemon':1, 'energia':[329]},
    9:{'nom':'Pokemito','punts':250,'numpartides':1, 'pokemon':3, 'energia':[651]},
    10:{'nom':'Juanito23','punts':14,'numpartides':1, 'pokemon':2, 'energia':[964]},
    11:{'nom':'pokemazo','punts':26,'numpartides':1, 'pokemon':1, 'energia':[836]}
}


menu0 = "1.- Escull pokemon\n2.- Generar pokemon pc\n3.- Començar la batalla.\n4.- Puntuació total de cada participant\n"+\
       "5.- Mostrar els 3 primers guanyadors\n6.- Mostrar el pokemon que més partides ha guanyat\n7.- Sortir"
menu01 = "1.- Tipus1\n2.- Tipus2\n3.- Tipus3\n4.- Atras"
menu012 = "1.- Veri\n2.- Foc\n3.- Volador\n4.- Atras"
menu0121 = "1.- Físic\n2.- Especial\n3.- Atras"
menu01212 = "1.- Platino\n2.- Rubí\n3.- Safir\n4.- Atras"
menu013 = "1.- Aigua\n2.- Bitxo\n3.- Atras"

menu04 = "PUNTUACIÓ TOTAL DE CADA PARTICIPANT\n"+"*"*35
menu05 = "RANKING GUANYADORS"
while True:
    nom = input("Digam el teu nom:\n")
    if len(nom) == 0 or nom.isspace():
        print("Inserta algo")
    elif not nom.isalnum():
        print("Inserta solo letras y numeros")
    elif nom.isalnum():
        break
input("Pulsa para continuar")
#########################################
nommaquina = "PC"
#########################################
while True:
    print(menu0)
    while True:
        opcion = input("Escull una opcio:\n")
        if len(opcion) == 0 or opcion.isspace():
            print("Inserta algo")
        elif not opcion.isdigit():
            print("Inserta solo numeros")
        elif opcion.isalpha():
            print("Inserta solo numeros")
        elif int(opcion) > 0 and int(opcion) < 8:
            opcion = int(opcion)
            break
        else:
            print("Inserta una opcio valida")
    if opcion == 1:
        while True:
            print(menu01)
            while True:
                tipusop = input("Tipus:\n")
                if len(tipusop) == 0 or tipusop.isspace():
                    print("Inserta algo")
                elif not tipusop.isdigit():
                    print("Inserta solo numeros")
                elif tipusop.isalpha():
                    print("Inserta solo numeros")
                elif int(tipusop) >0 and int(tipusop)<5:
                    tipusop=int(tipusop)
                    break
                else:
                    print("Inserta un valor valido")
            if tipusop == 1:
                print(tipus[tipusop]["tipus"],tipus[tipusop]["subtipus"],tipus[tipusop]["Moviment"],tipus[tipusop]["categoria"])
                participants[len(participants)+1] = {"nom":nom,"punts":0,"numpartides":0,"pokemon":1, "energia":[]}
            elif tipusop == 2:
                print(menu012)
                while True:
                    subtipus = input("Subtipus:\n")
                    if len(subtipus) == 0 or subtipus.isspace():
                        print("Inserta algo")
                    elif not subtipus.isdigit():
                        print("Inserta solo numeros")
                    elif subtipus.isalpha():
                        print("Inserta solo numeros")
                    elif int(subtipus) > 0 and int(subtipus) < 5:
                        subtipus = int(subtipus)
                        break
                    else:
                        print("Inserta un valor valido")
                if subtipus == 1:
                    print(menu0121)
                    while True:
                        moviment = input("Subtipus:\n")
                        if len(moviment) == 0 or moviment.isspace():
                            print("Inserta algo")
                        elif not moviment.isdigit():
                            print("Inserta solo numeros")
                        elif moviment.isalpha():
                            print("Inserta solo numeros")
                        elif int(moviment) > 0 and int(moviment) < 4:
                            moviment = int(moviment)
                            break
                        else:
                            print("Inserta un valor valido")
                    if moviment == 1:
                        print(tipus[2]["tipus"], tipus[2]["subtipus"], tipus[2]["Moviment"],
                              tipus[2]["categoria"])
                        participants[len(participants) + 1] = {"nom": nom, "punts": 0, "numpartides": 0, "pokemon": 2,
                                                               "energia": []}
                    elif moviment == 2:
                        print(menu01212)
                        while True:
                            especial = input("Subtipus:\n")
                            if len(especial) == 0 or especial.isspace():
                                print("Inserta algo")
                            elif not especial.isdigit():
                                print("Inserta solo numeros")
                            elif especial.isalpha():
                                print("Inserta solo numeros")
                            elif int(especial) > 0 and int(especial) < 5:
                                especial = int(especial)
                                break
                            else:
                                print("Inserta un valor valido")
                        if especial == 1:
                            print(tipus[3]["tipus"], tipus[3]["subtipus"], tipus[3]["Moviment"],
                                  tipus[3]["categoria"])
                            participants[len(participants) + 1] = {"nom": nom, "punts": 0, "numpartides": 0,
                                                                   "pokemon": 3,
                                                                   "energia": []}
                        elif especial == 2:
                            print(tipus[4]["tipus"], tipus[4]["subtipus"], tipus[4]["Moviment"],
                                  tipus[4]["categoria"])
                            participants[len(participants) + 1] = {"nom": nom, "punts": 0, "numpartides": 0,
                                                                   "pokemon": 4,
                                                                   "energia": []}
                        elif especial == 3:
                            print(tipus[5]["tipus"], tipus[5]["subtipus"], tipus[5]["Moviment"],
                                  tipus[5]["categoria"])
                            participants[len(participants) + 1] = {"nom": nom, "punts": 0, "numpartides": 0,
                                                                   "pokemon": 5,
                                                                   "energia": []}
                        elif especial == 4:
                            break
                    elif moviment == 3:
                        break
                elif subtipus == 2:
                    print(tipus[6]["tipus"], tipus[6]["subtipus"], tipus[6]["Moviment"],
                          tipus[6]["categoria"])
                    participants[len(participants) + 1] = {"nom": nom, "punts": 0, "numpartides": 0, "pokemon": 6,
                                                           "energia": []}
                elif subtipus == 3:
                    print(tipus[7]["tipus"], tipus[7]["subtipus"], tipus[7]["Moviment"],
                          tipus[7]["categoria"])
                    participants[len(participants) + 1] = {"nom": nom, "punts": 0, "numpartides": 0, "pokemon": 7,
                                                           "energia": []}
                elif subtipus == 4:
                    break
            elif tipusop == 3:
                print(menu013)
                while True:
                    subtipus = input("Subtipus:\n")
                    if len(subtipus) == 0 or subtipus.isspace():
                        print("Inserta algo")
                    elif not subtipus.isdigit():
                        print("Inserta solo numeros")
                    elif subtipus.isalpha():
                        print("Inserta solo numeros")
                    elif int(subtipus) > 0 and int(subtipus) < 5:
                        subtipus = int(subtipus)
                        break
                    else:
                        print("Inserta un valor valido")
                if subtipus == 1:
                    print(tipus[8]["tipus"], tipus[8]["subtipus"], tipus[8]["Moviment"],
                          tipus[8]["categoria"])
                    participants[len(participants) + 1] = {"nom": nom, "punts": 0, "numpartides": 0, "pokemon": 8,
                                                           "energia": []}
                elif subtipus == 2:
                    print(tipus[9]["tipus"], tipus[9]["subtipus"], tipus[9]["Moviment"],
                          tipus[9]["categoria"])
                    participants[len(participants) + 1] = {"nom": nom, "punts": 0, "numpartides": 0, "pokemon": 9,
                                                           "energia": []}
            elif tipusop == 4:
                break
            input("Pulsa per continuar")
    elif opcion == 2:
        print("Generant pokemon per PC...")
        tipus = random.randint(1,3)
        if tipus == 1:
            participants[len(participants)+1] = {"nom": "PC", "punts":0, "numpartides":0, "pokemon":1, "energia":[]}
        elif tipus == 2:
            subtipus = random.randint(1,3)
            if subtipus == 1:
                moviment = random.randint(1,2)
                if moviment == 1:
                    participants[len(participants) + 1] = {"nom": "PC", "punts": 0, "numpartides": 0, "pokemon": 2,
                                                           "energia": []}
                elif moviment == 2:
                    categoria = random.randint(1,3)
                    if categoria == 1:
                        participants[len(participants) + 1] = {"nom": "PC", "punts": 0, "numpartides": 0, "pokemon": 3,
                                                               "energia": []}
                    elif categoria == 2:
                        participants[len(participants) + 1] = {"nom": "PC", "punts": 0, "numpartides": 0, "pokemon": 4,
                                                               "energia": []}
                    elif categoria == 3:
                        participants[len(participants) + 1] = {"nom": "PC", "punts": 0, "numpartides": 0, "pokemon": 5,
                                                               "energia": []}
            elif subtipus == 2:
                participants[len(participants) + 1] = {"nom": "PC", "punts": 0, "numpartides": 0, "pokemon": 6,
                                                       "energia": []}
            elif subtipus == 3:
                participants[len(participants) + 1] = {"nom": "PC", "punts": 0, "numpartides": 0, "pokemon": 7,
                                                       "energia": []}
        elif tipus == 3:
            subtipus = random.randint(1,2)
            if subtipus == 1:
                participants[len(participants) + 1] = {"nom": "PC", "punts": 0, "numpartides": 0, "pokemon": 8,
                                                       "energia": []}
            elif subtipus == 2:
                participants[len(participants) + 1] = {"nom": "PC", "punts": 0, "numpartides": 0, "pokemon": 9,
                                                       "energia": []}
        input("PC creat\nPulsa per continuar")
    elif opcion == 3:
        print(3)
    elif opcion == 4:
        print(menu04)
        for i in participants:
            menu041 = str(participants[i]["nom"].upper()).rjust(10) + str(participants[i]["punts"]).rjust(10)
            print(menu041)
        input("Pulsa per continuar")
    elif opcion == 5:
        print(menu05)
        listaKys = []
        listapuntos = []
        for i in participants:
            listaKys.append(i)
            listapuntos.append(participants[i]["punts"])
        for i in range(len(listapuntos) - 1):
            for j in range(len(listapuntos) - i - 1):
                if listapuntos[j] < listapuntos[j + 1]:
                    numero = listapuntos[j]
                    listapuntos[j] = listapuntos[j + 1]
                    listapuntos[j + 1] = numero

                    numero = listaKys[j]
                    listaKys[j] = listaKys[j + 1]
                    listaKys[j + 1] = numero
        listaKys = listaKys[0:3]
        for i in listaKys:
            menu051 = str(participants[i]["nom"]).rjust(10) + str(participants[i]["punts"]).rjust(10)
            print(menu051)
        input("Pulsa per continuar")
    elif opcion == 6:
        print(6)
    elif opcion == 7:
        break