def esta_en_rango(numero, inicio, fin):
    if inicio <= numero <= fin:
        return True
    else:
        return False


numero = 5
inicio = 1
fin = 10
print("¿El número está en el rango?:", esta_en_rango(numero, inicio, fin))
