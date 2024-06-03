def funcionA(cadena):
    if len(cadena)>0:
        print(cadena[0])
        cadena = cadena[1:]
        funcionA(cadena)

cadena = "abcd"
funcionA(cadena)