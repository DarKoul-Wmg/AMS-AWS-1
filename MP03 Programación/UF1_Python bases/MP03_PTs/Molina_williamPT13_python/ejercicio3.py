lista = [["Antonia","dona"], ["Godofredo","home"], ["Marga","dona"], ["Jose", "home"]]

p0 = int(input("Posicion origen"))
c = int(input("cantidad"))

posicion_final = p0+c
if 0 <= p0 < len(lista):
    for i in range(p0, posicion_final):
        if i < len(lista):
            if lista[i][1] == "home":
                print(f"Estimat {lista[i][0]} M’alegro de veure’t")
            elif lista[i][1] == "dona":
                print(f"Estimada {lista[i][0]} M’alegro de veure’t")
else:
    print("posició no vàlida")
