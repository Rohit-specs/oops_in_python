from abc import ABC,abstractmethod

class paymentmethod(ABC):
    @abstractmethod
    def pay(self,amount):
        pass
    
class invoice(ABC):
    @abstractmethod
    def invoice(self,amount,purchase,quantity):
        pass
    
class CreditCard(paymentmethod,invoice):
    def pay(self, amount):
        print(f"Paid {amount} by using Credit Card")
    def invoice(self,purchase,amount,quantity):
        print("\n-------invoice-------")
        print(f"Product  = {purchase}")
        print(f"quantity = {quantity}")
        print(f"amount   = {amount*quantity}")
    
class gpay(paymentmethod,invoice):
    def pay(self, amount):
        print(f"Paid {amount} by using Gpay")
    def invoice(self,purchase,amount,quantity):
        print("\n-------invoice-------")
        print(f"Product  = {purchase}")
        print(f"quantity = {quantity}")
        print(f"amount   = {amount*quantity}")
    
class phonepay(paymentmethod,invoice):
    def pay(self, amount):
        print(f"Paid {amount} by using phonepay")
    def invoice(self,purchase,amount,quantity):
        print("\n-------invoice-------")
        print(f"Product  = {purchase}")
        print(f"quantity = {quantity}")
        print(f"amount   = {amount*quantity}")
        
class debitCard(paymentmethod,invoice):
    def pay(self, amount):
        print(f"Paid {amount} by using Debit Card")
    def invoice(self,purchase,amount,quantity):
        print("\n-------invoice-------")
        print(f"Product  = {purchase}")
        print(f"quantity = {quantity}")
        print(f"amount   = {amount*quantity}")
    
cc = CreditCard()
g = gpay()

cc.pay(100)  
cc.invoice("Bag",1200,5)

# g.pay(200)
