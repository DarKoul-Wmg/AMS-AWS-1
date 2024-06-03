def str_to_int(s):
    if len(s) == 0:
        return 0
    else:
        return int(s[0]) * 10 ** (len(s) - 1) + str_to_int(s[1:])


def int_to_str(n):
    if n < 10:
        return str(n)
    else:
        return int_to_str(n // 10) + str(n % 10)


cadena = "12345"
numero = 54321
numero_convertido = str_to_int(cadena)
print("Cadena convertida a entero:", numero_convertido)
print("Tipo de dato de la conversión:", type(numero_convertido))
cadena_convertida = int_to_str(numero)
print("Entero convertido a cadena:", cadena_convertida)
print("Tipo de dato de la conversión:", type(cadena_convertida))
