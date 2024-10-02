#!/usr/bin/python3
"""
Importa el módulo 'json' para trabajar con datos en formato JSON.
"""
import json

"""
funcion que  Guarda un objeto en un archivo en formato JSON.
"""


def save_to_json_file(my_obj, filename):
    with open(filename, 'w') as a:
        json.dump(my_obj, a)
