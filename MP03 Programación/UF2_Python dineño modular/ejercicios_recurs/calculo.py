def media(*paramentres):
    try:
        suma = 0
        for i in paramentres:
            if len(paramentres) < 2:
                raise TypeError("Tiene que haber mas de un parametro")
            if not isinstance(i, int):
                raise TypeError("Error, el parametro '{}' tienen que ser INT".format(i))

            suma += i
        media = float(suma / len(paramentres))
        return media

    except TypeError as error:
        print(error)
        quit()



print(media("a",1,2))
print(media(1,2))
print(media(1,2,3))
print(media(1,2,3,4,5))
