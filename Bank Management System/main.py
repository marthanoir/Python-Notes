import json
import random
import string
from pathlib import Path

class Bank:
    database = Path(__file__).parent / 'data.json'
    data = []       #dummy data

    try:
        if Path(database).exists():
            with open(database) as fs:
                data = json.loads(fs.read())

        else:
            print("No such file exists.")

    except Exception as err:
        print(f"An exception occured as {err}.")

    @classmethod
    def __update(cls):
        with open(cls.database, 'w') as fs:
            fs.write(json.dumps(Bank.data))

    @classmethod
    def __accountgenerate(cls):
        alpha = random.choices(string.ascii_letters, k = 4)
        num = random.choices(string.digits, k = 6)
        spchar = random.choices("!@#$%^&*", k = 1)
        id = alpha + num + spchar
        random.shuffle(id)
        return "".join(id)


    def CreateAccount(self):
        info = {
            "Name" : input("Enter your name: "),
            "Age" : int(input("Enter your age: ")),
            "Email" : input("Enter your email: "),
            "PIN" : int(input("Enter your pin: ")),
            "AccountNo.": Bank.__accountgenerate(),
            "Balance" : 0,
        }
        if info['Age']<18 or len(str(info['PIN'])) != 4:
            print("Sorry you cannot create your account. ")

        else:
            print("Account CREATED SUCCESSFULLY")

            for i in info:
                print(f"{i} : {info[i]}")
            print("Please Note Down Your Account Number. ")

            Bank.data.append(info)
            Bank.__update()


    def depositmoney(self):
        accno = input("Enter your account number: ")
        pin = int(input("Enter your pin: "))

        userdata = [i for i in Bank.data if i['AccountNo.']== accno and i['PIN']==pin]

        if userdata == False:
            print("No data found.")

        else:
            amount = int(input("Enter the amount you want to deposit: "))
            if amount>50000 and amount<0:
                print("Deposit invokes rules. Limit: 0 - 50000")
            else:
                userdata[0]['Balance'] += amount
                Bank.__update()
                print("Amount deposited successfully.")

    def withdrawmoney(self):
            accno = input("Enter your account number: ")
            pin = int(input("Enter your pin: "))
    
            userdata = [i for i in Bank.data if i['AccountNo.']== accno and i['PIN']==pin]
    
            if userdata == False:
                print("No data found.")
    
            else:
                amount = int(input("Enter the amount you want to withdraw: "))
                if userdata[0]['Balance']<amount:
                    print("Insufficient Balance.")
                else:
                    userdata[0]['Balance'] -= amount
                    Bank.__update()
                    print("Amount withdrawn successfully.")

    def showdetails(self):
                accno = input("Enter your account number: ")
                pin = int(input("Enter your pin: "))
            
                userdata = [i for i in Bank.data if i['AccountNo.']== accno and i['PIN']==pin]
                print("ACCOUNT DETAILS: \n\n ")
                if userdata == False:
                    print("No data found.")
                
                else:
                    for i in userdata[0]:
                        print(f"{i} : {userdata[0][i]}")

    def updatedetails(self):
        accno = input("Enter your account number: ")
        pin = int(input("Enter your pin: "))
                    
        userdata = [i for i in Bank.data if i['AccountNo.']== accno and i['PIN']==pin]
        print("ACCOUNT DETAILS: \n\n ")
        if userdata == False:
            print("No data found.")
                        
        else:
            print("Can't change details of Age, Account Number and Balance.")
            print("Fill details for change or leave it empty if no change.")

            newdata ={
                "Name" : input("Enter your new name: "),
                "Email" : input("Enter your new email: "),
                "PIN" : input("Enter NEW PIN: ")
            }

            if newdata["Name"] == "":
                newdata["Name"] = userdata[0]["Name"]
            if newdata["Email"] == "":
                newdata["Email"] = userdata[0]["Email"]
            if newdata["PIN"] == "":
                newdata["PIN"] = userdata[0]["PIN"]

            newdata["Age"] = userdata[0]["Age"]
            newdata["AccountNo."] = userdata[0]["AccountNo."]
            newdata["Balance"] = userdata[0]["Balance"]

            if type(newdata["PIN"]) == str:
                newdata["PIN"] = int(newdata["PIN"])

            for i in newdata:
                if newdata[i] == userdata:
                    continue
                else:
                    userdata[0][i] = newdata[i]

            Bank.__update()
            print("DETAILS UPDATED SUCCESSFULLY.")

    def deleteaccount(self):
        accno = input("Enter your account number: ")
        pin = int(input("Enter your pin: "))
                            
        userdata = [i for i in Bank.data if i['AccountNo.']== accno and i['PIN']==pin]
        if userdata == False:
            print("No data found.")
        else:
            check = input("Enter Y for Yes AND N for NO: ")
            if check == 'n' or check == 'N':
                print("NOT DELETED.")

            else:
                index = Bank.data.index(userdata[0])
                Bank.data.pop(index)
                print("ACCOUNT DELETED SUCESSFULLY.")

                Bank.__update()

        



user = Bank()
print("Press 1 for CREATING ACCOUNT")
print("Press 2 for DEPOSITING MONEY IN THE BANK")
print("Press 3 for WITHDRAWING THE MONEY")
print("Press 4 for DETAILS")
print("Press 5 for UPDATING ACCOUNT")
print("Press 6 for DELETING ACCOUNT")

response = int(input("Choose your response: "))

if response == 1:
    user.CreateAccount()

if response == 2:
    user.depositmoney()

if response == 3:
    user.withdrawmoney()

if response == 4:
    user.showdetails()

if response == 5:
    user.updatedetails()

if response == 6:
    user.deleteaccount()