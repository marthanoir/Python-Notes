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

# Multilevel Inheritance

# import math

# class Calculator: #PARENT CLASS
#     def sum(self,a, b):
#         return (a+b)

#     def difference(self,a,b):
#         return (a-b)

# class AdvCalculator(Calculator): #CHILD CLASS
#     def multiply(self,a,b):
#         return (a*b)

#     def divide(self,a,b):
#         return (a/b)

# class SciCalculator(AdvCalculator):
#     def mod(self,a,b):
#         return (a%b)

#     def power(self,a,b):
#         c = math.pow(a,b)
#         return (c)

# calc = AdvCalculator()

# print(calc.sum(3,5))


# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def show(self):
#         print(f"Your name is {self.name}.")

# class Human(Animal):
#     pass

# animal1 = Animal("lion")
# person1 = Human("Richeek")
# person1.show()

# class Animal():
#     def __init__(self, name):
#         self.name = name

#     def show(self):
#         print(f"Your name is {self.name}.")

# class Human(Animal):
#     def __init__(self, name, age):
#         super().__init__(name) #super keyword targets the parent class for attributes
#         self.age = age

#     def show(self):     #Method Overriding
#             print(f"Your name is {self.name} and age is {self.age}.")

# animal1 = Animal("lion")
# person1 = Human("Richeek",21)
# person1.show()


# class Animal:
#     name1 = "lion"

# class Human:
#     name2 = "Richeek"

# class Robot(Animal, Human):
#     name3 = "Robot 2.0"
'''
 if the names of the attributes are same in all three class, then there
 will be method overriding and the last name of the of the attribute
 will be executed everytime.
'''
# obj = Robot()
# print(obj.name1)
# print(obj.name2)
# print(obj.name3)

#mMltiple Inheritance 

# class Animal():
#     def __init__(self, name):
#         pass

# class Human:
#     def __init__(self, name, age):
#         pass

# class Robot(Animal, Human): #This will take parameters based on Animal as human is prioritized
#     name3 = "Robot 2.0"

# class Robot2(Human, Animal): #This will take parameters based on Human as human is prioritized
#     name3 = "Robot 2.0"

# # Done by MRO( Method Resolution Order)

# obj = Robot("Hi Robo")
# obj = Robot2("Richeek", 3)

# class Factory():
#     def __init__(self, material, zips):
#         self.material = material
#         self.zips = zips

# class PuneFactory(Factory):
#     def __init__(self, material, zips, pockets):
#         super().__init__(material, zips)
#         self.pockets = pockets

# class Bhopalfactory(PuneFactory):
#     def __init__(self, material, zips, pockets, color):
#         super().__init__(material, zips, pockets)
#         self.color = color

#     def show(self):
#         print(f"The cloth you want is made of {self.material}, has {self.zips} zip, {self.pockets} pockets and is of {self.color} color. ")

# obj = Bhopalfactory("leather", 1, 4, "blue")
# obj.show()


'''
POLYMORPHISM

Polymorphism means "many forms".
In Python, polymorphism allows objects of different classes to be treated as objects of 
a common superclass.

There are different ways to achieve polymorphism in Python:

Method Overloading
Method Overriding
Duck Typing

METHOD OVERLOADING

Method overloading means defining multiple methods with the same name but different parameters.
Python does not support traditional method overloading like Java or C++.
However, we can achieve similar behaviour using default arguments or variable-length arguments.

METHOD OVERRIDING

Method overriding occurs when a subclass provides a specific implementation of a 
method that is already defined in its parent class.

DUCK TYPING

Duck typing is a concept in Python where the type or class of an object is less important 
than the methods or behaviour it supports.
'''

# Method Overriding

# class Animal:
#     def show(self):
#         print("Hello this is parent class.")

# class Human:
#     def show(self):
#         print("Hello this is child class")

# obj = Human()
# obj.show()

# Duck Typing

# class Animal:
#     def show(self):
#         print("Hello this is parent class.")

# class Human:
#     def show(self):
#         print("Hello this is child class")

# obj = Animal()
# obj2 = Human()

# obj.show()
# obj2.show()

'''
ENCAPSULATION

Encapsulation is the process of bundling data (attributes) and methods that operate on that data into a single unit, usually a class.

It is used to restrict direct access to some of an object's components and protect the data from unwanted changes.

ACCESS MODIFIERS

Python does not have strict access modifiers like Java or C++.

However, Python uses naming conventions to indicate the accessibility of attributes and methods.

1. Public

Public members can be accessed from anywhere.

2. Protected

Protected members are indicated by a single underscore (_) before the name. But this is not 
useful as the attributes can still be accessed.
In other languges, it is useful, that's the reason we use the protected keyword,
so that when we share it to someone they can implement this in their own language where it works.

3. Private

Private members are indicated by two underscores (__) before the name.

Encapsulation helps in data hiding and provides better control over how 
the data is accessed and modified.

'''

# class Demo:
#     def __init__(self, name, age, salary):
#         self.name = name        #PUBLIC
#         self._age = age         #PROTECTED
#         self.__salary = salary  #PRIVATE

#     def show(self):   #GETTER
#         print("Inside the class: ")
#         print("Public Class: ",self.name)
#         print("Protected Class: ", self._age)
#         print("Private Class: ", self.__salary)     #accessing private attributes

# obj = Demo("Richeek", 21, 10000)
# obj.show()

'''
ABSTRACTION

Abstraction is the process of hiding the implementation details and showing only 
the essential features of an object.

It helps in reducing complexity and allows the user to focus on what an object does 
rather than how it does it.

In Python, abstraction does not exist but can be achieved using abstract classes and 
abstract methods from the abc module.

Abstract Class

An abstract class is a class that cannot be instantiated directly.

It is used as a blueprint for other classes.

Abstract Method

An abstract method is a method that is declared in an abstract class but does not 
have an implementation.

The subclasses must provide an implementation for the abstract methods.
'''

from abc import ABC, abstractmethod
import math

class abstract(ABC):
    @abstractmethod     #decorator
    def perimeter(self):
        pass

    @abstractmethod
    def area(self):
        pass

class Square(abstract):
    def __init__(self, side):
        self.side = side

    def perimeter(self):
        per = 4*self.side
        return per

    def area(self):
        ar = self.side*self.side
        return ar

    def show(self):
         print(f"The perimeter is {self.perimeter()} and the area is {self.area()}.")

class Circle(abstract):
    def __init__(self, radius):
        self.radius = radius

    def perimeter(self):
            per = 2*math.pi*self.radius
            return per
    
    def area(self):
            ar = math.pi*self.radius*self.radius
            return ar
    def show(self):
             print(f"The perimeter is {self.perimeter()} and the area is {self.area()}.")

obj = Square(5)
obj2 = Circle(7)
obj.show()
obj2.show()