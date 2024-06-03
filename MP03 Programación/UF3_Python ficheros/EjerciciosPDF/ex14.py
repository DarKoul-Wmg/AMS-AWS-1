fichero = open("13persones.txt","r")

personas = fichero.readlines() #sacamos todas las entradas

for i in personas:
    i = i.replace("\n","")
    per = i.split("-")
    for j in per:
        dato = j.split(":")
        if dato[0].lower() == "nom":
            nom = dato[1]
        if dato[0].lower() == "cognoms":
            cognoms = dato[1]
        if dato[0].lower() == "nif":
            dni = dato[1]
        if dato[0].lower() == "altura":
            altura = float(dato[1])
        if dato[0].lower() == "edat":
            edat = int(dato[1])
    if edat >= 18:
        print("Alumno: {} {} \n NIF: {} \n Edat: {} \n Altura: {}\n".format(nom, cognoms, dni, str(edat), str(altura)))

