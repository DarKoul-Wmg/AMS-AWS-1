def ex1(tupla,excepcions =("A",)):
    #Comprobaciones de tipos = tupla
    try:
        if not type(tupla) is tuple:
            raise ValueError("The options have to be a tuple")

        elif not type(excepcions) is tuple:
            raise ValueError("The exceptions have to be a tuple")
        #Comprobar len
        elif not len(tupla) >= 2:
            raise ValueError("The minimun length of the options are 2")

    except ValueError as error:
        print(error)
        quit() #Return devuelve un none

    #Menu
    while True:
        menu =""
        for i in range(len(tupla)):
            menu += str(i+1) +") "+"{}\n".format(tupla[i])

        print(menu)

        try:
            opc = input("Option: ")
            if opc in excepcions:
                return opc

            if not opc.isdigit(): #Value error1
                raise ValueError("The option is not a number and is not in exceptions")

            if int(opc) < 1 or int(opc) > len(tupla) and not int(opc) in excepcions: #Value error2
                raise ValueError("The option is out of range and not in exceptions")

            else:
                return int(opc)

        except ValueError as error: #Capturar error
            print(error)
            input("Enter to continue")



tupla = ("opcion1","opcion2","opcion3")

resultado = ex1(tupla,excepcions=("c","10",11))
print(resultado)
