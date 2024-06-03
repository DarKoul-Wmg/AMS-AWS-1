def exercici2(*parametres):
    try:
        string = ""
        cont = 0
        for i in parametres:
            cont +=1
            if len(parametres) < 2:
                raise TypeError("Tiene que haber como minimo 2 paarametros")
            if not isinstance(i, str):
                raise TypeError("Error, el parametro '{}' tienen que ser un string".format(i))

            if cont == len(parametres):
                string += i
            else:
                string += i + "-"

        return string
    except TypeError as error:
        print(error)

print(exercici2("A"))
print(exercici2("A",1))
print(exercici2("A","B","c"))
