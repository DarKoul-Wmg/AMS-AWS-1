def descuento(precio,porcenaje_des):
   precioFin = precio - (precio*porcenaje_des)

   return precioFin

precio = int(input("Introduce el precio del producto "))
porcentaje_des = int(input("Introduce el descuento "))

porcentaje_des = porcentaje_des /100

print("El precio con el descuento aplicado es: "+ str(descuento(precio,porcentaje_des)))

