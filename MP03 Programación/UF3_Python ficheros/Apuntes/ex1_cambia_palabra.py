import os

def e1_canviaParaula(arxiu, paraula, substitucio):
    # Validación de la extensión del archivo
    if not arxiu.endswith('.txt'):
        raise ValueError("L'arxiu no té extensió .txt")

    # Verificar si el archivo existe
    if not os.path.exists(arxiu):
        raise ValueError("L'arxiu no existeix")

    # Realizar la sustitución de palabras
    try:
        # Abrir el archivo original para lectura y escritura
        with open(arxiu, 'r+') as f:
            # Leer y procesar línea por línea
            while True:
                pos = f.tell()  # Obtener la posición actual en el archivo
                line = f.readline()  # Leer una línea del archivo
                if not line:  # Si no hay más líneas, salir del bucle
                    break
                if paraula in line:
                    # Realizar la sustitución de la palabra en la línea
                    line = line.replace(paraula, substitucio)
                    # Regresar al inicio de la línea y escribir la línea modificada
                    f.seek(pos)
                    f.write(line)

    except UnicodeDecodeError:
        raise TypeError("L'arxiu no és un .txt vàlid")

# Ejemplo de uso:
try:
    e1_canviaParaula("text.txt", "hola", "adeu")
except ValueError as e:
    print(f"Error: {e}")
except TypeError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"Error inesperat: {e}")
