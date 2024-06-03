fichero = open("archivo3","r")

info = fichero.readlines()

for linea in info:
    linea = linea.replace("\n","").split(";")
    for i in linea:
        print(i)

fichero.close()
