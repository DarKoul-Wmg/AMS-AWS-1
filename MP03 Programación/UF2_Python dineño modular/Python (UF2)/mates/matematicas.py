# Calcula los primeros n términos de la secuencia de Fibonacci.
def fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence[:n]


# Realiza la división de dos números y devuelve el cociente y el residuo.
def realizar_division(dividendo, divisor):
    cociente = dividendo // divisor
    residuo = dividendo % divisor
    return cociente, residuo

# Realiza la resta de dos números.
def realizar_resta(a, b):
    return a - b

# Realiza la suma de dos números.
def realizar_suma(a, b):
    return a + b

# Calcula la suma consecutiva de los dígitos de un número.
def suma_consecutiva(numero):
    suma = 0
    for d in str(numero):
        suma += int(d)
    return suma

# Ejemplos de uso:
print("Cambio de base: ", cambiar_base("101", 2, 10))

print("Secuencia de Fibonacci: ", fibonacci(5))

print("División: ", realizar_division(10, 3))

print("Resta: ", realizar_resta(7, 4))

print("Suma: ", realizar_suma(5, 8))

print("Suma consecutiva de los dígitos: ", suma_consecutiva(123))
