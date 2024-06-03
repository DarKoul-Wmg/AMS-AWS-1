import os

def e3_capgiraNoms(directori_base):
    # Verificar si el directorio existe
    if not os.path.exists(directori_base):
        raise ValueError("El directori no existeix")

    # Recorrer el directorio base
    for element in os.listdir(directori_base):
        ruta_element = os.path.join(directori_base, element)
        if os.path.isdir(ruta_element):  # Verificar si es un directorio
            # Si es un directorio, llamar recursivamente a la función para explorarlo
            e3_capgiraNoms(ruta_element)
        elif os.path.isfile(ruta_element):  # Verificar si es un archivo
            # Obtener el nuevo nombre del archivo intercambiando los caracteres
            nou_nom = element[::-1]
            # Construir la ruta del nuevo archivo
            nova_ruta_arxiu = os.path.join(directori_base, nou_nom)
            # Renombrar el archivo
            os.rename(ruta_element, nova_ruta_arxiu)

# Ejemplo de uso:
try:
    e3_capgiraNoms('arxius/capgirar')
    print("Noms dels arxius han estat capgirats amb èxit.")
except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"Error inesperat: {e}")

