print("REPETICIONES")
num_ent = int(input("Escribe un numero entero: "))
totalnums = int(input("Cantidad de numeros a introducir: "))

cont_igual = 0
cont_diff = 0
for num in range(totalnums):
    numero =  int(input("Escribe un numero entero: "))
    if numero == num_ent:
        cont_igual += 1
    else:
        cont_diff += 1

if cont_igual < cont_diff:
    print(f"Has escrito menos veces el número {num_ent} que el resto de numeros.")
elif cont_igual > cont_diff:
    print(f"Has escrito más veces el número {num_ent} que el resto de numeros.")
else:
    print(f"Has escrito las mismas veces el número {num_ent} que el resto de numeros.")





