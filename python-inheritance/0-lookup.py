#!/usr/bin/python3
def lookup(obj):
    """
    Devuelve una lista de atributos y métodos disponibles de un objeto.

    Args:
        obj: El objeto del cual se quieren obtener los atributos y métodos.

    Returns:
    list: Una lista de nombres de los atributos y métodos del
    objeto,incluyendo los heredados y los especiales.
    """
    return dir(obj)
