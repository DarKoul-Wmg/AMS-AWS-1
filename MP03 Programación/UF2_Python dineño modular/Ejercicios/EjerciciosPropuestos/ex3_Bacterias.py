import time


def vida_bacterias(B1,CA):
    segundos = 1
    cabecera = "Seconds".ljust(10)+"Bacterias B1".rjust(15) + "Cells CA".rjust(15)
    print(cabecera)
    while B1 > 0 and CA >0:
        time.sleep(1)

        if CA >= 3*B1:
            CA = CA - 3*B1
            B1 = 2*B1

        else:
            bacterias_B1_comen_CA = CA//3
            celulas_CA_restantes = CA %3 #Residuo para ver las que quedan cuando no son multiples de 3

            B1 = 2*bacterias_B1_comen_CA
            CA = celulas_CA_restantes

        if segundos % 3 == 0:
            B1_muertas_por_CA = CA//10
            B1 = B1 - B1_muertas_por_CA
            if B1 < 0:
                B1 = 0

        if segundos % 4 == 0:
            CA = CA*4

        print(str(segundos).ljust(10) + str(B1).rjust(15) + str(CA).rjust(15))

        segundos += 1

vida_bacterias(15,1000)

#SOLO SI CA >= 3*B1
# CA - 3*B1
#SI CA < 3*B1Ç

#CA = CA%3 (SON LAS QUE QUEDAN DESPUES DE SER COMIDAS)
#CA // 3

#CALCULO DE B1: B1 = (CA//3)*2