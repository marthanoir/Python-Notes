# n = int(input("Enter the number: "))
# count = 1
# for i in range (n, (n*10)+1, n):
#     print(f"{n}*{count}={i}")
#     count+= 1

# a = "RICHEEK MITRA MAZUMDAR"
# print(len(a))
# for i in range(len(a)):
#     print(a[i])

#Accept an integer and Print hello world n times

# a = int(input("Enter a number: "))
# fact = 1
# result = 0
# for i in range (a):
#     print("Hello")

# for i in range (1,a+1):
#     print(i)

# for i in range (a,0,-1):
#     print(i)
# for i in range(a):
#     result += i
# print(result)


# for i in range(1,a+1):
#     fact *= i
# print(fact)

#TAKE OUT EVERY NUMBER FROM A GIVEN BIG NUMBER
# a = int(input("Enter the number: "))
# while (a>0):
#     result = a%10
#     a = a//10
#     print(result)

#REVERSE A NUMBER
# a = int(input("Enter the number: "))
# rev = 0
# while (a>0):
#     result = a%10
#     rev = rev*10+ result
#     a = a//10
# print(rev)

#METHOD 1
# import random

# tries = 1
# a = random.randint(1,10)
# print(a)

# num = int(input("enter a number: "))
# if (a == num):
#     print("guess matched")

# else:
#     print("Not matched.")
# while (a!=num):
#     num = int(input("enter a number: "))
#     tries += 1
#     if (a == num):
#         print("guess matched")

#     else:
#         print("Not matched.")

# print(f"No of tries taken is {tries}")

import random

tries = 0
a = random.randint(1,10)
print(a)

while True:
    num = int(input("enter a number: "))
    
    if a == num:
        tries += 1
        print("guess matched")
        break

    elif a>num:
        tries += 1
        print ("Go a little higher")

    elif a<num:
        tries += 1
        print("Go a little lower")

    else:
        tries += 1
        print("Not matched.")

print(f"No of tries taken is {tries}")