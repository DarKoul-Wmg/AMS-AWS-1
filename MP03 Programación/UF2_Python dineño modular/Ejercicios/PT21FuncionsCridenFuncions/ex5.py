cabecera1 = "ALUMNOS APROBADOS".center(30,"*")+"\n\n"
cabecera2 = "ALUMNOS MAX NOTA".center(30,"*")+"\n\n"
cabecera3 = "ALUMNOS SOBRE MEDIA".center(30,"*")+"\n\n"
cabecera4= "BUSQUEDA ALUMNOS".center(30,"*")+"\n\n"

def alumnes_aprovats(lista_alumn,lista_notas): #a
    datos = ""
    for i in range(len(lista_notas)):
        if lista_notas[i] >= 5:
            datos += lista_alumn[i]+"\n"

    print(cabecera1 + datos)


def total_aprovats(lista_notas): #b
    aprobados = 0
    for nota in lista_notas:
        if nota >= 5:
            aprobados +=1
    return aprobados


def alumnes_maxNota(lista_alumn, lista_notas): #c
    datos = ""
    nota_max = 10
    for i in range(len(lista_notas)):
        if lista_notas[i] == nota_max:
            datos += lista_alumn[i] + "\n"

    print(cabecera2 + datos)


def alumnes_Sobre_mitja(lista_alumn,lista_notas): #d
    datos = ""
    nota_media = 0
    for nota in lista_notas:
        nota_media += nota
    nota_media = nota_media / len(lista_notas)
    #print(nota_media)

    for i in range(len(lista_notas)):
        if lista_notas[i] >= nota_media:
            datos += lista_alumn[i] + "\n"

    print(cabecera3 + datos)

def buscar_alumne(lista_alumn,lista_notas,nom): #e
    resultado= ""
    for i in range(len(lista_alumn)):
        if nom.lower() in lista_alumn[i].lower():
            resultado += lista_alumn[i].ljust(18) + str(lista_notas[i]).rjust(25) + "\n"


    if resultado:
        return resultado

    else:
        return None


lista_alumn = ["Manuel Garcia", "Maria Lopez", "Antonio Gutierrez", "Sonia Galan", "Paco Mermelo"]
lista_notas = [7.4,4.5,8,10,6.9]

#a
alumnes_aprovats(lista_alumn,lista_notas)

#b
print("El recuento de alumnos aprobados es: "+ str(total_aprovats(lista_notas)) + "\n")

#c
alumnes_maxNota(lista_alumn,lista_notas)

#d
alumnes_Sobre_mitja(lista_alumn, lista_notas)

#e
nom = input("Nombre a buscar")
resultado = buscar_alumne(lista_alumn,lista_notas,nom)
print(resultado)

