lista = ["Antonio", "Godofredo", "Marc", "Jose"]

p0 = int(input("Posicion origen"))
c = int(input("cantidad"))

posicion_final = p0+c
if 0 <= p0 < len(lista):
    for i in range(p0, posicion_final):
        if i < len(lista):
            print(f"Estimat {lista[i]} M’alegro de veure’t")

else:
    print("posició no vàlida")
