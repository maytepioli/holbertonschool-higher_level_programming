#!/usr/bin/python3
class CountedIterator:
    def __init__(self, index):
        self.index = iter(index)
        self.counter = 0
    
    def get_count(self):
        return self.counter
    
    def __next__(self):
        value = next(self.index)
        self.counter += 1
        return value
