print("\nSIN DECORACIÓN:")


def multiplicacion_rusa(A, B):
    if A == 1:
        return B
    elif A % 2 == 0:
        return multiplicacion_rusa(A // 2, B * 2)
    else:
        return B + multiplicacion_rusa(A // 2, B * 2)

# Ejemplo de uso
A = 17
B = 23
resultado = multiplicacion_rusa(A, B)
print("Resultado de la multiplicación:", resultado)

print("\nCON DECORACIÓN:")


def multiplicacion_rusa(A, B):
    def helper(A, B, suma):
        print(f"{A:4}    {B:4}    {suma:4}")
        if A == 1:
            return suma
        elif A % 2 == 0:
            return helper(A // 2, B * 2, suma)
        else:
            suma += B
            return helper(A // 2, B * 2, suma)

    print("A       B       SUMES")
    suma = 0
    resultado = helper(A, B, suma)
    print(f"RESULTAT: {resultado}")


A = 27
B = 82
print("Tabla de multiplicación:")
resultado = multiplicacion_rusa(A, B)
