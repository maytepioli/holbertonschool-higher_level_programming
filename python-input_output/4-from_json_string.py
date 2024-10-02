#!/usr/bin/python3
"""
Importa el módulo 'json' para trabajar con datos en formato JSON.
"""
import json

"""
    Función que convierte un objeto a su representación en formato JSON
"""


def from_json_string(my_str):

    """
    Convierte una cadena JSON a un objeto de Python.
    """

    return json.loads(my_str)
