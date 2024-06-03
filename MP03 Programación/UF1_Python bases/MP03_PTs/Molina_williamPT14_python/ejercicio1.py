llistaAlumnes = []
llistaNotes = []

llistaLiteras = ["Suspès", "Suspès", "Suspès", "Suspès", "Aprovat", "Bé", "Notable", "Notable", "Excel·lent", "Excel·lent"]

for i in range(8):
    nom = input("Nom alumne {}: ".format(i+1))
    nota = float(input("Nota alumne {}: ".format(i+1)))
    llistaAlumnes.append(nom)
    llistaNotes.append(nota)

for i in range(8):

    print(llistaAlumnes[i] +" nota: " + llistaLiteras[int(llistaNotes[i])])



llistaAlumnes = []
llistaNotes = []

llistaLiteras = ["Suspès", "Suspès", "Suspès", "Suspès", "Aprovat", "Bé", "Notable", "Notable", "Excel·lent", "Excel·lent"]

for i in range(8):
    nom = input("Nom alumne {}: ".format(i+1))
    nota = round(float(input("Nota alumne {}: ".format(i+1))))  # Redondear la nota a un entero
    llistaAlumnes.append(nom)
    llistaNotes.append(nota)

for i in range(8):
    print(llistaAlumnes[i] + " nota: " + llistaLiteras[int(llistaNotes[i])])


