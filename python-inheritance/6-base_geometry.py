#!/usr/bin/python3
"""
módulo base_geometry

Define la clase BaseGeometry como interfaz base para geometrías.
"""


class BaseGeometry:
    """
    Clase BaseGeometry.

    Esta clase sirve como una interfaz base para
    otras clases de geometría.
    No se debe instanciar directamente
    y debe ser subclases para definir
    geometrías específicas.
    """
    def area(self):
        raise Exception("area() is not implemented")
