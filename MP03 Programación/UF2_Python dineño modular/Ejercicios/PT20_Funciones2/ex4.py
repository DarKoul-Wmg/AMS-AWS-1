def inversa(cadena):
    invertida = ""
    cont = len(cadena)
    indice = -1
    while cont >= 1:
        invertida += cadena[indice]
        indice = indice + (-1)
        cont -= 1

    return invertida

print(inversa('asca'))

# ESta funcion toma una cadena con el indice -1 para poder
# invertirla y sacar la cadena en order inverso. Se usa un contador
# con la longitud de la cadena para que, una vez se pasa uno de los caracteres
# de la cadena, este disminuya. Una vez que el contador llega a 0, la funcion detecta
# que ya ha invertido toda la cadena.