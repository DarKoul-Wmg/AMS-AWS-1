alumnos ={
    "11111111H":{"nombre":"Pedro","nota":7.5},
    "22222222A":{"nombre":"Aroa","nota":6.5},
    "33333333B":{"nombre":"Rafael","nota":1.5}
}

f = open("diccionario_clase_jordi.txt","w")

for dni in alumnos:
    datos = ""
    datos += dni
    for key in alumnos[dni]:
        datos += "*"+str(alumnos[dni][key])
    datos +="\n"

    f.write(datos)
f.close()

new_dict ={}
f = open("diccionario_clase_jordi.txt", "r")

for linea in f:
    linea = linea.replace("\n","")
    dni = linea.split("*")[0]
    new_dict[dni] = {"nombre":linea.split("*")[1], "nota":float(linea.split("*")[2])}

print(new_dict)
f.close()
