#!/usr/bin/python3
"""
# Esta función agrega un texto al final de un archivo especificado.
# Si el archivo no existe, se creará uno nuevo.
# Devuelve la longitud del texto agregado.
"""


def append_write(filename="", text=""):

    """
    # Abre el archivo especificado por 'filename' en modo de adición ('a').
    # Esto permite que se escriba al final del archivo sin borrar
    # el contenido existente.
    """

    with open(filename, 'a') as a:
        a.write(text)
    return len(text)
