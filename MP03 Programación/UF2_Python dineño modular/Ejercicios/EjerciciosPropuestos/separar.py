tuplaMenu = "opcion1;opcion2;opcion;opcion4;opcion5"

opciones = []
inicio = 0

while True:
    final = tuplaMenu.find(";", inicio)
    if final == -1: #Cuando no queden ;
        opciones.append(tuplaMenu[inicio:])
        break
    opciones.append(tuplaMenu[inicio:final])
    inicio = final + 1


print(opciones)
