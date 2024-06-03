cabecera = "Menu00".center(30,"-")
tupla_Opciones = (cabecera,"opcion1","opcion2","opcion3","opcion4","opcion5")


def MenusF(tupla_Opciones):
    if tupla_Opciones[0] != "":
        print(tupla_Opciones[0])
    string_Menu = ""

    for i in range(1,len(tupla_Opciones)):
        string_Menu += str(i)+")"+tupla_Opciones[i]+"\n"

    print(string_Menu)
    opcion = ""

    while True:

        try:
            opc = int(input("Opcion:"))
            #assert 1 <= opc <= len(tupla_Opciones)-1
            if not 1 <= opc <= len(tupla_Opciones)-1:
                # COMO ASSERT, PERO YO ELIGO EL TIPO DE EXCEPCION

                raise ZeroDivisionError("LA opción no esta contemplada")
            return opc

        except ValueError: #Hacemos petar el codigo con algo que no sea un num para ver el tipo de error
            print("La opcion ha de ser numérica")

        except AssertionError: #Hacemos petar el codigo con num fuera de rango para capturar el error
            print("Numero esta fuera de rango")

        except ZeroDivisionError as error: #Capturar error y usarlo como variable
            print("NUM esta fuera de rango ")
            print(error)

devolOpcion = MenusF(tupla_Opciones)
print("devolucion = ", devolOpcion)