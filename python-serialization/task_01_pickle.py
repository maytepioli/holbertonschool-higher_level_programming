#!/usr/bin/env python3
import pickle


class CustomObject:
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        print(f'Name: {self.name}')
        print(f'Age: {self.age}')
        print(f'Is Student: {self.is_student}')

    def serialize(self, filename):
        with open(filename, 'wb') as f:
            return pickle.dump(self, f)

    @classmethod
    def deserialize(cls, filename):
        try:
            with open(filename, 'rb') as a:
                return pickle.load(a)
        except EOFError:
            return None
