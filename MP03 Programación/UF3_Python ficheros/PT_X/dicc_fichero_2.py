def exercici2(diccioanrio):
    fichero = open("clients.txt","a+")
    datos = ""
    for clave in diccioanrio:
        print(clave)

        if clave == "nif":
            dni = diccioanrio[clave]

        if clave == "name":
            nombre = diccioanrio[clave]

        if clave == "surname":
            apellido = diccioanrio[clave]

        if clave == "shoppings":
            cadena_compras =""
            compras = diccioanrio[clave]
            for compra in compras:
                cadena_compras += compra +"-"
            cadena_compras = cadena_compras[:-1]

    datos = "\nnif:"+dni+","+"name:"+nombre+","+"surname:"+apellido+",""shoppings:"+cadena_compras

    fichero.write(datos)
    fichero.close()


nuevo_cliente = {'nif':'99999999A','name':'Marta','shoppings': ['234','34','2344'],'surname':'Lara'}

exercici2(nuevo_cliente)

