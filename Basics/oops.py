'''
OBJECT-ORIENTED PROGRAMMING (OOP)

Object-Oriented Programming is a programming paradigm based on the concept of objects.

It is used to structure a program by bundling related properties and behaviours into objects.

CLASS

A class is a blueprint or a template for creating objects.

It defines the attributes and methods that the objects created from the class will have.

OBJECT

An object is an instance of a class.

It is created using the class and can access the attributes and methods defined in the class.

For example:

class Student:
name = "Richeek"
age = 21

student1 = Student()

print(student1.name)
print(student1.age)

Here, Student is a class and student1 is an object of the Student class.

ATTRIBUTES

Attributes are the variables that belong to an object or class.

They represent the properties or characteristics of an object.

METHODS

Methods are functions that are defined inside a class.

They represent the behaviour or actions that an object can perform.

CONSTRUCTOR

A constructor is a special method that is automatically called when an object is created.

In Python, the constructor is written using **init**().

Example:

class Student:

```
def __init__(self, name, age):
    self.name = name
    self.age = age
```

student1 = Student("Richeek", 21)

print(student1.name)
print(student1.age)

'''

