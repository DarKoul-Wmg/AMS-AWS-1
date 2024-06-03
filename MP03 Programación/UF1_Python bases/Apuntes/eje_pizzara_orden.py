print('*'*30)
print('Comida'.center(30))
print('*'*30)
print('Nombre'.ljust(14),'Percios'.rjust(15))
print('Entrecot'.ljust(14),'25.35'.rjust(15))
print('Callos'.ljust(14),'15.1'.rjust(15))
print('Patatas brabas'.ljust(14),'9.5'.rjust(15))
print('*'*30)

######################################################

'''Manera de jordi'''
print('')
print('Manera de jordi')#\ añade el siguiente caso
cabezera = '*'*30+'\n'+'Comida'.center(30)+ '\n'+ '*'*30 +\
            '\n'+'Nombre'.ljust(14) + 'Precio'.rjust(15)+'\n'
Cuerpo= 'Entrecot'.ljust(14) + '25.35'.rjust(15)+\
            '\n'+ 'Callos'.ljust(14) + '15.1'.rjust(15)+\
            '\n'+ 'Patatas brabas'.ljust(14) + '9.5'.rjust(15)+'\n'
print(cabezera,Cuerpo)