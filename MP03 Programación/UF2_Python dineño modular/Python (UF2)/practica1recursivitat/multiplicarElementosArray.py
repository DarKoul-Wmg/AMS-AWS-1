def multiplicar_array(arr):
    if len(arr) == 0:
        return 1
    else:
        return arr[0] * multiplicar_array(arr[1:])


array = [1, 2, 3, 4, 5]
print("Producto de los elementos del Array:", multiplicar_array(array))
