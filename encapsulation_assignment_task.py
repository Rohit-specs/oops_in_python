class Bankaccount:
    # name=str
    # __balance=int
    # __password=int
    # __password=int
    def __init__(self,name):
        self.name=name
        self.__balance=10000
        self.__account=123456789
        self.__password=123456
    def deposit(self,deposit):
        while True:
            if deposit>0:
                self.__balance+=deposit
                break
            else:
                print("You have entered amount in (-)ve !")
                deposit=int(input("Please enter amount again: "))

    def withdraw(self,amount,password):
        while True:
            if amount>0 and self.__balance>=amount and password ==self.__password:
                self.__balance-=amount
                break
            elif amount<0:
                print("Entered amount is in negetive")
                amount=int(input("Please enter amount again: "))
                continue
            elif amount>self.__balance:
                print("You have only",self.__balance,"In your bankaccount")
                amount=int(input("Please enter amount less than ",self.balance,":" ))
                continue
            elif password!=self.__password:
                print("Wrong password")
                password=int(input("Please enter password again: "))
    def get_balance(self,password):
        while True:
            if password==self.__password:
                return "Your balance on account",self.__account,"is",self.__balance
            password=int(input("Your entered password is wrong\nPlease enter password again: "))
    def get_account_info(self,account,password):
        while True:
            if password==self.__password and account==self.__account:
                print("Name:",self.name)
                print("Account Number:",self.__account)
                break
            elif password!=self.__password:
                print("Wrong password")
                password=int(input("Please enter password again: "))
                continue
            elif account!=self.__account:
                print("Not A Calid Account Number")
                password=int(input("Please enter Account Number again: "))

obj=Bankaccount("Rohit")
print(obj.get_balance(123456))
obj.deposit(2500)
print(obj.get_balance(123456))
obj.withdraw(5000,123456)
print(obj.get_balance(123456))
obj.get_account_info(123456789,123456)


    


        