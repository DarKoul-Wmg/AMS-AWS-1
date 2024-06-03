def coincide_valor_indice(vector, indice):
    if len(vector) == 0:
        return False
    elif vector[0] == indice:
        return True
    else:
        return coincide_valor_indice(vector[1:], indice + 1)


vector = [5, 4, 3, 2, 1]
print("¿Coincide algún valor con su índice?:", coincide_valor_indice(vector, 0))
