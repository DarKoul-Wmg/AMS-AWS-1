datos = [("Pérez", "Juan", "M"), ("Molina", "Willy", "K")]


for elemento in datos:
    apellido, nombre, inicial_segundo_nombre = elemento
    cadena_formateada = f"{nombre} {inicial_segundo_nombre}. {apellido}"
    print(cadena_formateada)

