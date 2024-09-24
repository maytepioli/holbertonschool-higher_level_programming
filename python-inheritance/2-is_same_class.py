#!/usr/bin/python3
"""
Este archivo contiene un objeto
"""


def is_same_class(obj, a_class):
    """
    Verifica si un objeto es exactamente una
    instancia de la clase especificada.

    Args:
        obj: El objeto a comprobar.
        a_class: La clase con la que se va a comparar.

    Returns:
    True si obj es una instancia de a_class; de
    lo contrario, False.
    """
    if type(obj) is a_class:
        return True
    else:
        return False
