def formula_wallis(n):
    pi_aproximado = 2
    for i in range(1, n+1):
        pi_aproximado *= (4 * i**2) / (4 * i**2 - 1)
    return pi_aproximado


n = 1000000
pi_aproximado = formula_wallis(n)
print("Aproximación de pi usando la fórmula de Wallis con", n, "términos:", pi_aproximado)
