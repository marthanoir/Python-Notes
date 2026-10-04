'''
ADVANCED PYTHON

DECORATORS

Decorators are a powerful feature in Python that allows you to modify or extend the behaviour 
of a function or class without changing its actual code.

A decorator is a function that takes another function as an argument and returns a new function 
with additional functionality.

*args AND **kwargs

*args allows a function to accept any number of positional arguments.

**kwargs allows a function to accept any number of keyword arguments.

Example:

def add(*args):
return sum(args)

print(add(1, 2, 3, 4))

def student(**kwargs):
print(kwargs)

student(name="Richeek", age=21)

COMPREHENSIONS

Comprehensions provide a concise way to create collections such as lists, sets, and dictionaries.

They allow us to create a new collection in a single line of code.

Example:

numbers = [1, 2, 3, 4, 5]

squares = [x**2 for x in numbers]

print(squares)

LAMBDA

A lambda function is a small anonymous function that can take any number of arguments but can have 
only one expression.

Syntax:

lambda arguments: expression

Example:

square = lambda x: x**2

print(square(5))

MAP()

The map() function is used to apply a function to every item in an iterable.

Example:

numbers = [1, 2, 3, 4, 5]

squares = list(map(lambda x: x**2, numbers))

print(squares)

FILTER()

The filter() function is used to filter elements from an iterable based on a condition.

Example:

numbers = [1, 2, 3, 4, 5]

even = list(filter(lambda x: x % 2 == 0, numbers))

print(even)

MODULES

A module is a Python file containing Python code such as functions, classes, and variables.

Modules help us organise code into separate files and make the code reusable.

A module can be imported using the import keyword.

Example:

import math

print(math.sqrt(25))

PACKAGES

A package is a collection of modules organised in a directory.

Packages help in organising large Python projects into smaller and manageable parts.

A package generally contains an **init**.py file.

Example structure:

my_package/
**init**.py
module1.py
module2.py

We can import modules from a package using:

from my_package import module1

'''

# def decorate(func):
#     def wrapper(a,b):
#         print("The addition to your numbers are: ")
#         func(a,b)
#         print("Thank you.")
#     return wrapper


# @decorate
# def addition(a,b):
#     print(f"your total is {a+b}")

# addition(12,65)

'''
*args is basically used to accept multiple arguments without initializing a variable for each one every time.
full form of args is arguments.
can use any variable in place of args
'''
# def addition(*args):
#     sum = 0
#     for i in args:
#         sum += i

#     print(sum)

# addition(34,23,23,45,67,89,76)

'''
**kwargs full form is keyword arguments.
basically accepting keywords and arguments in a dictionary.
kargs always contain **, the variable name can be changed.
'''

# def information(**kwargs):
#     for i in kwargs:
#         print(f"{i}:{kwargs[i]}")

# print("Your information is: ")
# information(name = "richeek", age = 22, designation = "AI/ML")

# DECORATORS USING *args & **kwargs

# def decorate(func):
#     def wrapper(*args, **kwargs):
#         print("The addition to your numbers are: ")
#         func(*args, **kwargs)
#         print("Thank you.")
#     return wrapper

# @decorate
# def addition(a,b,c,d):
#     print(f"your total is {a+b+c+d} ")

# addition(12,65,56,67)

'''
Comprehensions -> It is used to create List, dictionary and sets but we dont use multiple lines of codes for 
loops and if-else statement.
'''

# Eg: Taking elements in a LIST.

#NORMAL WAY
# a = []
# for i in range(1,21):
#     if i%2 == 0:
#         a.append(i)

# print(a)

#USING COMPREHENSION

# a = [i for i in range(1,21) if i%2==0]

# print(a)

#DICTIONARIES

# a = {i : i**2 for i in range(1,10)}
# print (a)

#SETS

# a = {i*i for i in range(10) if i%2==0}
# print (a)

'''
Lambda function: A lambda function is an anonymous inline function defined using the lambda keyword. 
It's often used for short, simple functions that are only used only once or temporarily. 
You can have multiple arguments, but there will only be one expression.
'''

# Using function
# def addition(a,b):
#     print(a+b)

# addition(12,13)
# print(addition)

# Using Lambda

# addition = lambda a,b : a+b
# addition = lambda a: "even" if a%2 == 0 else "odd"

# print(addition(12))

'''
MAP()

The map() function is used to apply a function to every item in an iterable.

FILTER()

The filter() function is used to filter elements from an iterable based on a condition.

'''

# MAP

#  result = map(lambda function: variable of list)

# a = [1,2,3,4,5]
# result = map(lambda x : x*2,a)

# print(list(result))

# FILTER

# def even(x):
#     if x%2 ==0:
#         return True
#     else:
#         return False
    
# a =[1,2,3,4,5,6]

# result = filter(even, a )
# print(list(result))

# a =[1,2,3,4,5,6]

# result = filter(lambda x : True if x%2==0 else False, a )
# print(list(result))

'''
MODULES AND PACKAGES

MODULES

A module is a Python file containing Python code such as functions, classes, and variables.

Modules help us organise code into separate files and make the code reusable.

A module can be imported using the import keyword.

Example:

import math

print(math.sqrt(25))

PACKAGES

A package is a collection of modules organised in a directory.

Packages help in organising large Python projects into smaller and manageable parts.

A package generally contains an **init**.py file.

Example structure:

my_package/
**init**.py
module1.py
module2.py

We can import modules from a package using:

from my_package import module1

A module is a file that can be accessed by import keyword.. 
A packages is a folder containing multiple files of module.
'''

