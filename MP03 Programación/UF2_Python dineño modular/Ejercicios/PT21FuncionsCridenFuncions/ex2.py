

def canvi_diners(euros):
    lista_cambio = []

    cont500 = euros // 500
    euros = euros - (500* cont500)
    lista_cambio.append((cont500,"Billetes 500")) #Crear una lista de tuplas, donde relacionar el num de cambio y su tipo


    cont200 = euros // 200
    euros = euros - (200* cont200)
    lista_cambio.append((cont200,"Billetes 200"))

    cont100 = euros // 100
    euros = euros - (100* cont100)
    lista_cambio.append((cont100,"Billetes 100"))

    cont50 = euros // 50
    euros = euros - (50* cont50)
    lista_cambio.append((cont50,"Billetes 50"))

    cont20 = euros // 20
    euros = euros - (20* cont20)
    lista_cambio.append((cont20,"Billetes de 20"))

    cont10 = euros // 10
    euros = euros - (10* cont10)
    lista_cambio.append((cont10,"Billetes de 10"))

    cont5 = euros // 5
    euros = euros - (5* cont5)
    lista_cambio.append((cont5,"Billetes de 5"))

    cont2 = euros // 2
    euros = euros - (2* cont2)
    lista_cambio.append((cont2,"Monedas de 2"))

    cont1 = euros // 1
    euros = euros - (1* cont1)
    lista_cambio.append((cont1,"Monedas de 1"))

    if euros == 0:
        for element in lista_cambio:
            if not element[0] == 0:
                print(str(element[0])+" "+element[1])

canvi_diners(933)




# Per fer el desglossament es comença per calcular la divisió entera
# entre la quantitat i 500 (el valor de la major moneda): 434 entre 500 da 0,
# doncs no hi ha bitllets de 500 € en el desglossament; a continuació, es
# divideix la quantitat 434 entre 200, el quocient és 2 i el residu 34, així que
# en el desglossament hi ha 2 bitllets de 200 €; dividim a continuació 34 entre
# 100 i com dona 0 no hi ha cap bitllet de 100 € en el desglossament; com el
# residu de la última divisió és 34, passem a dividir 34 entre 20 i veiem que el
# desglossament inclou un bitllet de 20 € i encara ens falten 14 € per
# desglossar. . . )
