fichero = open("pacients","r")
resultados = open("resultado", "w+")

datos = fichero.readlines()

cabecera = datos[0]
datos = datos[1:]
#cabecera = cabecera.split()
#cabecera = cabecera[0].ljust(10) + cabecera[1].rjust(5) + cabecera[2].rjust(15) +"\n"
#cabecera += "-"*len(cabecera)
#data = ""
resultado = ""
for entrada in datos:
    entrada = entrada.replace("\n", "")
    info = entrada.split(" ")
    #print(info)
    nom = info[0]
    edad = int(info[1])
    diab = info[2]
    #data += str(nom).ljust(10) + str(edad).rjust(5) + str(diab).rjust(15) + "\n"

    if edad > 20 and diab.lower() == "no":
        resultado += "{} {} {} \n".format(nom,edad,diab)

resultados.write(resultado)
#print(cabecera)
#print(data)
print("\nPacientes con más de 20 años y no son Diabeticos: ")
resultados.seek(0)#mover cursor para leer contenido
pacientes = resultados.read()
print(cabecera)
print(pacientes)
fichero.close()
resultados.close()
