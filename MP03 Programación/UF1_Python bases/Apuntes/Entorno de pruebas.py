nombre_usuario = "jose"
puntos_usuario = 50
datos_rank = "antonio:100;jose:50;miguel:75;"

if len(datos_rank) == 0:
    datos_rank = nombre_usuario + ":" + str(puntos_usuario) + ";"
else:
    inicio = 0
    final = datos_rank.index(";")

    while inicio < len(datos_rank):
        usuario_puntaje = datos_rank[inicio:final]
        nombre, puntaje = usuario_puntaje.split(":")
        puntaje = int(puntaje)

        if puntos_usuario > puntaje:
            datos_rank = datos_rank[:inicio] + nombre_usuario + ":" + str(puntos_usuario) + ";" + datos_rank[inicio:]
            break

        inicio = final + 1
        if inicio < len(datos_rank):
            final = datos_rank.index(";", inicio)

print(datos_rank)
