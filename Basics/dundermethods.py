'''
DUNDER METHODS

Dunder methods are special methods in Python that begin and end with double underscores (`__`).

The word "dunder" comes from "double underscore".

These methods are also called magic methods and are used to define the behaviour of objects for built-in operations.

Some commonly used dunder methods are:

`__init__()` - Used as a constructor and called automatically when an object is created.

`__str__()` - Defines the string representation of an object.

`__len__()` - Defines the behaviour of the `len()` function.

`__add__()` - Defines the behaviour of the `+` operator.

Example:

class Student:

```
def __init__(self, name):
    self.name = name

def __str__(self):
    return self.name
```

student = Student("Richeek")

print(student)

'''

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return "Hi this is a dunder method. "

    def __add__(self, other):
        sum = 0
        for i in other:
            sum += i.age

        return f"Your sum of ages is {self.age + sum}."

obj = Animal("Animal 1", 20)
obj2 = Animal("Animal 2", 30)
obj3 = Animal("Animal 3", 10)

print(obj + (obj2,obj3)) # IF more than two ages, use tuple and in add method, use for loop and sum.