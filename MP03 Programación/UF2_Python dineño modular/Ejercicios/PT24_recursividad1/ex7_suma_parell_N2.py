def suma_parells(num):
    resultado = 0
    if num == 2:
        resultado += 2
        return resultado
    else:
        if num %2 == 0:
            resultado += num
            return resultado + suma_parells(num-1)
        else:
            return resultado + suma_parells(num-1)

num = 12
print(suma_parells(num))
