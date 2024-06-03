with open("5origen","r") as origen:
    with open("5destino","w+") as destino:
        contenido = origen.readlines()
        #print(contenido)

        for linea in contenido:
            linea.replace("\n","")
            #print(linea)
            linea_cifrada = ""
            for caracter in linea:
                if caracter.isalpha():
                    if "a" <= caracter.lower() <= "z":
                        valor = ord(caracter)
                        valor +=13
                        #print(valor)
                        valor_nuevo = valor%26
                        #valor_nuevo += ord('a') #sumamos valor para obtener uno valido
                        #print(valor_nuevo)
                        car_cifrado = chr(valor_nuevo)
                        #print(car_cifrado)
                        linea_cifrada += car_cifrado
                else:
                    linea_cifrada += caracter
            #print(linea_cifrada)
            destino.write(linea_cifrada)
        resultado = destino.read()
        print(resultado)

        # for linea in contenido:
        #     linea_cifrada = ""
        #     for caracter in linea:
        #         if caracter.isalpha():
        #             if 'a' <= caracter.lower() <= 'z':
        #                 valor = ord(caracter)
        #                 valor += 13
        #                 if caracter.islower():
        #                     if valor > ord('z'):
        #                         valor -= 26
        #                 else:  # Es una letra mayúscula
        #                     if valor > ord('Z'):
        #                         valor -= 26
        #                 car_cifrado = chr(valor)
        #                 print(car_cifrado)
        #                 linea_cifrada += car_cifrado
        #         else:
        #             linea_cifrada += caracter  # Añade caracteres no alfabéticos
        #     print(linea_cifrada)
        #     destino.write(linea_cifrada + '\n')  # Añade una nueva línea al final de cada línea cifrada
