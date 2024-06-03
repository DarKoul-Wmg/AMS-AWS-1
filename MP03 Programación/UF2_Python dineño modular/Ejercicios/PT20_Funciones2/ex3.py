def es_vocal(x):
    if x == "a" or x =="e" or x =="i" or x =="o" or x =="u":
        return True

    if x == "A" or x =="E" or x =="I" or x =="O" or x =="U":
        return True

    else:
        return False

print(es_vocal('9'))

# ESta funcion nos devuelve True si introducimos como x una vocal,
# ya sea mayuscula o minuscula. Si introducimos otra letra, caracter
# o numero, nos retorna un False