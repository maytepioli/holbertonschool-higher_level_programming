#!/usr/bin/python3
"""
Este archivo contiene un objeto
"""


def is_kind_of_class(obj, a_class):
    """
    Verifica si un objeto es una instancia de una clase o de una subclase.

    Args:
        obj: El objeto a comprobar.
        a_class: La clase con la que se va a comparar.

    Returns:
        True si obj es una instancia de a_class
        o de una subclase de a_class; de lo contrario, False.
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
