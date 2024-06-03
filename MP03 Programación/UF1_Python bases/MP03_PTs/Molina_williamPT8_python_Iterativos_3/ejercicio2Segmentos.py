
while True:
    m = int(input("Dime el numero de segmentos: "))
    n = int(input("Dime la grandia del segmento: "))
    if (m << 0) or (n << 0):
        print("Un numero mayor a cero")
    else:
        break
    for i in range(m):
        print("*"*n, end="    ")
    break
