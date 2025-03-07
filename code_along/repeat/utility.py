def add_numbers(a, b):
    return a + b

class Person:
    def __init__(self, name, age=None):
        self.name = name
        self.age = age
        
    def greet(self):
        return f'Hi my name is {self.name}'
