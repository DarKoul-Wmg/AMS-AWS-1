def divbase(num,b):
    resultado = ""
    if b > num:
        resultado += str(num)
        return resultado
    else:
        resultado += str(int(num % b))
        num = int(num / b)
        return  divbase(num,b) + resultado


# def changeBase(num,base):
#     resultado = ""
#     while num >= base:
#         resultado = str(num%base) + resultado
#         num = int(num/base)
#     resultado = str(num) +resultado
#     return resultado

num = 768
base = 8

print(changeBase(num,base))
print(divbase(num,base))


# def divbase(num, b):
#     if b > num:
#         return str(num)
#     else:
#         resto = str(int(num % b))
#         num = int(num / b)
#         return divbase(num, b) + resto
#
# # Ejemplo de uso
# num = 10
# base = 2
# print(divbase(num, base))
