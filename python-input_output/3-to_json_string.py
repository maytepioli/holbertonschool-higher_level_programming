#!/usr/bin/python3
"""
Importa el módulo 'json' para trabajar con datos en formato JSON.
"""
import json

"""
    Función que convierte un objeto a su representación en formato JSON
"""


def to_json_string(my_obj):

    """
    Convierte un objeto a formato JSON y devuelve la cadena JSON.
    """

    return json.dumps(my_obj)
