a = (2, 10, 1991)
b = (25, 12, 1990)
c = ('Donald', True, b)
x, y = ((27, 3), 9)
z, w = x
v = (x, a)

# # Expresiones
# >>> a < b
# # Resultado: True
# # Tipo: bool
#
# >>> y + w
# # Resultado: 12
# # Tipo: int
#
# >>> x + a
# # Resultado: (27, 3, 2, 10, 1991)
# # Tipo: tuple
#
# >>> len(v)
# # Resultado: 2
# # Tipo: int
#
# >>> v[1][1]
# # Resultado: 10
# # Tipo: int
#
# >>> c[0][0]
# # Resultado: 'D'
# # Tipo: str
#
# >>> z, y
# # Resultado: (27, 9)
# # Tipo: tuple
#
# >>> a + b[1:5]
# # Resultado: (2, 10, 1991, 12)
# # Tipo: tuple
#
# >>> (a + b)[1:5]
# # Resultado: (10, 1991, 25, 12)
# # Tipo: tuple
#
# >>> str(a[2]) + str(b[2])
# # Resultado: '19911990'
# # Tipo: str
#
# >>> str(a[2] + b[2])
# # Resultado: '3981'
# # Tipo: str
#
# >>> str((a + b)[2])
# # Resultado: '1991'
# # Tipo: str
#
# >>> str(a + b)[2]
# # Resultado: '1'
# # Tipo: str

r = a < b
print(r)

r = y+w
print(r)

r = x + a
print(r)

r = len(v)
print(r)
r = v[1][1]
print(r)
r = c[0][0]
print(r)
r = z, y
print(r)
r = a + b[1:5]
print(r)
r = (a + b)[1:5]
print(r)
r = str(a[2]) + str(b[2])
print(r)
r = str(a[2] + b[2])
print(r)
r = str((a + b)[2])
print(r)
r = str(a + b)[2]
print(r)

