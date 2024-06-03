def llegirPersona():
    fichero = open("13persones.txt","r")
    for linea in fichero.readlines():
        linea.replace("\n","")
        linea = linea.split("-")
        print("Persona: ")

        for i in linea:
            i = i.split(":")
            print(i[0] + ": "+str(i[1]))





def escriurePersonaDisc():
    datos = True
    while datos:
        persona = []
        print("Ingresa los datos de una persona\n")
        nom = input("Nom: ")
        cognoms = input("cognoms: ")
        nif = input("NIF: ")
        edat = input("edat: ")
        altura = input("alçada: ")
        persona.append("nom:" + nom)
        persona.append("cognoms:"+ cognoms)
        persona.append("NIF:" + nif)
        persona.append("edat:"+ edat)
        persona.append("alçada:"+str(float(altura)))

        entrada = ""
        for i in persona:
            if len(entrada) == 0:
                entrada += str(i)
            else:
                entrada += "-" + str(i)
        print(entrada)
        with open("13persones.txt","a+") as fichero:
            fichero.write(entrada+"\n")

        salir = input("Enter para seguir, s para salir")
        if salir.lower() == "s":
            datos = False

#escriurePersonaDisc()

llegirPersona()
