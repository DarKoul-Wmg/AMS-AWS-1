"""5. Creeu un programa per gestionar les qualificacions dels alumnes, es demana:
a) Dissenyar un procediment que rebi una llista d’alumnes i altra de notes i mostri per pantalla el nom de tots els
   estudiants que aprovaren l’examen.
b) Dissenyar una funció que rebi la llista de notes i retorni el número de aprovats.
c) Dissenyar un procediment que rebi les dos llistes i mostri per pantalla el nom de tots els estudiants que van obtenir
   la màxima nota.
d) Dissenyar un procediment que rebi les dos llistes i mostri per pantalla el nom de tots els estudiants que tenen una
   qualificació igual o superior a la qualificació mitja.
e) Dissenyar una funció que rebi les dos llistes i un nom (una cadena); si el nom està a la llista d’estudiants,
   retornarà la seva nota, si no, retornarà None."""


# a) Procedimiento para mostrar los estudiantes que aprobaron el examen.
def mostrar_aprobados(alumnos, notas):
    print("Estudiantes que aprobaron el examen:")
    for i in range(len(alumnos)):
        if notas[i] >= 5:
            print(alumnos[i])


# b) Función para contar el número de aprobados.
def contar_aprobados(notas):
    contador = 0
    for nota in notas:
        if nota >= 5:
            contador += 1
    return contador


# c) Procedimiento para mostrar los estudiantes que obtuvieron la máxima nota.
def mostrar_maxima_nota(alumnos, notas):
    maxima_nota = max(notas)
    print("Estudiantes que obtuvieron la máxima nota:")
    for i in range(len(alumnos)):
        if notas[i] == maxima_nota:
            print(alumnos[i])


# d) Procedimiento para mostrar los estudiantes con una calificación igual o superior a la media.
def mostrar_calificacion_superior_media(alumnos, notas):
    media = sum(notas) / len(notas)
    print("Estudiantes con calificación igual o superior a la media:")
    for i in range(len(alumnos)):
        if notas[i] >= media:
            print(alumnos[i])


# e) Función para obtener la nota de un estudiante dado su nombre.
def obtener_nota_por_nombre(alumnos, notas, nombre):
    if nombre in alumnos:
        indice = alumnos.index(nombre)
        return notas[indice]
    else:
        return None


alumnos = ["Juan", "María", "Pedro", "Ana"]
notas = [7, 5, 8, 6]

mostrar_aprobados(alumnos, notas)
print("\n")
print("Número de aprobados:", contar_aprobados(notas))
print("\n")
mostrar_maxima_nota(alumnos, notas)
print("\n")
mostrar_calificacion_superior_media(alumnos, notas)
print("\n")

nombre = input("Ingrese el nombre del estudiante.\n> ")
nota = obtener_nota_por_nombre(alumnos, notas, nombre)
if nota is not None:
    print(f"La nota de {nombre} es: {nota}")
else:
    print(f"{nombre} no está en la lista de estudiantes.")
