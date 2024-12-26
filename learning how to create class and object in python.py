

class Userinfo:
    def getData(self):
        self.name=input("Enter your Name:")
        self.id=int(input("Enter your id:"))
        self.salary=float(input("Enter your salary:"))

    def display(self):
        print("User Name:",self.name)
        print("User id:",self.id)
        print("User salary:",self.salary)

obj=Userinfo()
obj.getData()
obj.display()
