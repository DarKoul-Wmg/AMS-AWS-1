cabecera = "Menu01".center(30,"-")
tuplaMenu = "opcion1;opcion2;opcion3;opcion4;opcion5"

def MenuF (tuplaMenu):
    opciones = []
    inicio = 0
    stringMenu = ""
    while True:
        final = tuplaMenu.find(";", inicio)
        if final == -1: #Cuando no queden ;
            opciones.append(tuplaMenu[inicio:])
            break
        opciones.append(tuplaMenu[inicio:final])
        inicio = final + 1

    #print(opciones)
    if cabecera != "":
        print(cabecera)

    for opc in range(0,len(opciones)):
        stringMenu += str(opc+1)+")"+opciones[opc]+"\n"

    print(stringMenu)
    while True:
        opcion = input("Opcion:\n")
        if not opcion.isdigit():
            print("Solo valores numéricos")

        elif not int(opcion) in range(1,len(opciones)):
            print("Opcion fuera de rango")
        else:
            return int(opcion)

devOpcion = MenuF(tuplaMenu)
print("devolucion = ",devOpcion)


