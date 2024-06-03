#diccionario: guardar datos en un fichero y recuperarlos

# USO SPLIT
# cadena = "1234;3434;dfdfdf ; erere"
# print(cadena.split(";"))


datos = open("diccionario_clase.txt", "w")

alumnos ={"11111111h": {"nombre":"Pedro","nota":7},
        "22222222A":{"nombre":"Antonio","nota":4},
          "33333333J":{"nombre":"Marko","nota":8}
          }


guardar = alumnos.items()

string = ""
for dni, alumno in guardar:
    #print("dni:" + str(dni))
    #print("alumno: "+str(alumno))

    string += dni
    string += ";"
    for valor in alumno.values():
        #print("valor: "+str(valor))
        if not isinstance(valor, str): #Si no es str cambia valor a str
            string += str(valor)

        else:
            string += valor
            string += ";"

    string += "\n" #salto de linea poe cada entrada
datos.write(string)
print(string)
datos.close()


datos_nuevos = open("diccionario_clase.txt","r")
nuevo_dicc = {}

entradas = datos_nuevos.readlines()
#print(entradas)

for alumno in entradas:
    alumno = alumno.split(";") #Te devuelve tres listas con los elementos separados

    for i in alumno:
        i.replace("\n", "") #quitar saltos de linea
    nuevo_dicc[alumno[0]] = {"nombre": alumno[1], "nota": int(alumno[2])}

print(alumnos)
print(nuevo_dicc)
datos_nuevos.close()

