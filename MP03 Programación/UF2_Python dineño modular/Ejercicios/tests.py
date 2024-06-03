


num = 1234
num = str(num)
print(type(num))

resultado = 0
resultado += int(num[0])

num = num[1:]
num = int(num)
print(type(num))

print(resultado)
print(num)
