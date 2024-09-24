#!/usr/bin/python3
"""
Este archivo contiene una función para verificar la herencia de clases.
"""


def inherits_from(obj, a_class):
    """
    Verifica si un objeto es una instancia de una clase que hereda de a_class,
    pero no es una instancia de a_class en sí misma.

    Args:
        obj: El objeto a comprobar.
        a_class: La clase con la que se va a comparar.

    Returns:
        True si obj es una instancia de una subclase de
        a_class, de lo contrario False.
    """
    if isinstance(obj, a_class) and not type(obj) is a_class:
        return True
    else:
        False
