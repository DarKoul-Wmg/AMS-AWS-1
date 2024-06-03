# 1.1) Función para aplicar un descuento a un precio
"""Definiu i programeu una funció que, donats un preu i un percentatge de descompte, ens torni el preu amb
el descompte aplicat. La funció té dos paràmetres: preu i percentatge. Retorna el preu amb el descompte
aplicat."""


# No recursiva:
def aplicar_descuento(precio, porcentaje_descuento):
    return precio - (precio * porcentaje_descuento / 100)


# Recursiva:
"""
def aplicar_descuento(precio, porcentaje_descuento):
    return precio - (precio * porcentaje_descuento / 100)
"""

precio_original = 100
descuento = 20
precio_con_descuento = aplicar_descuento(precio_original, descuento)
print("Precio con descuento:", precio_con_descuento)