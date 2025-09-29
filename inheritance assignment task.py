class Vehicle:
    def __init__(self,make,model,year):
        self.make=make
        self.model=model
        self.year=year
    def display_info(self):
        print("Make:",self.make)
        print("Model:",self.model)
        print("Year:",self.year)
class Car(Vehicle):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
    def display_info(self):
        super().display_info()
class Motorcycle(Vehicle):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
    def display_info(self):
        super().display_info()

obj=Car("Toyota","don't know about models",2022)
obj.display_info()
print()
obj=Motorcycle("Splender","What are models? this is from future ",2066)
obj.display_info()



    
