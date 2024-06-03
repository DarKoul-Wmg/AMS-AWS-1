#METODO 1:
[27,34,12,1,7] ordenar de forma creciente

pasada (ver todos numeros de lista) = comparamos el primero con el segundo, si numero
mas pequeño que segundo se intercambia. Si cojemos como referencia el primero queda:

[12,34,27,12,7], al final de la pasada 0 queda [1,34,27,12,7]

La segunda pasada empieza en el segundo elemento(34), despues de intercambiar los
numeros, el intercambio total queda[1, 7, 34, 27, 12]:

La pasada 2 da como resultado [1,7,12,34,27]
La pasada 3 deja ya la cadena ordenada [1,7,12,27,34]

#PARA AHVER LOS INTERCAMBIOS: lista[5] <-> lista[10]

aux = lista[5]
lista[5] = lista[10]
lista[10]= aux

#METODO PYTHON: lista[5], lista[10]=lista[10],lista[5]



#METODO 2 BURBUJA
pasadas = (len(lista)) -1

#si contamos desde 0:
comparacion = (len(lista))  -1 - pasada

pasada 0, comparamos primero con el segundo, si se quedan igual,
el segundo lo comparamos con el siguiente:
Comp0 : [27,34,12,1,7]
Comp1 : [27,12,34,1,7]
Comp2 : [27,12,1,34,7]
Comp3 : [27,12,1,7,34]

pasada 1
Comp0 : [12,27,1,7,34]
Comp1 : [12,1,27,7,34]
Comp2 : [12,1,7,27,34]

pasada 2
Comp0: [1,12,7,27,34]
Comp1 : [1,7,12,27,34]

pasada 3 #Ultima pasada de comp para verificar que 1 es mas pequeño que 7.
Comp0: [1,7,12,27,34]

#EN RESUMEN Pasadas = longitud(lista) - 1
for pasada in range (4):
    for i in range (long(lista)-1-pasada):