import math

# Crear un diccionario para almacenar les coordenades dels punts
diccionari_coordenades = {}

# Llegir les coordenades del primer punt
x1 = float(input("Introdueix la coordenada x del primer punt: "))
y1 = float(input("Introdueix la coordenada y del primer punt: "))
diccionari_coordenades['punt1'] = (x1, y1)

# Llegir les coordenades del segon punt
x2 = float(input("Introdueix la coordenada x del segon punt: "))
y2 = float(input("Introdueix la coordenada y del segon punt: "))
diccionari_coordenades['punt2'] = (x2, y2)

# Calcular la distància en línia recta entre els dos punts
distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Mostrar la distància calculada
print(f"La distància entre els dos punts és: {distancia}")
