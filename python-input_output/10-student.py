#!/usr/bin/python3
"""
Este archivo contiene una clase Estudiantes
"""

class Student:
    """
    Este archivo contiene una clase Estudiantes
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        
    def to_json(self, attrs=None):
        # Si no se pasa attrs, devuelve todos los atributos
        if attrs is None:
            return self.__dict__
        
        # Si attrs es una lista, filtrar los atributos
        if type(attrs) is list:
            result = {}  # Cambié el nombre de dict a result
            for i in attrs:
                # Verificar si el atributo existe en la lista de atributos
                if i == 'first_name':
                    result[i] = self.first_name
                elif i == 'last_name':
                    result[i] = self.last_name
                elif i == 'age':
                    result[i] = self.age
            return result
