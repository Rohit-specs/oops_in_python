class Loan:
    def __init__(self):
        self.__income=int
        self.__loanamount=int
        self.__creditscore=int
        self.__workexperience=int
    def validincome(self):
        self.__income=int(input("Please enter your monthly income: "))
        return self.__income
    
    def validloanamount(self):
        self.__loanamount=int(input("Please enter your loan amount: "))
        return self.__loanamount
    
    def validcreditscore(self):
        self.__creditscore=int(input("Please enter your Credit score: "))
        return self.__creditscore

    def validworkexperience(self):
        self.__workexperience=int(input("Please enter your Work experience: "))
        return self.__workexperience
    def updateloanamount(self):
        self.__loanamount=int(input("enter laon amount: "))
        
ob=Loan()

if ob.validincome()>=40000 and ob.validloanamount()<=200000:
    if ob.validcreditscore()>=700:
        if ob.validworkexperience()>2:
            print("You are eligible for Loan \nyour loan is approved")
        else:
            print("you work experience is below 2 years")
    else:
        print("your credit score below 700")
else:
    print("you are not eligible for loan")



       