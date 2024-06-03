import os
import shutil

def e2_gestionaArxius(acció, arxiu1, arxiu2=None):
    # Validación de la acción
    if acció not in ('c', 'e', 'm'):
        raise ValueError("L'acció no és correcta")

    # Acción: Crear archivo
    if acció == 'c':
        # Verificar si el archivo ya existe
        if os.path.exists(arxiu1):
            raise ValueError("L'arxiu ja existeix")
        # Crear el archivo y escribir 'Contingut de prova'
        with open(arxiu1, 'w') as f:
            f.write('Contingut de prova')

    # Acción: Borrar archivo
    elif acció == 'e':
        # Verificar si el archivo existe
        if not os.path.exists(arxiu1):
            raise ValueError("L'arxiu no existeix")
        # Borrar el archivo
        os.remove(arxiu1)

    # Acción: Mover archivo
    elif acció == 'm':
        # Validar si se proporcionó el segundo archivo
        if arxiu2 is None:
            raise ValueError("Falta el segon arxiu")
        # Verificar si el archivo de origen existe
        if not os.path.exists(arxiu1):
            raise ValueError("L'arxiu no existeix")
        # Verificar si el archivo de destino ya existe
        if os.path.exists(arxiu2):
            raise ValueError("L'arxiu de destí ja existeix")
        # Mover el archivo de origen al archivo de destino
        shutil.move(arxiu1, arxiu2)

# Ejemplo de uso:
try:
    e2_gestionaArxius('c', 'nuevo_archivo.txt')
    e2_gestionaArxius('e', 'archivo_a_borrar.txt')
    e2_gestionaArxius('m', 'archivo_a_mover.txt', 'nueva_ruta/archivo_moved.txt')
except ValueError as e:
    print(f"Error: {e}")
except Exception as e:
    print(f"Error inesperat: {e}")
