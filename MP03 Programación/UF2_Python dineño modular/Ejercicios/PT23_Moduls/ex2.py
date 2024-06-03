#EX2

from matematiques import operacions_basiques
from matematiques import operacions_basiques as ob
from matematiques.operacions_basiques import *


#a

a, b = 13, 3
print ('operands =', a, b)
print ('sumar =', operacions_basiques.sumar (a, b))
print ('restar =', operacions_basiques.restar (a, b))
print ('multiplicar =', operacions_basiques.multiplicar (a, b))
print ('dividir =', operacions_basiques.dividir (a, b))
print("-------------------------------------------")

#b

a, b = 13, 3
print ('operands =', a, b)
print ('sumar =', ob.sumar (a, b))
print ('restar =', ob.restar (a, b))
print ('multiplicar =', ob.multiplicar (a, b))
print ('dividir =', ob.dividir (a, b))
print("-------------------------------------------")

#c

a, b = 13, 0
print ('operands =', a, b)
print ('sumar =', sumar (a, b))
print ('restar =', restar (a, b))
print ('multiplicar =', multiplicar (a, b))
print ('dividir =', dividir (a, b))
