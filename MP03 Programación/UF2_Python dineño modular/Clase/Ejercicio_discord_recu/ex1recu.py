#dada una frase y una letra, devolver la frase desde la letra al final
def encontrarLetra(n,cadena):
     if cadena[0] == n:
        return cadena[0:]

     return encontrarLetra(n,cadena[1:])

print(encontrarLetra("d","abcde"))

#CLASE (construir cadena para comprobar)

# def letra_to_final(cadena,letra):
#     resultado = ""
#     if len(cadena) == 0:
#         return resultado
#
#     elif cadena[-1] == letra:
#         resultado = letra
#         return resultado
#
#     else:
#         resultado = letra_to_final(cadena[0:-1],letra + cadena[-1])
#         return resultado
#
# cadena = "abcdefgh"
# letra = "d"
# print(letra_to_final(cadena,letra))

