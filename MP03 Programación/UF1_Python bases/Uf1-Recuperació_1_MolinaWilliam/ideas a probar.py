import random

# tablero = '''
# +------+------+------+------+------+------+------+------+
# |00    |01    |02    |03    |04    |05*   |06P   |07    |
# +------+------+------+------+------+------+------+------+
# |25*   |26    |27    |28    |29U   |30*   |31    |08    |
# +------+------+------+------+------+------+------+------+
# |24D   |43    |44    |45    |46*   |47    |32    |09*   |
# +------+------+------+------+------+------+------+------+
# |23    |42    |53     LaOca        |48    |33    |10D   |
# +------+------+------+------+------+------+------+------+
# |22    |41*   |52C   |51    |50    |49    |34*   |11    |
# +------+------+------+------+------+------+------+------+
# |21*   |40    |39    |38L   |37*   |36    |35    |12    |
# +------+------+------+------+------+------+------+------+
# |20    |19P   |18    |17H   |16*   |15    |14    |13    |
# +------+------+------+------+------+------+------+------+
# '''
# posicionV = 18
# posicionB = 3
# posicionD = 42
# posicionG = 17
# # Posiciones de los jugadores
# jugadorV = '-V'
# jugadorB = '-B'
# jugadorD = '-D'
# jugadorG = '-G'
#
# # Encontrar las coordenadas de las posiciones
# posicion_jV = tablero.index(f"{posicionV}")
# posicion_jB = tablero.index(f'{posicionB}')
# posicion_jD = tablero.index(f'{posicionD}')
# posicion_jG = tablero.index(f'{posicionG}')
#
# # Mostrar el tablero
# tablero_con_jugadores = (
#     tablero[:posicion_jV] + jugadorV + tablero[posicion_jV + len(jugadorV):posicion_jB] +
#     jugadorB + tablero[posicion_jB + len(jugadorB):posicion_jD] +
#     jugadorD + tablero[posicion_jD + len(jugadorD):posicion_jG] +
#     jugadorG + tablero[posicion_jG + len(jugadorG):]
# )
# print(tablero_con_jugadores)

tablero = '''
+------+------+------+------+------+------+------+------+
|00    |01    |02    |03    |04    |05*   |06P   |07    |
+------+------+------+------+------+------+------+------+
|25*   |26    |27    |28    |29U   |30*   |31    |08    |
+------+------+------+------+------+------+------+------+
|24D   |43    |44    |45    |46*   |47    |32    |09*   |
+------+------+------+------+------+------+------+------+
|23    |42    |53     LaOca        |48    |33    |10D   |
+------+------+------+------+------+------+------+------+
|22    |41*   |52C   |51    |50    |49    |34*   |11    |
+------+------+------+------+------+------+------+------+
|21*   |40    |39    |38L   |37*   |36    |35    |12    |
+------+------+------+------+------+------+------+------+
|20    |19P   |18    |17H   |16*   |15    |14    |13    |
+------+------+------+------+------+------+------+------+
'''

# Jugadores y sus posiciones
jugadorV = '-V'
jugadorB = '-B'
jugadorD = '-D'
jugadorG = '-G'

posicionV = 18
posicionB = 3
posicionD = 42
posicionG = 17

# Modificar el tablero con las posiciones de los jugadores
tablero_con_jugadores = tablero.replace(f"{posicionV}", f"{posicionV}{jugadorV}") \
    .replace(f"{posicionB}", f"{posicionB}{jugadorB}") \
    .replace(f"{posicionD}", f"{posicionD}{jugadorD}") \
    .replace(f"{posicionG}", f"{posicionG}{jugadorG}")

print(tablero_con_jugadores)





