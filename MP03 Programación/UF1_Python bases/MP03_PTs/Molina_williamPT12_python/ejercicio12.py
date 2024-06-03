import math

menu00 = "1. Introduir el primer vector\n2. Introduir el segon vector\n3. Calcular la suma\n4. Calcular la diferencia\n" \
         "5. Calcular el producte escalar\n6. Calcular el producte vectorial\n7. Calcular l’angle (en graus) entre ells\n" \
         "8. Calcula la longitud\n9. Finalitzar"

menu04 = "1. Primer vector menys segon vector\n2. Segon vector menys primer vector"

menu06 = ""

menu08 = "1. Calcular longitud del primer vector\n2. Calcular longitud del segon vector"

vector1 = None
vector2 = None

while True:
    print(menu00)
    opc = input("Selecciona una opció: \n")

    if opc == "1":
        # Introducir el primer vector
        x = float(input("Introdueix la coordenada x del primer vector: "))
        y = float(input("Introdueix la coordenada y del primer vector: "))
        z = float(input("Introdueix la coordenada z del primer vector: "))
        vector1 = (x, y, z)
        print(f"Primer vector introduït: {vector1}\n")

    elif opc == "2":
        # Introducir el segundo vector
        x = float(input("Introdueix la coordenada x del segon vector: "))
        y = float(input("Introdueix la coordenada y del segon vector: "))
        z = float(input("Introdueix la coordenada z del segon vector: "))
        vector2 = (x, y, z)
        print(f"Segon vector introduït: {vector2}\n")

    elif opc == "3":
        # Calcular la suma
        if vector1 and vector2:
            suma = (vector1[0] + vector2[0], vector1[1] + vector2[1], vector1[2] + vector2[2])
            print(f"La suma dels vectors és: {suma}\n")
        else:
            print("Cal introduir els dos vectors abans de calcular la suma.\n")

    elif opc == "4":
        # Calcular la diferencia
        if vector1 and vector2:
            print(menu04)
            opc_dif = input("Selecciona una opció: ")

            if opc_dif == "1":
                diferencia = (vector1[0] - vector2[0], vector1[1] - vector2[1], vector1[2] - vector2[2])
                print(f"La diferencia entre els vectors és: {diferencia}\n")
            elif opc_dif == "2":
                diferencia = (vector2[0] - vector1[0], vector2[1] - vector1[1], vector2[2] - vector1[2])
                print(f"La diferencia entre els vectors és: {diferencia}\n")
            else:
                print("Opció invàlida.")
        else:
            print("Cal introduir els dos vectors abans de calcular la diferència.")

    elif opc == "5":
        # Calcular el producto escalar
        if vector1 and vector2:
            producto_escalar = vector1[0] * vector2[0] + vector1[1] * vector2[1] + vector1[2] * vector2[2]
            print(f"El producte escalar dels vectors és: {producto_escalar}\n")
        else:
            print("Cal introduir els dos vectors abans de calcular el producte escalar.")

    elif opc == "6":
        # Calcular el producto vectorial
        if vector1 and vector2:
            producto_vectorial = (
                vector1[1] * vector2[2] - vector1[2] * vector2[1],
                vector1[2] * vector2[0] - vector1[0] * vector2[2],
                vector1[0] * vector2[1] - vector1[1] * vector2[0]
            )
            print(f"El producte vectorial dels vectors és: {producto_vectorial}\n")
        else:
            print("Cal introduir els dos vectors abans de calcular el producte vectorial.")

    elif opc == "7":
        # Calcular el ángulo entre los vectores
        if vector1 and vector2:
            dot_product = vector1[0] * vector2[0] + vector1[1] * vector2[1] + vector1[2] * vector2[2]
            magnitude1 = math.sqrt(vector1[0]**2 + vector1[1]**2 + vector1[2]**2)
            magnitude2 = math.sqrt(vector2[0]**2 + vector2[1]**2 + vector2[2]**2)
            angle = math.degrees(math.acos(dot_product / (magnitude1 * magnitude2)))
            print(f"L'angle (en graus) entre els vectors és: {angle}\n")
        else:
            print("Cal introduir els dos vectors abans de calcular l'angle.")

    elif opc == "8":
        # Calcular la longitud
        if vector1 and vector2:
            print(menu08)
            opc_longitud = input("Selecciona una opció: ")

            if opc_longitud == "1":
                longitud = math.sqrt(vector1[0]**2 + vector1[1]**2 + vector1[2]**2)
                print(f"La longitud del primer vector és: {longitud}\n")
            elif opc_longitud == "2":
                longitud = math.sqrt(vector2[0]**2 + vector2[1]**2 + vector2[2]**2)
                print(f"La longitud del segon vector és: {longitud}\n")
            else:
                print("Opció invàlida.")
        else:
            print("Cal introduir els dos vectors abans de calcular la longitud.\n")

    elif opc == "9":
        # Finalizar
        print("Programa finalitzat.")
        break

    else:
        print("Opció invàlida. Torna a seleccionar una opció.")

