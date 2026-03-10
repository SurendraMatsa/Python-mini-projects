import json, os , random, time

database = "database.json"

def LoadData():
    if os.path.exists(database):
        with open(database, "r") as file:
            return json.load(file)
    else:
        return {}
    
def save_data(data):
    with open(database, "w") as file:
        json.dump(data, file, indent=4)

class Account:
    
    def __init__(self):
        self.data = LoadData()
    
    def deposit(self, acc_no,amount):
        if amount > 0:
            self.data[acc_no]['balance'] += amount
            self.data[acc_no]['transactions'].append(f"Deposited : {amount}")
            save_data(self.data)
            print(f"You current balance is : {self.data[acc_no]['balance']}")
            print("Deposited Successfully")
        else:
            print("Invalid amount")

    def withdraw(self,acc_no, amount):
        if self.data[acc_no]['balance'] >= amount and amount > 0:

            self.data[acc_no]['balance'] -= amount
            self.data[acc_no]['transactions'].append(f"Withdrawn : {amount}")
            save_data(self.data)
            print(f"You current balance is : {self.data[acc_no]['balance']}")
            print("Withdrawal Completed Collect Your Cash\n")

        else:
            
            print("Insufficient Funds or Invalid amount\n")

    def checkBalance(self,acc_no):
        print(f"Your account Balance is : {self.data[acc_no]['balance']} ")

    def showTransactions(self,acc_no):
        if not self.data[acc_no]['transactions']:
            print("No transactions yet")
        else:
            print("-------------- Transactions History --------------")
            
            for transacation in self.data[acc_no]['transactions']:
                print(transacation)

    def changepin(self, acc_no, oldPIN,  newpin):
        if oldPIN == self.data[acc_no]['pin']:
            self.data[acc_no]['pin'] = newpin
            save_data(self.data)
            print("PIN changed successfully")
        else:
            print("Something Went Wrong")

    def HomePage(self,acc_no):
        
        print("--------------- Main Menu ---------------")
        print(f"Hello Mr/Mrs {self.data[acc_no]['name']}, Welcome Come To MSB Bank")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Show Transactions")
        print("5. Change Pin")
        print("6. Exit")
        Result = int(input("Choose Your Option : "))
        return Result

class Atm:

    def __init__(self):
        self.data = LoadData()

    def login(self):
        
        self.data = LoadData()

        Useracc = input("Enter Your Account No : ")
        if Useracc not in self.data:
            print("Account not found. Please create a new account.")
            return
        if self.data[Useracc]['status'] == "blocked":
            print("Your account is blocked. Contact bank.")
            return
        
        attempts = self.data[Useracc]['attempts']
        while attempts > 0:
            Userpin = int(input("Enter Your PIN No : "))
            
            if Useracc in self.data and Userpin == self.data[Useracc]['pin'] and self.data[Useracc]['status'] == "Active":
                Act.data = LoadData()
                self.data[Useracc]['attempts'] = 3
                save_data(self.data)

                while True:
                    result = Act.HomePage(Useracc)
                    if result == 1:
                        amount = float(input("Enter Your Deposit amount : "))
                        Act.deposit(Useracc,amount)
                    elif result == 2:
                        amount = float(input("Enter Your Withdrawal amount : "))
                        Act.withdraw(Useracc,amount)
                    elif result == 3:
                        Act.checkBalance(Useracc)
                    elif result == 4:
                        Act.showTransactions(Useracc)
                    elif result == 5:
                        oldpin = int(input("Enter Your Old PIN : "))
                        newpin = int(input("Enter Your Pin : "))
                        Act.changepin(Useracc,oldpin,newpin)
                        break
                    elif result == 6:
                        print("Session Ended. Your Account Logged Out.\n")
                        print("----------- Visit again, Thank You -----------")
                        break
                    else:
                        print("Invalid Option, Try Again...")


            elif Useracc in self.data and Userpin != self.data[Useracc]['pin']:
                attempts -=1
                self.data[Useracc]['attempts'] = attempts
                save_data(self.data)
                print(f"Wrong PIN. attempts left {attempts}")

            if attempts == 0:
                self.data[Useracc]['status'] = "blocked"
                save_data(self.data)
                print("To many attempts. Card Blocked Temporary. Contact Bank Manager. ")
                break
            
                
    def create_account(self):
        self.data = LoadData()
        name = str(input("Enter Your Name : "))
        surname = str(input("Enter Your surname : "))
        full_name = (name +" "+ surname).title()
        acc_no = str(random.randint(100000000,999999999))
        mobile = int(input("Enter Your Mobile NO : "))
        pin = int(input("Set Your PIN NO : "))
        self.data[acc_no] = {
            "name": full_name,
            "pin": pin,
            "balance": 0.0,
            "mobile": mobile,
            "transactions": [],
            "status": "Active",
            "attempts": 3
            }
        save_data(self.data)
        print("Account Created Successfully....\n")
        print(f"Hi, {full_name} your account No : {acc_no}")
        print(f"Your account PIN  : {pin}")
        self.login()

acc = Atm()
Act = Account()
while True:
    print("----------- Welcome To MSB Bank -----------")
    print("1. Login")
    print("2. Create Account")
    Status = int(input("Choose Your Option : "))
    
    if Status == 1:
        print("------------------ Login ------------------")
        acc.login()
        
    elif Status == 2:
        print("------------------ Create Account ------------------")
        acc.create_account()
    else:
        print("Choose Correct Option")
