#!/usr/bin/python3
"""
importamos la clase BaseGeometry desde el módulo 7-base_geometry.
 BaseGeometry proporciona métodos para validar atributos en geometrías.
"""
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
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        return self.__height * self.__width

    def __str__(self):
        return f"[Rectangle] {self.__width}/{self.__height}"
