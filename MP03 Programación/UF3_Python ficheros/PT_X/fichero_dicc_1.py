import os

def exercici1(nom_fichero):
    fichero = open(nom_fichero,"r")
    customers = {}
    dni = ""
    nombre = ""
    apellido = ""

    cabecera = "Customers".center(73,"*")+"\n" +"Nif".ljust(15) + "Name".ljust(20) +"Surname".ljust(23) +\
               "Total Shoppings".rjust(15) +"\n" + "*"* 73
    datos = ""

    for linea in fichero:
        linea = linea.replace(" ","")
        linea = linea.replace("\n","")
        valores = linea.split(",") #separamos los diferentes valores
        print("------------------")
        for valor in valores:

            valor = valor.split(":")
            print(valor)
            if valor[0].lower() == "nif":
                dni = valor[1]
            if valor[0].lower() == "name":
                nombre = valor[1]
            if valor[0].lower() == "surname":
                apellido = valor[1]
            if valor[0].lower() == "shoppings":
                total_compras = 0
                compras = valor[1].split("-") # separamos y calculamos el total
                if len(compras) <=1:
                    total_compras = int(valor[1])
                else:
                    for compra in compras:
                        total_compras += int(compra)
                        #print(total_compras)
        customers[dni] = {"name": nombre, "surname":apellido, "shoppings": compras, "totalshoppings": total_compras}
    #print(clientes)

    lista = list(customers.keys())

    # ordenar en funcion de compras
    print(lista)
    for i in range(len(lista)-1):
        for j in range(len(lista)-i-1):
            if customers[lista[j]]["totalshoppings"] < customers[lista[j+1]]["totalshoppings"]:
                lista[j], lista[j+1] = lista[j+1], lista[j]

    #print(lista)
    for dni in lista:
        datos += "\n"+dni.ljust(15) + customers[dni]["name"].ljust(20) + customers[dni]["surname"].ljust(23) \
                 + str(customers[dni]["totalshoppings"]).rjust(15)
    print(cabecera)
    print(datos)

    fichero.close()

nom_fichero = "clients.txt"
if os.path.exists(nom_fichero):
    print("El fichero existe...")
    exercici1(nom_fichero)
else:
    print("El archivo no existe")
