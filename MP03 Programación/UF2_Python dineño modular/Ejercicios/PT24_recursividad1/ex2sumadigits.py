def suma_digits_num(num):
    resultado = 0
    num = str(num)
    if len(num) == 0:
        return resultado

    else:
        resultado += int(num[0])
        return resultado + suma_digits_num(num[1:])



num = 1234
print(str(suma_digits_num(num)))
