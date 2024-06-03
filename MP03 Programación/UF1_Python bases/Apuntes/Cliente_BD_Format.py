print('Vamos a hacer la lista de clientes ')
Cabezera = '{}{}{}{}{}'.format('Nombre'.ljust(10),'Edad'.rjust(5),'  ','Dni'.ljust(10),'Telefono'.rjust(14))

print('*'*30+'\n' +Cabezera+'\n'+'*'*30 )

#1
INFO = ''
Nombre = input('Nombre > ')
Edad = input('Edad > ')
DNI = input('DNI > ')
Telefono = input('Telefono > ')

Linea='{}{}{}{}{}'.format(Nombre.ljust(10),Edad.rjust(5),'  ',DNI.ljust(10),Telefono.rjust(14))
INFO = INFO+Linea+'\n'
print(Cabezera+'\n'+INFO)

#2

Nombre = input('Nombre > ')
Edad = input('Edad > ')
DNI = input('DNI > ')
Telefono = input('Telefono > ')
Linea='{}{}{}{}{}'.format(Nombre.ljust(10),Edad.rjust(5),'  ',DNI.ljust(10),Telefono.rjust(14))
INFO = INFO+Linea+'\n'
print(Cabezera+'\n'+INFO)

#3

Nombre = input('Nombre > ')
Edad = input('Edad > ')
DNI = input('DNI > ')
Telefono = input('Telefono > ')
Linea='{}{}{}{}{}'.format(Nombre.ljust(10),Edad.rjust(5),'  ',DNI.ljust(10),Telefono.rjust(14))
INFO = INFO+Linea+'\n'
print(Cabezera+'\n'+INFO)