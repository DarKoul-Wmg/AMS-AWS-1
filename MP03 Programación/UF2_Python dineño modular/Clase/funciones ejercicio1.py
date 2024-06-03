
cabecera = "Menu00".center(30,"*")
menu00= (cabecera,"opc1","opc2","opc3","opc4")

def misMenus(tupla_menus):
    if cabecera != "":
        print(cabecera)
    str_menu = ""
    for i in range(1,len(tupla_menus)):
        str_menu += str(i)+")"+tupla_menus[i]+"\n"

    print(str_menu)
    opc = ""
    # while not ( opcion.isdigit() and opcion in range(1,len(tupla_menus)+1)):
    while True:
        opc = input("Opcion:\n")
        if not opc.isdigit():
            print("Solo valores numericos")

        elif not int(opc) in range(1,len(tupla_menus)):
            print("Opción fuera de rango")
        else:
            return int(opc)


devolucion_opcion = misMenus(menu00)
print("devolucion = ",devolucion_opcion)



