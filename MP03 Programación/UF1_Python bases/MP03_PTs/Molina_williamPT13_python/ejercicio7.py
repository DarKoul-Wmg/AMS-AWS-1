primera_medida = []
segunda_medida = []

print("medidas del primer año")

for i in range(10):
    medida = float(input(str(i+1)+") Altura del alumn@: "))
    primera_medida.append(medida)

print("medidas del segundo año")

for i in range(10):
    medida = float(input(str(i+1)+") Altura del alumn@: "))
    segunda_medida.append(medida)

if len(primera_medida) == 10:
    for i in range(10):
        diferencia = segunda_medida[i] - primera_medida[i]
        print("Diferencia de alturas: "+ str(diferencia))
