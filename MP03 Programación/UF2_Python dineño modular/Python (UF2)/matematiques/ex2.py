# a) Importeu el mòdul del exercici1 en el següent codi, de manera que les instruccions
# següents s'executin sense produir errors:
import operacions_basiques

a, b = 13, 3
print('operands =', a, b)
print('sumar =', operacions_basiques.sumar(a, b))
print('restar =', operacions_basiques.restar(a, b))
print('multiplicar =', operacions_basiques.multiplicar(a, b))
print('dividir =', operacions_basiques.dividir(a, b))

# b) Com hauries d'importar el mòdul perquè no hi hagués errors en executar?
import operacions_basiques as ob

a, b = 13, 3
print('operands =', a, b)
print('sumar =', ob.sumar(a, b))
print('restar =', ob.restar(a, b))
print('multiplicar =', ob.multiplicar(a, b))
print('dividir =', ob.dividir(a, b))

# c) I com faries que funcionés el següent codi?
from operacions_basiques import sumar, restar, multiplicar, dividir

"""DA ERROR POR ESTO. Hay un cero."""
a, b = 13, 0
print('operands =', a, b)
print('sumar =', sumar(a, b))
print('restar =', restar(a, b))
print('multiplicar =', multiplicar(a, b))
print('dividir =', dividir(a, b))
