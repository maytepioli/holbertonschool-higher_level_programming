#!/usr/bin/python3
"""
Importa el módulo 'json' para trabajar con datos en formato JSON.
"""
import json

"""
función que devuelve la descripción del diccionario con una
estructura de datos simple
"""


def class_to_json(obj):
    """
    función que devuelve la descripción del diccionario con una
    estructura de datos simple
    """

    dic = {}
    dic = obj.__dict__
    return dic
