'''
EXCEPTION HANDLING

Types of exceptions we can't handle:
1. Syntax Error
2. Indentation Error
3. Tab Error

There are exceptions we can handle, for eg:

a = 10/a where input a is 0 
gives ZeroException Error

Exception Handling

Keyword	Purpose
try ->	Wrap the block of code that might cause an exception.
except	-> Handle the exception if it occurs
else	-> Run code only if no exception occurs
finally ->	Run code no matter what, whether there's an exception or not
raise ->	Manually throw an exception
'''

# a = int(input("Enter your number: "))

# try:
#     b = 10/a
#     print(b)
# # except ZeroDivisionError:  #Specific Exception
# #     print("Can't divide by zero.")

# except Exception as err:  #Can accept any error
#     print(f"Sorry there is an {err} error.")

# else:       #Wont be called if except is called.
#     print("No errors found.")

# finally:        #always runs no matter what
#     print("I will be always present.")

# print("Division done.")

'''
USECASE OF raise
'''

# age = int(input("Enter your age: "))

# try:
#     if age<10 or age>18:
#         raise ValueError ("Your age doesnt fit the required criteria. ")
#     else:
#         print("Welcome to the club.")

# except Exception as err:
#     print(f"Invalid input for {err}.")

# print("We gonna be rolling soon.")

