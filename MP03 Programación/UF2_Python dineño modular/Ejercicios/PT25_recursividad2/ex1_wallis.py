def wallis(n):
    resultat = 2
    if n == 0:
        return resultat

    else:
        resultat *= (2*n / 2*n -1) * (2*n / 2*n +1)
        return resultat + wallis(n-1)

num = 4
print(wallis(num))


def wallis2(n):
    resultado = 1
    if n == 0:
        resultado = 2
        return resultado

    else:           #(2*n*2*n)
        resultado = (4*(n*n)) /((2*n-1)*(2*n+1)) * wallis2(n-1)
        return resultado
e12
num = 5
print(wallis2(num))

