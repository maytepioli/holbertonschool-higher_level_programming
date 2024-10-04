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

    def to_json(self):
        return self.__dict__
