# 3. N-ésimo término de la serie de Fibonacci de manera recursiva
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)



print("1to término de la serie de Fibonacci =", fibonacci(1))
print("2to término de la serie de Fibonacci =", fibonacci(2))
print("3to término de la serie de Fibonacci =", fibonacci(3))
print("4to término de la serie de Fibonacci =", fibonacci(4))
print("5to término de la serie de Fibonacci =", fibonacci(5))
print("6to término de la serie de Fibonacci =", fibonacci(6))
print("7to término de la serie de Fibonacci =", fibonacci(7))
print("8to término de la serie de Fibonacci =", fibonacci(8))
