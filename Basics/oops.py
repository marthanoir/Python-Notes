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

Two Types: Class and Instance

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

# class Factory():  #class
#     a = 12        #attribute

#     def hello(self):  #method     #Self stores the location of the object
#         print("Hello how are you?")

#     print("How are you and This is getting initialized.")

# obj = Factory()     #OBJECT 

# print(Factory().a)
# Factory().hello()

# print(obj.a)

# class Factory():  #class
           
#     def __init__(self, material, zips, pockets):  #method
#             print(self)
#             self.material = material
#             self.zips = zips
#             self.pockets = pockets

#     def show(self):
#       print(f"Your object details are {self.material}, {self.zips} zips, {self.pockets} pockets.")

# reebok = Factory("leather", 1, 4) 
# campus = Factory("plastic", 1, 2)

# # print(reebok.pockets)

# reebok.show()
# campus.show()

# class Animal():

#     name = 'lion'       #class attribute

#     def __init__(self,age):
#         self.age = age      #instance attribute

#     def show(self):         #instance method
#         print("hellooo!!!")

#     @classmethod
#     def hello(cls):     #class method - can call only class attributes
#         print("Hello from class method.")

#     @staticmethod
#     def static():   #can call objects
#         print("Hello from statiic method")


# obj = Animal(12)

# obj.static()

'''
4 PILLARS OF OOPs

1. Encapsulation
2. Polymorphism
3. Abstraction
4. Inheritance
'''

#Inheritance

import math

class Calculator:
    def sum(self,a, b):
        return (a+b)

    def difference(self,a,b):
        return (a-b)

class AdvCalculator(Calculator):
    def multiply(self,a,b):
        return (a*b)

    def divide(self,a,b):
        return (a/b)

class SciCalculator(AdvCalculator):
    def mod(self,a,b):
        return (a%b)

    def power(self,a,b):
        c = math.pow(a,b)
        return (c)

calc = AdvCalculator()

print(calc.sum(3,5))
