def suma_vector(vector):
    if not vector:
        return 0
    else:
        return vector[0] + suma_vector(vector[1:])


# Vector de ejemplo.
vector = [1, 2, 3, 4, 5]

# Calculando la suma de los elementos del vector.
resultado = suma_vector(vector)

# Imprimiendo el resultado de la suma.
print("La suma de los elementos del vector es:", resultado)
