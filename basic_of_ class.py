class Student:
    def __init__(self):
        print("1. registraion")
        print("2. display record")
        print("3. update student details")
    
    def registration(self):
        self.id=int(input("Please enter student id: "))
        self.name=input("Please enter your name: ")
        self.address=input("Please enter your address: ")
    def displayrecord(self):
        print(f"ID : {self.id} |Name : {self.name} |Address : {self.address}")
        
    def updatestudentdetail(self):
        newid=input("Enter new id: ")
        newname=input("Enter new name: ")
        newaddress=input("Enter new address: ")
        self.id=newid
        self.name=newname
        self.address=newaddress
    def exitprogram(self):
        print("Exit successfully")

while True:
    ob=Student()
    choice=int(input("Enter your choice: "))
    if choice==1:
        ob.registration()
    elif choice ==2:
        ob.displayrecord()
    elif choice==3:
        ob.updatestudentdetail()
    elif choice==4:
        ob.exitprogram()
        break
    else:
        print(f"{choice} is not a valid option")
