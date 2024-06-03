# ———————————————————————————————————————————————————————————————————————

print("Función: Calcular la suma de los elementos de una lista")


def sum_list(lst):
    if len(lst) == 0:
        return 0
    else:
        return lst[0] + sum_list(lst[1:])


original = [1, 2, 3, 4, 5]
total_sum = sum_list(original)
print("Lista:", original)
print("Suma:", total_sum)

# ———————————————————————————————————————————————————————————————————————
print("\n")
# ———————————————————————————————————————————————————————————————————————

print("Función: Encontrar el máximo valor en una lista")


def find_max(lst):
    if len(lst) == 1:
        return lst[0]
    else:
        max_rest = find_max(lst[1:])
        return lst[0] if lst[0] > max_rest else max_rest


original = [3, 7, 2, 9, 5]
max_value = find_max(original)
print("Lista:", original)
print("Máximo valor:", max_value)

# ———————————————————————————————————————————————————————————————————————
print("\n")
# ———————————————————————————————————————————————————————————————————————

print("Función: Calcular la longitud de una lista")


def list_length(lst):
    if not lst:
        return 0
    else:
        return 1 + list_length(lst[1:])


original = [1, 2, 3, 4, 5]
length = list_length(original)
print("Lista:", original)
print("Longitud:", length)

# ———————————————————————————————————————————————————————————————————————
print("\n")
# ———————————————————————————————————————————————————————————————————————

print("Función: Ordenar una lista utilizando el método de burbuja")


def bubble_sort(lst):
    n = len(lst)
    if n == 1:
        return lst
    for i in range(n-1):
        if lst[i] > lst[i+1]:
            lst[i], lst[i+1] = lst[i+1], lst[i]
    return bubble_sort(lst[:-1]) + [lst[-1]]


original = [5, 3, 8, 2, 1, 7, 4, 6]
sorted_lst = bubble_sort(original)
print("Original:", original)
print("Ordenada con burbuja:", sorted_lst)

# ———————————————————————————————————————————————————————————————————————
print("\n")
# ———————————————————————————————————————————————————————————————————————


def bubble_sort2(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n-i-1):
            if lista[j] > lista[j+1]:
                lista[j], lista[j+1] = lista[j+1], lista[j]


numeros = [5, 3, 8, 2, 1, 7, 4, 6]
bubble_sort2(numeros)
print("Lista ordenada sin símbolos:")
for numero in numeros:
    print(numero, end=' ')
print()

# ———————————————————————————————————————————————————————————————————————
print("\n")
# ———————————————————————————————————————————————————————————————————————

print("Función: Calcular la suma de los elementos pares en una lista")


def sum_even(lst):
    if not lst:
        return 0
    else:
        current = lst[0] if lst[0] % 2 == 0 else 0
        return current + sum_even(lst[1:])


original = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
total_sum_even = sum_even(original)
print("Lista:", original)
print("Suma de pares:", total_sum_even)

# ———————————————————————————————————————————————————————————————————————
print("\n")
# ———————————————————————————————————————————————————————————————————————

print("Función: Calcular la suma de los elementos impares en una lista")


def sum_even(lst):
    if not lst:
        return 0
    else:
        current = lst[0] if lst[0] % 2 == 1 else 0
        return current + sum_even(lst[1:])


original = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
total_sum_even = sum_even(original)
print("Lista:", original)
print("Suma de impares:", total_sum_even)

# ———————————————————————————————————————————————————————————————————————
print("\n")
# ———————————————————————————————————————————————————————————————————————

print("Función: Verificar si una lista está ordenada")


def is_sorted(lst):
    if len(lst) <= 1:
        return True
    else:
        return lst[0] <= lst[1] and is_sorted(lst[1:])


sorted_list = [1, 2, 3, 4, 5]
unsorted_list = [5, 2, 8, 1, 3]
print("Lista ordenada:", is_sorted(sorted_list))
print("Lista desordenada:", is_sorted(unsorted_list))

# ———————————————————————————————————————————————————————————————————————
print("\n")
# ———————————————————————————————————————————————————————————————————————

print("Función: Eliminar duplicados de una lista")


def remove_duplicates(lst):
    if not lst:
        return []
    elif lst[0] not in lst[1:]:
        return [lst[0]] + remove_duplicates(lst[1:])
    else:
        return remove_duplicates(lst[1:])


original = [1, 2, 2, 3, 4, 4, 5]
unique_elements = remove_duplicates(original)
print("Lista original:", original)
print("Sin duplicados:", unique_elements)

# ———————————————————————————————————————————————————————————————————————
print("\n")
# ———————————————————————————————————————————————————————————————————————

print("Función: Calcular el producto de los elementos en una lista")


def product(lst):
    if not lst:
        return 1
    else:
        return lst[0] * product(lst[1:])


original = [1, 2, 3, 4, 5]
result = product(original)
print("Lista:", original)
print("Producto de los elementos:", result)

# ———————————————————————————————————————————————————————————————————————
print("\n")
# ———————————————————————————————————————————————————————————————————————

print("Función: Revertir el orden de los elementos en grupos de tamaño k")


def reverse_groups(lst, k):
    if len(lst) < k:
        return lst[::-1]
    else:
        return lst[k-1::-1] + reverse_groups(lst[k:], k)


original = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
group_size = 3
reversed_groups = reverse_groups(original, group_size)
print("Lista original:", original)
print("Grupos revertidos de tamaño", group_size, ":", reversed_groups)

# ———————————————————————————————————————————————————————————————————————
print("\n")
# ———————————————————————————————————————————————————————————————————————

print("Función: Promedio")


def average(lst):
    if not lst:
        return None
    else:
        return sum(lst) / len(lst)


original = [1, 2, 3, 4, 5]
avg = average(original)
print("Lista:", original)
print("Promedio de los elementos:", avg)

# ———————————————————————————————————————————————————————————————————————
print("\n")
# ———————————————————————————————————————————————————————————————————————


def merge_lists(lst1, lst2):
    merged = []
    min_len = min(len(lst1), len(lst2))
    for i in range(min_len):
        merged.append(lst1[i])
        merged.append(lst2[i])
    merged.extend(lst1[min_len:] if len(lst1) > len(lst2) else lst2[min_len:])
    return merged


list1 = [1, 3, 5, 7]
list2 = [2, 4, 6, 8, 10]
merged_list = merge_lists(list1, list2)
print("Lista 1:", list1)
print("Lista 2:", list2)
print("Listas combinadas:", merged_list)

# ———————————————————————————————————————————————————————————————————————
print("\n")
# ———————————————————————————————————————————————————————————————————————


def remove_duplicates_ordered(lst):
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


original = [1, 3, 2, 4, 3, 5, 2, 6, 7, 7, 8]
unique_elements = remove_duplicates_ordered(original)
print("Lista original:", original)
print("Sin duplicados (manteniendo el orden):", unique_elements)

# ———————————————————————————————————————————————————————————————————————
print("\n")
# ———————————————————————————————————————————————————————————————————————


def intersection(lst1, lst2):
    set1 = set(lst1)
    set2 = set(lst2)
    return list(set1.intersection(set2))


list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
intersect = intersection(list1, list2)
print("Lista 1:", list1)
print("Lista 2:", list2)
print("Intersección:", intersect)

# ———————————————————————————————————————————————————————————————————————
print("\n")
# ———————————————————————————————————————————————————————————————————————


def is_palindrome(lst):
    reversed_lst = lst[::-1]
    return lst == reversed_lst


palindrome_list = [1, 2, 3, 2, 1]
non_palindrome_list = [1, 2, 3, 4, 5]
print("Lista palíndromo:", is_palindrome(palindrome_list))
print("Lista no palíndromo:", is_palindrome(non_palindrome_list))

# ———————————————————————————————————————————————————————————————————————
print("\n")
# ———————————————————————————————————————————————————————————————————————


def split_list(lst, n):
    split_size = len(lst) // n
    return [lst[i:i+split_size] for i in range(0, len(lst), split_size)]


original = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
num_parts = 3
split_lists = split_list(original, num_parts)
print(f"Lista original: {original}")
print(f"Dividida en {num_parts} partes iguales:", split_lists)

# ———————————————————————————————————————————————————————————————————————
print("\n")
# ———————————————————————————————————————————————————————————————————————


def rotate_list(lst, k):
    k %= len(lst)
    return lst[-k:] + lst[:-k]


original = [1, 2, 3, 4, 5]
rotated_left = rotate_list(original, 2)  # Rotar hacia la izquierda
rotated_right = rotate_list(original, -2)  # Rotar hacia la derecha
print("Lista original:", original)
print("Rotada hacia la izquierda:", rotated_left)
print("Rotada hacia la derecha:", rotated_right)

# ———————————————————————————————————————————————————————————————————————
print("\n")
# ———————————————————————————————————————————————————————————————————————


def filter_list(lst, condition):
    return [x for x in lst if condition(x)]

# Ejemplo de uso:
original = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filtered_even = filter_list(original, lambda x: x % 2 == 0)  # Filtrar números pares
filtered_gt_5 = filter_list(original, lambda x: x > 5)  # Filtrar números mayores que 5
print("Lista original:", original)
print("Elementos pares:", filtered_even)
print("Elementos mayores que 5:", filtered_gt_5)

# ———————————————————————————————————————————————————————————————————————
print("\n")
# ———————————————————————————————————————————————————————————————————————


def apply_function(lst, operation):
    return [operation(x) for x in lst]


def square(x):
    return x ** 2


def double(x):
    return x * 2


def triple(x):
    return x * 3


original = [1, 2, 3, 4, 5]
squared = apply_function(original, square)
doubled = apply_function(original, double)
tripled = apply_function(original, triple)
print("Lista original:", original)
print("Cuadrados de los elementos:", squared)
print("Dobles de los elementos:", doubled)
print("Triples de los elementos:", tripled)

# ———————————————————————————————————————————————————————————————————————
print("\n")
# ———————————————————————————————————————————————————————————————————————


def combine_lists(lst1, lst2):
    return [x + y for x, y in zip(lst1, lst2)]


list1 = [1, 2, 3, 4, 5]
list2 = [10, 20, 30, 40, 50]
combined = combine_lists(list1, list2)
print("Lista 1:", list1)
print("Lista 2:", list2)
print("Lista combinada:", combined)

# ———————————————————————————————————————————————————————————————————————
print("\n")
# ———————————————————————————————————————————————————————————————————————


def remove_odd_numbers(lst):
    return [x for x in lst if x % 2 == 0]


original = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens_only = remove_odd_numbers(original)
print("Lista original:", original)
print("Solo números pares:", evens_only)

# ———————————————————————————————————————————————————————————————————————
print("\n")
# ———————————————————————————————————————————————————————————————————————


def remove_even_numbers(lst):
    return [x for x in lst if x % 2 == 1]


original = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odds_only = remove_odd_numbers(original)
print("Lista original:", original)
print("Solo números impares:", odds_only)

# ———————————————————————————————————————————————————————————————————————
print("\n")
# ———————————————————————————————————————————————————————————————————————


def mean(lst):
    return sum(lst) / len(lst) if lst else None


numbers = [2, 4, 6, 8, 10]
average = mean(numbers)
print("Lista de números:", numbers)
print("Media de la lista:", average)

# ———————————————————————————————————————————————————————————————————————
print("\n")
# ———————————————————————————————————————————————————————————————————————


def mode(lst):
    freq_map = {}
    max_count = 0
    mode_values = []

    for num in lst:
        if num not in freq_map:
            freq_map[num] = 1
        else:
            freq_map[num] += 1

        if freq_map[num] > max_count:
            max_count = freq_map[num]
            mode_values = [num]
        elif freq_map[num] == max_count:
            mode_values.append(num)

    return mode_values


data = [1, 2, 2, 3, 4, 4, 4, 5, 5, 5, 5]
mode_value = mode(data)
print("Datos:", data)
print("Moda de los datos:", mode_value)
