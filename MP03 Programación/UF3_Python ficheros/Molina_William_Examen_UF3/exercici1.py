import os.path


def exercici1(nom_fitxer):
    if not os.path.exists(nom_fitxer):
        raise ValueError("L'arxiu no existeix")

    fichero = open(nom_fitxer,"r")
    dadesClients = {}
    dni = ""
    nombre = ""
    apellido1 = ""
    apellido2 = ""
    tfn = ""
    edad = 0
    id = ""

    cabecera = "*"*128+"\n" +"Name".ljust(20) + "Surname1".ljust(20) +"Surname2".ljust(20) +\
               "Dni".ljust(20) + "Tfn".ljust(20)+ "Age".ljust(20)+"\n" + "*"* 128

    datos = ""
    for linea in fichero:
        #print(linea)
        linea = linea.replace(" ","")
        linea = linea.replace("\n","")
        valores = linea.split(";") #separamos los diferentes valores
        #print(valores)
        for valor in valores:
            #print(valor)
            valor = valor.split(":")
            if valor[0].lower() == "dni":
                dni = valor[1]
            if valor[0].lower() == "name":
                nombre = valor[1]
            if valor[0].lower() == "id":
                id = valor[1]
            if valor[0].lower() == "tfn":
                tfn = valor[1]
            if valor[0].lower() == "age":
                edad = int(valor[1])
            if valor[0].lower() == "surnames":
                apellidos = valor[1].split("-") #Iteramos para sacar los dos apellidos
                #print(apellidos)
                apellido1 = apellidos[0]
                #print(apellido1)
                apellido2 = apellidos[1]
                #print(apellido2)

        dadesClients[id] = {'name':nombre,'surname1':apellido1,'surname2':apellido2,'dni':dni,'tfn':tfn,'age':edad}
    #print(dadesClients)

    listar_edad = list(dadesClients.keys()) #sacamos ids para filtrar las edades
    #print(listar_edad)
    for i in range(len(listar_edad)-1):
        if dadesClients[listar_edad[i]]["age"] <18:
            listar_edad.remove(listar_edad[i]) #eliminamos el cliente menor de 18 años
    #print(listar_edad)

    for id in listar_edad:
        datos += "\n"+dadesClients[id]['name'].ljust(20) + dadesClients[id]['surname1'].ljust(20) + \
                 dadesClients[id]['surname2'].ljust(20) + dadesClients[id]['dni'].ljust(20) + \
                 dadesClients[id]['tfn'].ljust(20)+ str(dadesClients[id]['age']).ljust(20)

    print(cabecera)
    print(datos)
    fichero.close()



nom_fitxer = "clients.txt"
try:
    exercici1(nom_fitxer)
except ValueError as e:
    print(e)
