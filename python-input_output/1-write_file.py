#!/usr/bin/python3
"""
# Esta función escribe un texto en un archivo especificado.
# Si el archivo ya existe, se generará un error, ya que se usa el modo 'x'.
# Devuelve la longitud del texto escrito.
"""


def write_file(filename="", text=""):

    """
    # Abre el archivo especificado por 'filename' en modo exclusivo ('x').
    # Esto significa que el archivo debe no existir previamente
    """

    with open(filename, 'x') as a:
        a.write(text)
    return len(text)
