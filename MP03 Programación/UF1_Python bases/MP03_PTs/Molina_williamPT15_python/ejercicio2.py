dias_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
anno_usuario = int(input("Ingresa el año: "))
mes_usuario = int(input("Ingresa el mes: "))
dia_usuario = int(input("Ingresa el día: "))
#año bisiesto
if anno_usuario % 4 == 0 and (anno_usuario % 100 != 0 or anno_usuario % 400 == 0):
    dias_mes[1] = 29  # Febrero tiene 29 días en años bisiestos

# Verificar si el día es válido
if 1 <= dia_usuario <= dias_mes[mes_usuario - 1]:
    # Verificar ultimo día del mes
    if dia_usuario == dias_mes[mes_usuario - 1]:
        # Si es el último día, pasar al primer día del próximo mes
        mes_siguiente = mes_usuario % 12 + 1
        anno_siguiente = anno_usuario if mes_siguiente > mes_usuario else anno_usuario + 1
        dia_siguiente = 1
    else:
        # Si no es el ultimo día, sumar 1 al día
        mes_siguiente = mes_usuario
        anno_siguiente = anno_usuario
        dia_siguiente = dia_usuario + 1


    print(f"El día siguiente de ({anno_usuario}, {mes_usuario}, {dia_usuario}) es ({anno_siguiente}, {mes_siguiente}, {dia_siguiente})")
else:
    print("Fecha no válida")


print("====================================================")

anno1 = int(input("Ingresa el año de la primera fecha: "))
mes1 = int(input("Ingresa el mes de la primera fecha: "))
dia1 = int(input("Ingresa el día de la primera fecha: "))

anno2 = int(input("Ingresa el año de la segunda fecha: "))
mes2 = int(input("Ingresa el mes de la segunda fecha: "))
dia2 = int(input("Ingresa el día de la segunda fecha: "))

dias_totales1 = 0
dias_totales2 = 0

for i in range(1, mes1):
    dias_totales1 += dias_mes[i - 1]

dias_totales1 += dia1

for i in range(1, mes2):
    dias_totales2 += dias_mes[i - 1]

dias_totales2 += dia2


diferencia_dias = dias_totales2 - dias_totales1

print(f"La diferencia en días entre las fechas es: {diferencia_dias} días")
