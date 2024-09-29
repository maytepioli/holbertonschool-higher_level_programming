#!/usr/bin/python3
from abc import ABC, abstractmethod
from math import pi


"""
 Clase abstracta que define la interfaz para formas geométricas
"""


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


"""
  Clase que representa un círculo
"""


class Circle(Shape):
    def __init__(self, radius):
        if radius < 0:
            radius = abs(radius)
        self.radius = radius

    def area(self):
        return pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * pi * self.radius


"""
clase que representa rectangulo
"""


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return (self.width * 2) + (self.height * 2)


"""
función para mostrar información sobre la forma
"""


def shape_info(shape):
    area = shape.area()
    perimeter = shape.perimeter()
    print(f"Area: {area}")
    print(f"Perimeter: {perimeter}")
