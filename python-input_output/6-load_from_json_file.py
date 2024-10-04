#!/usr/bin/python3
"""
Importa el módulo 'json' para trabajar con datos en formato JSON.
"""
import json

"""
funcion que crea un objeto a partir de un archivo JSON
"""

def load_from_json_file(filename):
    with open(filename, 'r') as file:
        obj = json.load(file)
        return obj
