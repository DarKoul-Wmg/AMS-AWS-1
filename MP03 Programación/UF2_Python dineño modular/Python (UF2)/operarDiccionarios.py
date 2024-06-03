def suma_valores(dic):
    total = 0
    for valor in dic.values():
        if isinstance(valor, dict):
            total += suma_valores(valor)
        else:
            total += valor
    return total


diccionario = {'a': 1, 'b': {'c': 2, 'd': {'e': 3}}}
print("La suma de los valores es:", suma_valores(diccionario))


# ———————————————————————————————————————————————————————————————————————
print("\n")
# ———————————————————————————————————————————————————————————————————————


def buscar_clave(dic, clave):
    if clave in dic:
        return True
    for valor in dic.values():
        if isinstance(valor, dict):
            if buscar_clave(valor, clave):
                return True
    return False


diccionario = {'a': 1, 'b': {'c': 2, 'd': {'e': 3}}}
clave = 'e'
print("La clave '{}' está presente:".format(clave), buscar_clave(diccionario, clave))

# ———————————————————————————————————————————————————————————————————————
print("\n")
# ———————————————————————————————————————————————————————————————————————


def contar_elementos(dic):
    count = len(dic)
    for valor in dic.values():
        if isinstance(valor, dict):
            count += contar_elementos(valor)
    return count

# Ejemplo de uso
diccionario = {'a': 1, 'b': {'c': 2, 'd': {'e': 3}}}
print("El número total de elementos es:", contar_elementos(diccionario))

# ———————————————————————————————————————————————————————————————————————
print("\n")
# ———————————————————————————————————————————————————————————————————————


def profundidad_dic(dic):
    if not isinstance(dic, dict):
        return 0
    max_prof = 0
    for valor in dic.values():
        if isinstance(valor, dict):
            prof = profundidad_dic(valor)
            if prof > max_prof:
                max_prof = prof
    return 1 + max_prof


diccionario = {'a': 1, 'b': {'c': 2, 'd': {'e': 3}}}
print("La profundidad máxima del diccionario es:", profundidad_dic(diccionario))

# ———————————————————————————————————————————————————————————————————————
print("\n")
# ———————————————————————————————————————————————————————————————————————


def imprimir_claves(dic):
    for clave, valor in dic.items():
        print(clave)
        if isinstance(valor, dict):
            imprimir_claves(valor)


diccionario = {'a': 1, 'b': {'c': 2, 'd': {'e': 3}}}
print("Las claves del diccionario son:")
imprimir_claves(diccionario)

# ———————————————————————————————————————————————————————————————————————
print("\n")
# ———————————————————————————————————————————————————————————————————————


def suma_para_clave(dic, clave):
    total = 0
    for k, v in dic.items():
        if k == clave:
            if isinstance(v, int):
                total += v
        elif isinstance(v, dict):
            total += suma_para_clave(v, clave)
    return total

diccionario = {'a': 1, 'b': {'c': 2, 'd': {'e': 3, 'f': 4}}}
clave = 'd'
print("La suma de los valores para la clave '{}' es:".format(clave), suma_para_clave(diccionario, clave))

# ———————————————————————————————————————————————————————————————————————
print("\n")
# ———————————————————————————————————————————————————————————————————————


def es_simetrico(dic):
    if not isinstance(dic, dict):
        return True
    first = next(iter(dic.values()))
    if isinstance(first, dict):
        for valor in dic.values():
            if not es_simetrico(valor):
                return False
        return True
    else:
        return all(isinstance(valor, type(first)) for valor in dic.values())


diccionario1 = {'a': {'b': 1, 'c': 2}, 'd': {'e': 3, 'f': 4}}
diccionario2 = {'a': {'b': 1, 'c': 2}, 'd': {'e': 3, 'f': 'four'}}
print("¿El diccionario 1 es simétrico?:", es_simetrico(diccionario1))
print("¿El diccionario 2 es simétrico?:", es_simetrico(diccionario2))

# ———————————————————————————————————————————————————————————————————————
print("\n")
# ———————————————————————————————————————————————————————————————————————


def contar_apariciones(dic, clave):
    count = 0
    for k, v in dic.items():
        if k == clave:
            count += 1
        if isinstance(v, dict):
            count += contar_apariciones(v, clave)
    return count


diccionario = {'a': 1, 'b': {'c': 2, 'd': {'a': 3, 'e': 4}}}
clave = 'a'
print("La clave '{}' aparece {} veces en el diccionario.".format(clave, contar_apariciones(diccionario, clave)))

# ———————————————————————————————————————————————————————————————————————
print("\n")
# ———————————————————————————————————————————————————————————————————————


def invertir_dic(dic):
    inv_dic = {}
    for clave, valor in dic.items():
        if isinstance(valor, dict):
            inv_dic.update(invertir_dic(valor))
        else:
            inv_dic.setdefault(valor, []).append(clave)
    return inv_dic


diccionario = {'a': 1, 'b': {'c': 2, 'd': {'e': 3}}}
print("Diccionario original:", diccionario)
print("Diccionario invertido:", invertir_dic(diccionario))

# ———————————————————————————————————————————————————————————————————————
print("\n")
# ———————————————————————————————————————————————————————————————————————


def calcular_tamano_archivos(sistema_archivos):
    """ Calcula el tamaño total de todos los archivos en el sistema de archivos, incluyendo los archivos en
    subdirectorios.
    Args: sistema_archivos (dict): Un diccionario que representa la estructura del sistema de archivos.
    Returns: int: El tamaño total de todos los archivos en el sistema de archivos. """
    total_tamano = 0
    for valor in sistema_archivos.values():
        if isinstance(valor, dict):
            total_tamano += calcular_tamano_archivos(valor)  # Llamada recursiva para los subdirectorios
        elif isinstance(valor, int):
            total_tamano += valor
    return total_tamano


sistema_archivos = {
    'docs': {
        'documento1.txt': 100,
        'documento2.txt': 200,
        'subdir': {
            'documento3.txt': 150,
            'documento4.txt': 300
        }},
    'images': {
        'imagen1.jpg': 500,
        'imagen2.jpg': 700
    }}

print("El sistema de archivos es:", sistema_archivos)
print("El tamaño total de todos los archivos en el sistema de archivos es:", calcular_tamano_archivos(sistema_archivos), "bytes.")

# ———————————————————————————————————————————————————————————————————————
print("\n")
# ———————————————————————————————————————————————————————————————————————


def crear_diccionario(**kwargs):
    """
    Crea un diccionario a partir de un número variable de argumentos clave-valor.

    Args:
    - **kwargs: Argumentos clave-valor.

    Returns:
    - dict: El diccionario creado a partir de los argumentos.
    """
    diccionario = {}
    for clave, valor in kwargs.items():
        diccionario[clave] = valor
    return diccionario


diccionario = crear_diccionario(a=1, b=2, c=3)
print("Diccionario creado:", diccionario)

# ———————————————————————————————————————————————————————————————————————
print("\n")
# ———————————————————————————————————————————————————————————————————————


def bubble_sort_dict_keys(diccionario):
    keys = list(diccionario.keys())
    n = len(keys)
    for i in range(n):
        for j in range(0, n-i-1):
            if keys[j] > keys[j+1]:
                keys[j], keys[j+1] = keys[j+1], keys[j]
    return {k: diccionario[k] for k in keys}

# Ejemplo de uso:
diccionario = {'b': 2, 'a': 1, 'd': 4, 'c': 3}
diccionario_ordenado = bubble_sort_dict_keys(diccionario)
print("Diccionario ordenado por claves:")
print(diccionario_ordenado)

# ———————————————————————————————————————————————————————————————————————
print("\n")
# ———————————————————————————————————————————————————————————————————————


def bubble_sort_dict_values(diccionario):
    items = list(diccionario.items())
    n = len(items)
    for i in range(n):
        for j in range(0, n-i-1):
            if items[j][1] > items[j+1][1]:
                items[j], items[j+1] = items[j+1], items[j]
    return {k: v for k, v in items}

# Ejemplo de uso:
diccionario = {'b': 2, 'a': 1, 'd': 4, 'c': 3}
diccionario_ordenado = bubble_sort_dict_values(diccionario)
print("Diccionario ordenado por valores:")
print(diccionario_ordenado)

# ———————————————————————————————————————————————————————————————————————
print("\n")
# ———————————————————————————————————————————————————————————————————————


def bubble_sort_dict_keys(diccionario):
    keys = list(diccionario.keys())
    n = len(keys)
    for i in range(n):
        for j in range(0, n-i-1):
            if keys[j] > keys[j+1]:
                keys[j], keys[j+1] = keys[j+1], keys[j]
    return keys

# Ejemplo de uso:
diccionario = {'b': 2, 'a': 1, 'd': 4, 'c': 3}
keys_ordenadas = bubble_sort_dict_keys(diccionario)
print("Claves del diccionario ordenadas:")
for key in keys_ordenadas:
    print(key, end=' ')
print()


# ———————————————————————————————————————————————————————————————————————
print("\n")
# ———————————————————————————————————————————————————————————————————————


def bubble_sort_dict_values(diccionario):
    items = list(diccionario.items())
    n = len(items)
    for i in range(n):
        for j in range(0, n-i-1):
            if items[j][1] > items[j+1][1]:
                items[j], items[j+1] = items[j+1], items[j]
    return items

# Ejemplo de uso:
diccionario = {'b': 2, 'a': 1, 'd': 4, 'c': 3}
items_ordenados = bubble_sort_dict_values(diccionario)
print("Valores del diccionario ordenados:")
for key, value in items_ordenados:
    print(value, end=' ')
print()

