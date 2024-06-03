llista_tuples = [('Hola', 'don Pepito'), ('Hola', 'don Jose'), ('Bon', 'dia')]


diccionari_resultat = {}

for tupla in llista_tuples:
    primera_part, segona_part = tupla


    if primera_part in diccionari_resultat:
        diccionari_resultat[primera_part].append(segona_part)
    else:
        diccionari_resultat[primera_part] = [segona_part]

print(diccionari_resultat)
