#creation of sim[ple application

class BankAccount:
    def __init__(self,initialAmt,accHolder):
        self.balance=initialAmt
        self.name=accHolder
        print("account is created")
        print(f"Account created for '{self.name}' with balance{self.balance}.2f")
        
