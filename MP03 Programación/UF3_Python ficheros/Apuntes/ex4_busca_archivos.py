import os

def buscaArxius(directori, paraules, condicio):
    # Validación del directorio
    if not isinstance(directori, str):
        raise TypeError("El valor de directori no és de tipus cadena")
    if not os.path.exists(directori):
        raise ValueError("El directori no existeix")

    # Validación de la condición
    if condicio not in ['totes', 'alguna']:
        raise ValueError("La condició no és correcta")

    # Validación de la lista de palabras
    if not isinstance(paraules, list):
        raise TypeError("El valor de paraules no és de tipus llista")
    if not paraules:
        raise ValueError("La llista de paraules és buida")

    # Lista para almacenar los nombres de los archivos que cumplen la condición
    arxius_coincidents = []

    # Recorrer los archivos en el directorio
    for arxiu in os.listdir(directori):
        ruta_arxiu = os.path.join(directori, arxiu)
        if os.path.isfile(ruta_arxiu):  # Verificar si es un archivo
            if condicio == 'totes':
                if all(paraula in open(ruta_arxiu).read() for paraula in paraules):
                    arxius_coincidents.append(arxiu)
            elif condicio == 'alguna':
                if any(paraula in open(ruta_arxiu).read() for paraula in paraules):
                    arxius_coincidents.append(arxiu)

    return arxius_coincidents

# Ejemplo de uso:
try:
    resultats = buscaArxius('directori', ['paraula1', 'paraula2'], 'totes')
    print("Arxius que compleixen la condició:", resultats)
except ValueError as e:
    print(f"Error: {e}")
except TypeError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"Error inesperat: {e}")
