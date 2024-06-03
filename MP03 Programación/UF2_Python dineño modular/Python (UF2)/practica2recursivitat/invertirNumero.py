def invertir_numero(numero):
    if numero < 10:
        return numero
    else:
        ultimo_digito = numero % 10
        longitud = len(str(numero))
        return ultimo_digito * 10**(longitud - 1) + invertir_numero(numero // 10)


numero = 123456789
numero_invertido = invertir_numero(numero)
print("Número invertido:", numero_invertido)
