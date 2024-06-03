while True:
    valido = False
    if valido == False:
        data = int(input("Introduce tu numero de la suerte, este numero es tu fecha de nacimiento(ddmmaaaa): "))
        # print(data)
        if len(str(data)) == 8 or len(str(data)) == 7:
         suma_num = 0
         valido = True
         numero = 0


         for i in str(data):
             suma_num += int(i)
         # print(suma_num)
         #Sacamos los 2 digitos
         division = suma_num // 10
         numero = suma_num %10
         numSort = division + numero
         #Suma de los 2 digitos
         division = numSort // 10
         numero = numSort %10
         numSort = division + numero
         print("El numero de la suerte es:", str(numSort))
         break
        else:
         valido = False
         print("Error...")







