#creation of sim[ple application

class BankAccount:
    def __init__(self,initialAmt,accHolder):
        self.balance=initialAmt
        self.name=accHolder
        print("account is created")
        print(f"Account created for '{self.name}' with balance{self.balance:.2f}")
        
    def getData(self):
        print(f"Account '{self.name}' has balance {self.balance:.2f}")

    def deposite(self,amount):
        self.balance=self.balance+amount
        print(f"the amount deposited succesfully")
       
        print("thank you")

    def Withdraw(self,Withdraw_Amt):
        self.balance=self.balance-Withdraw_Amt
        print(f"the Amount Withdrawed succesfully")
        self.getData()
