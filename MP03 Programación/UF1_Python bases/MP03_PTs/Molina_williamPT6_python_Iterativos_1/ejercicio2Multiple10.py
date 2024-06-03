#a
print("Introdueix un numero multiple de 10: ")
num = int(input())

while True:
 if num % 10 ==0:
    break
#b


 else:
  print("El numero introduït no es multiple de 10 ")
  num = int(input("Introdueix un altre que sigui multiple: "))

exponente = 0
temp = num
while temp % 10 == 0:
    temp //= 10
    exponente += 1
print("ENTRADA       MISSATGE DE SORTIDA")
print(str(num).ljust(6) + "    " + str(temp).rjust(5) + " per 10 elevat a " + str(exponente))

