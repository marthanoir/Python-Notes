'''
FILE HANDLING

File handling allows us to create, read, write, and modify files 
using Python.

Python provides built-in functions and methods to work with files.

Opening a File

The open() function is used to open a file.

file = open("example.txt", "r")

Here:
"example.txt" → name of the file
"r" → mode in which the file is opened

File Modes

r → Read the file
w → Write to the file
a → Append data to the file
x → Create a new file

Reading a File

read() is used to read the contents of a file.

file = open("example.txt", "r")
content = file.read()
print(content)
file.close()

close() is used to close the file after performing the required operation.

Writing to a File

The "w" mode is used to write data to a file.

file = open("example.txt", "w")
file.write("Hello World")
file.close()

If the file already contains data, "w" mode will overwrite the existing content.

Appending to a File

The "a" mode is used to add data at the end of an existing file.

file = open("example.txt", "a")
file.write("This is new data")
file.close()

The existing content is not removed. The new content is added 
at the end.

with Statement

The with statement is used to handle files automatically. It 
automatically closes the file after the block is executed.

with open("example.txt", "r") as file:
content = file.read()
print(content)

This is generally preferred because we don't have to manually 
call close().
'''

#READING A FILE

# p = open('/Users/richeek/Documents/Python/Basics/datastructures.py')
# print(p.read())

#WRITING/CREATING A FILE 

p = open("superman.txt", 'a')

# p.write("Hello this is Richeek and I have just created this file.")
p.write("\nThis line is being appended. ")

p.close()
