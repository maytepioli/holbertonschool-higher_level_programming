#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Clase que representa un rectángulo, que hereda de BaseGeometry.

    Atributos:
        __width (int): El ancho del rectángulo.
        __height (int): La altura del rectángulo.
    Métodos:
    __init__(width, height): Inicializa un nuevo objeto Rectangle.
        """
    def __init__(self, width, height):
        """
    Inicializa un objeto Rectangle.

    Args:
    width (int): Ancho del rectángulo.
    height (int): Altura del rectángulo.

    Lanza:
    TypeError: Si no son enteros.
    ValueError: Si son <= 0.

    Valida los valores con `integer_validator` y los asigna.
    """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
