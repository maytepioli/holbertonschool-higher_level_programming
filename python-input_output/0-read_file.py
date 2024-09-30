#!/usr/bin/python3
"""
Esta función lee el contenido de un archivo de texto y
lo imprime en la consola.
"""


def read_file(filename=""):

    """
    bre el archivo especificado por 'filename' en modo lectura ('r')
    """

    with open(filename, 'r') as a:
        reading = a.read()
        print(reading, end='')
