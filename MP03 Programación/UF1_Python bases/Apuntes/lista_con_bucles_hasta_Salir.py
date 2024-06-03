print('Vamos a hacer la lista de la compra ')
cabezera = 'Lista de la  compra'.center(40,'*') + '\n' + 'Aritculos'.ljust(20) + 'Cantidad'.rjust(10)+ 'Precio'.rjust(10)+'\n' +'*'*40 + '\n'
datos=''
salir = ''
print(salir!='S')
while salir!='S':
    print(cabezera)

    Articulo = input('Articulo > ')
    Cantidad = input('Cantidad > ')
    Precio = input('Precio > ')

    datos = datos + Articulo.ljust(20) + Cantidad.rjust(10)+ Precio.rjust(10)+'\n'
    print(cabezera+datos)    
    print()
    salir = input('Quieres salir del programa ?? S\ N  \n> ')
    