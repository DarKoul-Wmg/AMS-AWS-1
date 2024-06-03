cabecera = "Menu00".center(30,"-")
tupla_Menus = (cabecera,"opcion1","opcion2","opcion3","opcion4","opcion5")


def MenusF(tupla_Menus):
    if tupla_Menus[0] != "":
        print(tupla_Menus[0])
    string_Menu = ""

    for i in range(1,len(tupla_Menus)):
        string_Menu += str(i)+")"+tupla_Menus[i]+"\n"

    print(string_Menu)
    opcion = ""
    while True:
        opcion = input("Opcion:\n")
        if not opcion.isdigit():
            print("Solo valores numéricos")

        elif not int(opcion) in range(1,len(tupla_Menus)):
            print("Opcion fuera de rango")

        else:
            return int(opcion)

devolOpcion = MenusF(tupla_Menus)
print("devolucion = ", devolOpcion)