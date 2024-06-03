import json
import os

def e5_modificaJSON(arxiu, clau, valor):
    # Validación del nombre del archivo
    if not isinstance(arxiu, str):
        raise TypeError("El nom de l'arxiu no és de tipus cadena de text")

    # Validación de la existencia del archivo
    if not os.path.exists(arxiu):
        raise ValueError("L'arxiu no existeix")

    # Validación de la extensión del archivo
    if not arxiu.endswith('.json'):
        raise ValueError("L'arxiu no té extensió .json")

    # Lectura del archivo JSON
    with open(arxiu, 'r') as f:
        data = json.load(f)

    # Validación de la existencia de la clave en el JSON
    if clau not in data:
        raise ValueError("La clau no existeix al JSON")

    # Validación del tipo de valor
    if not isinstance(data[clau], type(valor)):
        raise TypeError("El tipus del valor no és el mateix que el valor de la clau")

    # Modificación del valor de la clave
    data[clau] = valor

    # Guardar el JSON modificado
    with open(arxiu, 'w') as f:
        json.dump(data, f, indent=4)

# Ejemplo de uso:
try:
    e5_modificaJSON('exemple.json', 'name', 'John Doe')
    print("JSON modificat amb èxit.")
except ValueError as e:
    print(f"Error: {e}")
except TypeError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"Error inesperat: {e}")
