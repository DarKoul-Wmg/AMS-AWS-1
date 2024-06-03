import csv
import os

def e0_llistaDades(arxiu, files, columnes):
    # Validación de la extensión del archivo
    if not arxiu[:-3]== 'csv':
        raise ValueError("L'arxiu no té extensió .csv")

    # Verificar si el archivo existe
    if not os.path.exists(arxiu):
        raise ValueError("L'arxiu no existeix")

    # Verificar si el archivo es un CSV válido
    with open(arxiu, 'r', newline='') as f:
        csv_reader = csv.reader(f)
        header = next(csv_reader)  # Leer la primera fila para obtener los nombres de las columnas
        if len(header) != len(columnes):
            raise TypeError("L'arxiu no és un .csv vàlid")

    # Verificar si las listas de filas y columnas están vacías
    if not files:
        raise ValueError("La llista de files és buida")
    if not columnes:
        raise ValueError("La llista de columnes és buida")

    # Verificar si las filas y columnas solicitadas existen
    with open(arxiu, 'r', newline='') as f:
        csv_reader = csv.reader(f)
        header = next(csv_reader)  # Leer la primera fila para obtener los nombres de las columnas

        for fila in files:
            if fila < 1:
                raise ValueError(f"La fila {fila} no existeix")
            if fila > sum(1 for _ in csv_reader):
                raise ValueError(f"La fila {fila} no existeix")

        for columna in columnes:
            if columna not in header:
                raise ValueError(f"La columna {columna} no existeix")

    # Leer y mostrar los datos de las filas y columnas especificadas
    with open(arxiu, 'r', newline='') as f:
        csv_reader = csv.reader(f)
        header = next(csv_reader)  # Leer la primera fila para obtener los nombres de las columnas

        for i, fila in enumerate(csv_reader, start=1):
            if i in files:
                valores_fila = [fila[header.index(col)] for col in columnes]
                print(f"Fila {i}: {', '.join(valores_fila)}")

# Ejemplo de uso:
try:
    e0_llistaDades("datos.csv", [1, 3], ["Nombre", "Edad"])
except ValueError as e:
    print(f"Error: {e}")
except TypeError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"Error inesperado: {e}")


