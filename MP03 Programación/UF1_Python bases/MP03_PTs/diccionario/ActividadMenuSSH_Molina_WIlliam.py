
# acceso: ssh -i /path hasta la clave privada/alumne2324_rsa -p 20123 practica1@ieticloudpro.ieti.cat

letrasDni = ['T','R','W','A','G','M','Y','F','P','D','X','B','N','J','Z','S','Q','V','H','L','C','K','E']
usuario1 = {"nombre":"Pedro Javier Morales",  "direccion": "Flores 36 8º 2º", "tfn":["+0034345345345"],"compras":[1234,423,23]}
usuario2 = {"nombre":"Maite Lopez Miravet", "direccion":"Balames 31 1º 2º","tfn":["+0034234234235","+0034239999235"],"compras":[12344]}
usuario3 = {"nombre":"Marta Garcia Suarez",  "direccion":"Valencia 21 3º 1º","tfn": ["+0075766576575"],"compras":[34,423,23,6]}
usuarios = {"47474747X":usuario1,"24536425T":usuario2,"76767676H":usuario3}



cabecera = "******Welcome to the User Management Program******\n"+"\n"+"1)Create User\n"+\
           "2)Modify User\n"+"3)Show User\n"+"4)Find User\n"+"5)List User\n"+"6)Exir\n"


while True:

    print(cabecera)
    opcion = input("Option:\n")
    if opcion.isdigit():
        opcion = int(opcion)

        if opcion == 1:
            dni =''
            name =''
            surname =''
            address = ''
            tlf = ''
            while True:
                cabecera1 = f"DNI:* {dni}\n"+f"Name:* {name}\n"+f"Surname:* {surname}\n"+f"Address:* {address}\n"+\
                            f"Tfn: {tlf}\n"+"\n"+"1)Enter DNI\n"+"2)Enter Name\n"+"3)Enter Surname\n"+"4)Enter Addres\n"+\
                            "5)Enter Tfn\n"+"6)Save User\n"+"7)Go Back"
                print(cabecera1)

                opcion = input("Option:\n")
                if opcion.isdigit():
                    opcion = int(opcion)

                    if opcion == 1:#DNI

                        dni_correcto = False
                        while not dni_correcto:
                            dni = input("DNI: ")
                            if len(dni) !=9:
                                print("DNI incorrecto, muy corto")
                            elif not dni[0:8].isdigit():
                                print("DNI Incorrecto, demasiadas letras")
                            elif not dni[8]==letrasDni[int(dni[0:8])%23]:
                                print("DNI Incorrecto, letra incorrecta")
                            else:
                                print("DNI correcto")
                                dni = dni.upper()
                                dni_correcto = True

                    elif opcion == 2:#Nombre
                        name = input("Introduce el nombre: ")
                        while not name.replace(" ", "").isalpha():
                            print(f'{name} no es un nombre valido')
                            name = input("Introduce el nombre otra vez")
                        else:
                            print('Nombre correcto')

                    elif opcion == 3:#Apellido
                        surname = input("Introduce el apellido: ")
                        while not surname.replace(" ", "").isalpha():
                            print(f'"{surname}" no es un apellido valido')
                            surname = input("Vuelve a introducir el apellido")
                        else:
                            print('Apellido correcto')

                    elif opcion == 4:#Dirección
                        address = input("Introduce tu dirección:")
                        while not len(address) > 0:
                            print('Dirección incorrecta')
                            address = input("Introduce tu dirección:")
                        else:
                            print("Dirección valida")

                    elif opcion == 5:#Telefonos
                        tlf = []

                        while True:
                            telefono = input("Introduce un número de teléfono o presiona Enter para salir: ")

                            if telefono == '':
                                break

                            elif len(telefono) == 9 and telefono.isdigit():
                                print("Teléfono válido")
                                telefono = "+0034"+telefono
                                tlf.append(telefono)
                            else:
                                print("Teléfono no válido")

                        print("Números de teléfono ingresados:", tlf)

                    elif opcion == 6:#Guardar usuario en diccionario
                        if dni =="" and name =="" and surname =="" and address =="":
                            print("Los campos con * son obligatorios")
                        elif dni in usuarios:
                            print("Este DNI ya esta registrado")
                        else:
                            nuevo_usuario = {"nombre":name+" "+surname,  "direccion":address, "tfn":tlf,"compras":[]}
                            usuarios[dni] = nuevo_usuario

                    elif opcion == 7:#Back
                        break
                    else:
                        print("Opción no válida. Por favor, elige una opción válida.")

                else:
                    print("Introduce una opcion numerica")


        elif opcion == 2:
            print("Dime el DNI del usuario a modificar:")
            dni = input("DNI:")
            if dni in usuarios:
                while True:

                    cabecera4 ='*'*10+" Menu 2 - Modify User"+'*'*10+ "\n1)Add purchase\n" + "2)Add tfn number\n" + \
                               "3)Del tfn number\n" + "4)Change Address\n"+ "5)Go Back\n"
                    print(cabecera4)
                    opcion = input("Option:\n")
                    if opcion.isdigit():
                        opcion = int(opcion)
                        if opcion == 1:#+Compras
                            compra = int(input("Introduce el valor de la compra:"))
                            usuarios[dni]['compras'].append(compra)
                            print(f"Se ha añadido el valor: {compra} a {dni} - {usuarios[dni]['nombre']}\n")

                        elif opcion == 2:# +tfn
                            nuevo_tfn = input("Introduce el telefono que quieres añadir):")
                            if len(nuevo_tfn) != 9:
                                print("El telefono tiene que tener una longitud de 9")
                            elif not nuevo_tfn.isdigit():
                                print("Un telefono solo puede tener numeros...")
                            else:
                                nuevo_tfn = "+0034"+nuevo_tfn
                                usuarios[dni]['tfn'].append(nuevo_tfn)
                                print(f"Se ha añadido el tfn: {nuevo_tfn} a {dni} - {usuarios[dni]['nombre']}\n")

                        elif opcion == 3:# -tfn
                            borrar_telefono =input("Introduce el numero de telefono que quieres eliminar (recuerda añadir el"
                                                   "prefijo +0034):")
                            if borrar_telefono in usuarios[dni]['tfn']:
                                usuarios[dni]['tfn'].remove(borrar_telefono)
                                print(f"Se ha eliminado el tfn: {borrar_telefono} a {dni} - {usuarios[dni]['nombre']}\n")



                        elif opcion == 4:# cambiar Direccion
                            nueva_direccion = input("Introduce la nueva dirección: ")
                            usuarios[dni]['direccion'] = nueva_direccion
                            print(f"Se ha modificado la direccion: {nueva_direccion} a {dni} -"
                                  f" {usuarios[dni]['nombre']}\n")


                        elif opcion == 5:
                            break

                        else:
                            print("Opción no válida. Por favor, elige una opción válida.")

                    else:
                        print("Introduce una opcion numerica")


            elif len(dni) !=9:
                print("Longitud incorrecta")

            elif not dni[0:8].isdigit():
                print("Demasiadas letras")
            else:
                print("El DNI introducido no pertenece a ningun cliente")


        elif opcion == 3:
            for dni, usuario in usuarios.items():
                print(f"DNI: {dni}")
                print(f"Nombre: {usuario['nombre']}")
                print(f"TFN: {(usuario['tfn'])}")
                print("\nEnter to continue")
                input()


        elif opcion == 4:
            while True:
                cabecera4 = "1)Find by DNI\n" + "2)Find by Name\n" + "3)Go Back"
                print(cabecera4)
                opcion = input("Option:\n")
                if opcion.isdigit():
                    opcion = int(opcion)

                    if opcion == 1:#Buscar DNI
                        dni_a_buscar = input("DNI para buscar al Usuario: ")
                        dni_encontrado = [(dni, usuario) for dni, usuario in usuarios.items() if dni_a_buscar in dni]
                        if dni_encontrado:
                            print("*"*140)
                            print("DNI"+" "*14+"Name"+" "*26+"Address"+" "*33+"Tfn"+" "*33+"Total Purchases")
                            print("*"*140)
                            for dni, usuario in dni_encontrado:
                                telefono = usuario['tfn'][0] if usuario['tfn'] else ''
                                compras = usuario['compras'][0] if usuario['compras'] else ''
                                print(f"{dni.ljust(14)}{usuario['nombre'].ljust(30)}{usuario['direccion'].ljust(40)}" \
                                f"{telefono.ljust(45)}{str(compras).ljust(55)}\n")
                        else:
                            print(f"No se encontró ningun usuario con ese DNI.\n")

                    elif opcion == 2:#Buscar Nombre
                        nombre_a_buscar = input("Nombre para buscar al usuario: ")
                        nombre_encontrado = [(dni, usuario) for dni, usuario in usuarios.items() if nombre_a_buscar in usuario['nombre']]
                        if nombre_encontrado:
                            print("*"*140)
                            print("DNI"+" "*14+"Name"+" "*26+"Address"+" "*33+"Tfn"+" "*33+"Total Purchases")
                            print("*"*140)
                            for dni, usuario in nombre_encontrado:
                                telefono = usuario['tfn'][0] if usuario['tfn'] else ''
                                compras = usuario['compras'][0] if usuario['compras'] else ''
                                print(f"{dni.ljust(14)}{usuario['nombre'].ljust(30)}{usuario['direccion'].ljust(40)}" \
                                      f"{telefono.ljust(45)}{str(compras).ljust(55)}\n")
                        else:
                            print(f"No se encontró ningun usuario con ese nombre.\n")

                elif opcion == 3:
                    break
                else:
                    print("Opción no válida. Por favor, elige una opción válida.")


        elif opcion == 5:
            while True:
                cabecera4 ='*'*10+" Menu 5 - List Users"+'*'*10+ "\n1)List by DNI \n" + "2)List by Name\n" + \
                               "3)List by Address\n" + "4)Total Purchase\n"+ "5)Go Back\n"
                print(cabecera4)
                opcion = input("Option:\n")
                if opcion.isdigit():
                    opcion = int(opcion)

                    if opcion == 1:#Ordenado por DNI
                        lista_usuarios = list(usuarios.items())
                        n = len(lista_usuarios)

                        for i in range(n - 1):
                            for j in range(0, n - i - 1):
                                dni_i = lista_usuarios[j][0]
                                dni_j = lista_usuarios[j + 1][0]

                                if dni_i > dni_j:
                                    lista_usuarios[j], lista_usuarios[j + 1] = lista_usuarios[j + 1], lista_usuarios[j]

                        print("*" * 140)
                        print("DNI" + " " * 14 + "Name" + " " * 26 + "Address" + " " * 33 + "Tfn" + " " * 33 + "Total Purchases")
                        print("*" * 140)
                        for dni, usuario in lista_usuarios:
                            todos_tfn = " ".join(usuario['tfn'])
                            total_compras = sum(usuario['compras'])
                            print(f"{dni.ljust(14)}{usuario['nombre'].ljust(30)}{usuario['direccion'].ljust(40)}"
                                  f"{todos_tfn.ljust(45)}{str(total_compras).ljust(55)}\n")



                    elif opcion == 2:#Ordenado por Nombre
                        lista_usuarios = list(usuarios.items())
                        n = len(lista_usuarios)

                        for i in range(n - 1):
                            for j in range(0, n - i - 1):
                                nombre_i = lista_usuarios[j][1]['nombre']
                                nombre_j = lista_usuarios[j + 1][1]['nombre']

                                if nombre_i > nombre_j:
                                    lista_usuarios[j], lista_usuarios[j + 1] = lista_usuarios[j + 1], lista_usuarios[j]

                        print("*" * 140)
                        print("DNI" + " " * 14 + "Name" + " " * 26 + "Address" + " " * 33 + "Tfn" + " " * 33 + "Total Purchases")
                        print("*" * 140)
                        for dni, usuario in lista_usuarios:
                            todos_tfn = " ".join(usuario['tfn'])
                            total_compras = sum(usuario['compras'])
                            print(f"{dni.ljust(14)}{usuario['nombre'].ljust(30)}{usuario['direccion'].ljust(40)}"
                                  f"{todos_tfn.ljust(45)}{str(total_compras).ljust(55)}\n")


                    elif opcion == 3:#Ordenado por Direccion
                        lista_usuarios = list(usuarios.items())
                        n = len(lista_usuarios)

                        for i in range(n - 1):
                            for j in range(0, n - i - 1):
                                direccion_i = lista_usuarios[j][1]['direccion']
                                direccion_j = lista_usuarios[j + 1][1]['direccion']

                                if direccion_i > direccion_j:
                                    lista_usuarios[j], lista_usuarios[j + 1] = lista_usuarios[j + 1], lista_usuarios[j]

                                    opc = lista_usuarios[j]
                                    lista_usuarios[j] = lista_usuarios[j + 1]
                                    lista_usuarios[j + 1] = opc

                        print("*" * 140)
                        print("DNI" + " " * 14 + "Name" + " " * 26 + "Address" + " " * 33 + "Tfn" + " " * 33 + "Total Purchases")
                        print("*" * 140)
                        for dni, usuario in lista_usuarios:
                            todos_tfn = ""
                            for tfn in usuario['tfn']:
                                todos_tfn += f"{tfn} "
                            total_compras = sum(usuario['compras'])
                            print(f"{dni.ljust(14)}{usuario['nombre'].ljust(30)}{usuario['direccion'].ljust(40)}"
                                  f"{todos_tfn.ljust(45)}{str(total_compras).ljust(55)}\n")

                    elif opcion == 4:#Ordenado por Total de Compras
                        lista_usuarios = list(usuarios.items())
                        n = len(lista_usuarios)

                        for i in range(n - 1):
                            for j in range(0, n - i - 1):
                                total_purchase_i = sum(lista_usuarios[j][1]['compras'])
                                total_purchase_j = sum(lista_usuarios[j + 1][1]['compras'])

                                if total_purchase_i < total_purchase_j:
                                    lista_usuarios[j], lista_usuarios[j + 1] = lista_usuarios[j + 1], lista_usuarios[j]

                        print("*" * 140)
                        print("DNI" + " " * 14 + "Name" + " " * 26 + "Address" + " " * 33 + "Tfn" + " " * 33 + "Total Purchases")
                        print("*" * 140)
                        for dni, usuario in lista_usuarios:
                            todos_tfn = ""
                            for tfn in usuario['tfn']:
                                todos_tfn += f"{tfn} "
                            total_compras = sum(usuario['compras'])
                            print(f"{dni.ljust(14)}{usuario['nombre'].ljust(30)}{usuario['direccion'].ljust(40)}"
                                  f"{todos_tfn.ljust(45)}{str(total_compras).ljust(55)}")




                    elif opcion == 5:
                        break

                    else:
                        print("Opción no válida. Por favor, elige una opción válida.")

                else:
                    print("Introduce una opcion numerica")

        elif opcion == 6:
            print("Cerrando programa...")
            break



        else:
            print("Opción no válida. Por favor, elige una opción válida.\n")
    else:
        print("Introduce una opcion numerica\n")
