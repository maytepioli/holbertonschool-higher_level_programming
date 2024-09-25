#!/usr/bin/python3
"""
importamos la clase Rectangle desde el módulo 9-rectangle.py.
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Clase Square que hereda de Rectangle.
    Representa un cuadrado y valida su tamaño.
    """
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        return self.__size * self.__size

    def __str__(self):
        return f"[Rectangle] {self.__size}/{self.__size}"
