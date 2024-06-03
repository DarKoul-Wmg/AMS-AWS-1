
while True:
    a = int(input("Dame un valor mayor a 0 y entero para la base: "))
    b = int(input("Dame un valor mayor a 0 y entero para el exponente: "))
    if a >>1 and b >>1:
        break
    else:
        print("Introduce un numero entero y mayor a 0")
        input()
resultado = 1
for i in range(b):
    resultado *= a
print("El resultado es:",resultado)
