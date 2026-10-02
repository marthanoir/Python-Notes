from pathlib import Path
import os

def readfileandfolder():
    path = Path('')
    items = list(path.rglob('*'))
    for i, items in enumerate(items):
        print(f"{i+1} : {items}")

def createafile():
    try:
        readfileandfolder()
        name = input("Enter your file name: ")
        p = Path(name)
        if not p.exists():
            with open(p, 'w') as fs:
                data = input("What do you want to write? \n")
                fs.write(data)
            print("FILE CREATED SUCCESSFULLY. ")
        else:
            print("File already exists")

    except Exception as err:
        print(f"An error occured as {err}")

def readfile():
    try:
        readfileandfolder()
        name = input("Enter the file name you want to read: ")
        p = Path(name)
        if p.exists() and p.is_file():
            with open(p,'r') as fs:
                data = fs.read()
                print(data)
            print("Readed Successfully.")
    except Exception as err:
        print(f"An exception occurred as {err}")

def updatefile():
    try:
        readfileandfolder()
        name = input("Which file do you want to update: ")
        p = Path(name)
        if p.exists() and p.is_file():
            print("Write 1 for name change")
            print("Write 2 for overwriting data")
            print("Write 3 for appending your data")

            res = int(input("Enter your choice: "))
            if res == 1:
                name2 = input("Enter new file name: ")
                p2 = Path(name2)
                p.rename(p2)

            if res == 2:
                with open(p, 'w') as fs:
                    data = input("Enter what you want to write: ")
                    fs.write(data)

            if res == 3:
                with open(p,'a') as fs:
                    data = input("Enter what you want to append: ")
                    fs.append(" "+name2)

    except Exception as err:
        print(f"An error occured as {err}. ")

def deletefile():
    try:
        readfileandfolder()
        name = input("Select the file you want to delete: ")
        p = Path(name)
        if p.exists() and p.is_file():
            os.remove(p)
            print("File removed successfully.")
        else:
            print("File doesn't exist.")
    except Exception as err:
        print(f"An error occured as {err}")


print("1. Select 1 for Creating a New File.")
print("2. Select 2 for Reading a File.")
print("3. Select 3 for Updating a File.")
print("4. Select 4 for Deletion of a File.")

check = int(input("Choose your input: "))

if check == 1:
    createafile()

if check == 2:
    readfile()

if check == 3:
    updatefile()

if check == 4:
    deletefile()