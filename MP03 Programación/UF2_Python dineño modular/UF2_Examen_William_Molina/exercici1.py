def ex1(string,excepcions =("A",)):
    #Comprobaciones de tipos = tupla
    try:

        if not type(string) is str:
            raise ValueError("The options have to be a string")

        elif not type(excepcions) is tuple:
            raise ValueError("The exceptions have to be a tuple")

        elif not string.count(";")>1:
            raise ValueError("The minimun amount of options are 2")

    except ValueError as error:
        print(error)
        quit() #Return devuelve un none

    #Menu
    while True:
        #creamos una lista con las opciones iterando la string
        lista=[]
        total_opc = string.count(";")
        for i in range(total_opc):
            pos = string.index(";")
            lista.append(string[:pos])
            #print(lista)
            string = string[pos+1:]

        menu =""
        for i in range(len(lista)):
            menu += str(i+1) +") "+"{}\n".format(lista[i])
        print(menu)

        try:
            opc = input("Option: ")
            if opc in excepcions:
                return opc

            if not opc.isdigit(): #Value error1
                raise IndexError("The option is not a number and is not in exceptions")

            if int(opc) < 1 or int(opc) > len(lista) and not int(opc) in excepcions: #Value error2
                raise IndexError("The option is out of range and not in exceptions")

            else:
                return int(opc)

        except ValueError as error: #Capturar error
            print(error)
            quit() #no devuelve none
        except IndexError as error:
            print(error)
            input("Enter to continue")


string = "opcion1;opcion2;opcion3;"

resultado = ex1(string,excepcions=("c","d",10))
print(resultado)



