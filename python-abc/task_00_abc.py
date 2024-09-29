#!/usr/bin/python3
from abc import ABC, abstractmethod
"""
Clase abstracta que define la interfaz para los animales
"""


class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass
        """
         Método abstracto que debe ser implementado por las subclases
        """


class Dog(Animal):

    def sound(self):
        return "Bark"
    """
    Implementación del método sound para el perro
    """


class Cat(Animal):
    def sound(self):
        return "Meow"
    """
    Implementación del método sound para el gato
    """
