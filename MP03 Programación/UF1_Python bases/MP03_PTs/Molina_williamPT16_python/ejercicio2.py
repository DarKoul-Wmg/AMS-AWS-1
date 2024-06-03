# Crear un diccionario para almacenar les Fitxes dels llibres
diccionari_llibres = {}

# Llegir del teclat les dades per a omplir el diccionari

identificador = input("Introdueix l'identificador del llibre: ")
titol = input("Introdueix el títol del llibre: ")
autor = input("Introdueix l'autor del llibre: ")
editorial = input("Introdueix l'editorial del llibre: ")
any_edicio = input("Introdueix l'any d'edició del llibre: ")
num_pagines = input("Introdueix el número de pàgines del llibre: ")

fitxa_llibre = {
    'identificador': identificador,
    'titol': titol,
    'autor': autor,
    'editorial': editorial,
    'any_edicio': any_edicio,
    'num_pagines': num_pagines
}

diccionari_llibres[identificador] = fitxa_llibre



print("Resum de les Fitxes dels llibres:")
for identificador, fitxa_llibre in diccionari_llibres.items():
    print(f"Identificador: {fitxa_llibre['identificador']}, Títol: {fitxa_llibre['titol']}, Autor: {fitxa_llibre['autor']}, Editorial: {fitxa_llibre['editorial']}, Any d'edició: {fitxa_llibre['any_edicio']}, Número de pàgines: {fitxa_llibre['num_pagines']}")
