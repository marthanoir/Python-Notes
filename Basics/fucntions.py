# def sum(a,b):   #a and b are positional arguments
#     result = a+b
#     return result

# a = int(input("Enter first number: "))
# b = int(input("Enter second number: "))
# result1= sum(a,b)
# print(f"the sum of the two numbers is {result1}")



# def hello(age, name):   #a and b are positional arguments
#     print(f"My name is {name} and age is {age}")


# def sum(a,b=45):   #b is default paramenter
#     result = a+b
#     return result

# a = int(input("Enter first number: "))
# result1= sum(a)
# print(f"the sum of the two numbers is {result1}")

def palindrome(str):
    rev = ""
    for i in range(len(str)-1,-1,-1):
        rev = rev +str[i]

    if rev == str:
        print("It is a palindrome")
    else:
        print("Not palindrome")

palindrome("madam")