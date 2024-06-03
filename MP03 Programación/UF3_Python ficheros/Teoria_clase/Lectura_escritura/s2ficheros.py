f = open("s2ficheros.txt","r")

dicc = {}
dni = ""
nombre =""
nota = 0
f.seek(0)
for linea in f:
    linea = linea.replace(" ","")
    linea = linea.replace("\n","")
    entradas = linea.split("*")
    print(entradas)
    for i in entradas:
        dato = i.split("-")
        print(dato)
        if dato[0].lower() == "dni":
            dni = dato[1]
        elif dato[0].lower() == "nombre":
            nombre = dato[1]
        elif dato[0] == "nota":
            nota = float(dato[1])

    dicc[dni] = {"nombre":nombre,"nota":nota}

print(dicc)

alumnos = dicc.items()
lista =[]

for dni in alumnos:
    lista.append(dni[0])

#print(lista)
for i in range(len(lista)-1):
    for j in range(len(lista)-i-1):
        if lista[j] > lista[j+1]:
            lista[j],lista[j+1] = lista[j+1],lista[j]

print("alumnos ordenados por dni: ")
for dni in lista:
    print(dni + "  " + dicc[dni]["nombre"])


print(alumnos)
f.close()


def nueva_entrada():
    nuevo = {"44444444C":{"nombre": "lala","nota": 7.45}}

    datos =""
    for dni in nuevo:

        datos += "dni-" + dni
        for key in nuevo[dni]:
            datos += "*"+str(key)
            datos += "-"+str(nuevo[dni][key])

    print(datos)
    f.write(datos)

def nueva_entrada2():
    dni = "55556555Q"
    nombre = "jose"
    nota = 7.6
    dicc[dni] = {"nombre":nombre, "nota":float(nota)}

    f.write("\ndni"+"-"+dni+"*nombre-"+nombre+"*nota-"+str(nota))

f = open("s2ficheros.txt","a+")
#nueva_entrada()
nueva_entrada2()
f.close()
