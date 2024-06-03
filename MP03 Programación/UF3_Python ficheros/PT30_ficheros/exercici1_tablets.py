
def tabletsBarats(nomf1,nomf2,p):
    nomf2 = open("resultats", "w+")

    tablets = nomf1.readlines()
    filtro = ""

    for element in tablets:
        element = element.replace("\n","").replace(" ","")
        element = element.split(";")
        #print(element)
        nom = element[0]
        model = element[1]
        vel = int(element[3])
        preu = float(element[-1])
        #print("nom:{} model: {} vel: {} preu: {}".format(nom,model,vel,preu))

        nom_model = nom[:3] + "-" + model
        #print(nom_model)
        nivell_vel = ""
        if vel < 500:
            nivell_vel = "Baixa"
        elif vel >= 500 and vel <= 900:
            nivell_vel = "Mitjana"
        elif vel > 900:
            nivell_vel = "Alta"

        if preu < p:
            filtro += "{} {} \n".format(nom_model,nivell_vel)

    nomf2.write(filtro)
    nomf2.close()

nomf1 = open("models","r")
nomf2 = ""

p = 100
tabletsBarats(nomf1,nomf2,p)
nomf1.close
