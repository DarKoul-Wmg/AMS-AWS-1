def invertir_num(num):
    resultado = ""
    num = str(num)
    if len(num) == 1:
        resultado += num[0]
        return resultado
    else:
        resultado += num[-1]
        num = num[:-1]
        num = int(num)
        return resultado + invertir_num(num)


num = 1234
print(invertir_num(num))
