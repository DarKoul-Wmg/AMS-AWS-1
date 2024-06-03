def exercici6(num):
    hexadecimal_digits = [0,1,2,3,4,5,6,7,8,9,"A","B","C","D","E","F"]
    resultado = ""
    if 16 > num:
        resultado += str(hexadecimal_digits[num])
        return resultado
    else:
        if num%16 > 9:
            resultado += str(hexadecimal_digits[num % 16])
        else:
            resultado += str(num % 16)
        num = int(num // 16)

        return exercici6(num) + resultado

num = 5132
print(exercici6(num))

