"""
LISTS:
Mutable, Duplicates, Ordered, Heterogenous: supports multiple data types.

a = [12,13,14,True,"Richeek"]

"""



# a = [12,13,14,True,"Richeek"]

# print(a[0:5])     # LIST INDEXING AND SLICING
# print(a[0:3])
# print(a[4])
# print(a[-1])

# for i in range(len(a)):   #INDEX ACCESS
#     print(a[i])

# for i in a:     #ELEMENT ACCESS
#     print(i)

# 
# help(list)
'''
append(self, object, /)
 |      Append object to the end of the list.

insert(self, index, object, /)
 |      Insert object before index.

remove(self, value, /)
 |      Remove first occurrence of value.

 extend(self, iterable, /)
 |      Extend list by appending elements from the iterable.
'''

# a = [12,13,14]
# a.append(6)
# a.insert(2,5)
# print(a)


#PRACTICE

#find positive and negative elements from list

# n= int(input("Enter the number of elements you want to enter: "))
# a= []
# for i in range(n):
#     num= int(input(f"enter number {i+1}: "))
#     a.append(num)

# print("POSTIVE NUMBERS")
# for i in range(len(a)):
#     if (a[i]>0):
#         print(a[i])

# print("NEGATIVE NUMBERS")
# for i in range(len(a)):
#     if (a[i]<0):
#         print(a[i])

# mean = 0
# for i in range(len(a)):
#     mean += a[i]
# mean = mean/n
# print(f"mean is {mean}") 

# lar = 0
# index = 0
# for i in range(n):
#     if (lar<a[i]):
#         lar = a[i]
#         index = i
# print(f"Largest element is {lar} and index is {index+1}")


# lar = 0
# secondgrt = 0
# index = 0
# for i in a:
#     if (lar<i):
#         secondgrt = lar
#         lar = i
#     elif i>secondgrt:
#         secondgrt = i
# print(f"Second Largest element is {secondgrt}.")

# SORTING CHECKER
# counter = 0
# for i in range(len(a)):
#     first = a[i]
#     for j in range(i+1,len(a)):
#         if (first>a[j]):
#             counter += 1
#             break

# if (counter==0):
#     print("Sorted.")
# else:
#     print("Not Sorted.")
    
        

'''
TUPLES

Immutable, Duplicates, Ordered, Heterogeneous

a = (1,2,3,4,5)
 
Tuple has two main methods

one for index finding
index = t.index(value)

second for occurence counts
count = t.count(value)
'''

# a = (1,2,3,4,5,5,5,5,55)

# print(a.index(55))
# print(a.count(5))

# a,b,c,d = (1,2,3,4)

# print(a)
# print(b)
# print(c)
# print(d)

'''
SETS

mutable: by using methods as there are no index values.
no duplicates, 
unordered (cant access through index values): uses hash value to store data
HASH VALUE CHANGES EVERY SINGLE TIME CODE IS RUN.
Since hashing doesnt have any order, hence sets are also unordered.
heterogeneous: semi heterogeneous, cant store everything

s = {} -> dictionary
s = {1,2,3,4,5} -> set

can't use loops using indexes as sets doesnt have indexes but we can use loops
where we are directly accessing the elements of a set.

the auto sorting happens in sets because of the random hash value generation
but if a string is being inserted in a set, then the place of the string in the
printed will be given randomly when it will be generated.

METHODS
s = {1,2,3}
s.add()
s.remove() #raises error if not found
s.discard() #doesnt raise any error if not found
s.clear() #removes all elements
popped_element = s.pop() #removes random element


'''

# s = {1,2,3,4,5,5,5}
# print(s)

# b = hash("hello")
# print(b)

# c = hash((1,2,3,4,5,6))
# print(c)

# a = {1,2,8,"hi",9,3,4,5}

# for i in a:
#     print(i)

# s = {1,2,3}
# s.add()
# s.remove() #raises error if not found
# s.discard() #doesnt raise any error if not found
# s.clear() #removes all elements
# popped_element = s.pop() #removes random element

# a = {1,2,3,4,5}
# b = {4,5,6,7,8}

# union = a.union(b)
# intersection = a.intersection(b)
# difference = a.difference(b)
# symmetric_diff = a.symmetric_difference(b)
# s = a|b #union
# r = a&b #intersection
# p = b-a #difference
# q = b^a #symmetric difference
# b -=a #compound operation
# print(union)
# print(intersection)
# print(difference)
# print(symmetric_diff)
# print (s)
# print(r)
# print(p)
# print(b)

'''
DICTIONARY

Dictionary is hash mapping.
Mutable: Keys not mutable, values can be.
Duplicates: keys must be unique, values can be duplicate,
Order: follows insertion order
heterogeneous.

dict = {1,2,3,4,5}  -> Set
dict = {1:"Hello, 2:45}     -> Dictionary
'''

# dict = {1:"Hello", 2:45, 3:60} 
# print(dict)
# print(dict[3])

# dict[2] = 400       #updating
# print(dict[2])

# dict.update({4:500})    #creating
# dict[5]= 600
# print(dict)

# del dict[3]     #deleting
# print(dict)

# for i in dict:  #accessing keys
#     print(i)

# for i in dict.values():     #accessing values of keys
#     print(i)

# help(dict)
'''
METHODS

__sizeof__(...)
 |      D.__sizeof__() -> size of D in memory, in bytes
 |
 |  clear(...)
 |      D.clear() -> None.  Remove all items from D.
 |
 |  copy(...)
 |      D.copy() -> a shallow copy of D
 get(self, key, default=None, /)
 |      Return the value for key if key is in the dictionary, else default.
 |
 |  items(...)
 |      D.items() -> a set-like object providing a view on D's items
 |
 |  keys(...)
 |      D.keys() -> a set-like object providing a view on D's keys
 |  pop(...)
 |      D.pop(k[,d]) -> v, remove specified key and return the corresponding value.
 |
 |      If the key is not found, return the default if given; otherwise,
 |      raise a KeyError.
 |
 |  popitem(self, /)
 |      Remove and return a (key, value) pair as a 2-tuple.
 |
 |      Pairs are returned in LIFO (last-in, first-out) order.
 |      Raises KeyError if the dict is empty.

'''

'''
 DEEP COPY IN DICT
 Changes made in a copied version automically changes values in original version
'''

# a = [1,2,3,4,5]
# b = a
# b[1] = 100
# print(a)
# print(b)

'''
 SHALLOW COPY IN DICT
 Changes made in a copied version does not automically changes values in original version
'''

# a = [1,2,3,4,5]
# b = a.copy()
# b[1] = 100
# print(a)
# print(b)

# dict = {1:"Hello", 2:45, 3:60} 
# print(dict.items())    #gives key value pair 

# MERGING DICTIONARIES
# d1 = {10:100, 20:200, 30:300}
# d2 = {40:400, 50:500, 60:600}

# for i in d2:
#     d1[i] = d2[i]

# print(d1)

# n = int(input("Enter the number of keys: "))
# d1 = {}
# for i in range (n):
#     key = int(input(f"Enter the value of key {i+1} for d1: "))
#     value = int(input(f"Enter the value of {key}:"))

#     d1[key] = value

# d2 = {}
# for i in range (n):
#     key = int(input(f"Enter the value of key {i+1} for d2: "))
#     value = int(input(f"Enter the value of {key}:"))

#     d2[key] = value
# print(d1)
# print(d2)

# SUM OF VALUES
# n = int(input("Enter the number of keys: "))
# d1 = {}
# sum = 0
# for i in range (n):
#     key = int(input(f"Enter the value of key {i+1} for d1: "))
#     value = int(input(f"Enter the value of {key}:"))
#     sum += value
#     d1[key] = value

# print(d1)
# print(sum)


# FREEQUENCY CALCULATION

# n = int(input("Enter the number of elements in the list: "))
# a = []
# for i in range(n):
#     item = int(input(f"Enter the value of {i+1}: "))
#     a.append(item)
# print(a)
# d1 = {}
# for i in a:
#     if i in d1.keys():
#         d1[i] += 1
#     else:
#         d1[i] = 1
# print(d1)

# SUM OF VALUES BASED ON KEYS

n = int(input("Enter the number of keys: "))
d1 = {}
for i in range (n):
    key = int(input(f"Enter the value of key {i+1} for d1: "))
    value = int(input(f"Enter the value of {key}:"))

    d1[key] = value

d2 = {}
for i in range (n):
    key = int(input(f"Enter the value of key {i+1} for d2: "))
    value = int(input(f"Enter the value of {key}:"))

    d2[key] = value
print(d1)
print(d2)

for i in d2:
    if i in d1:
        d1[i] += d2[i]
    else:
        d1[i] = d2[i]

print(d1)