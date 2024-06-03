def multipl_rus(numA,numB):
    resultado = 0
    if numA ==1:
        resultado += numB
        return resultado
    else:
        if numA %2 != 0:
            resultado += numB
        return resultado + multipl_rus(numA//2,numB*2)

A = 27
B = 82
print(multipl_rus(A,B))
