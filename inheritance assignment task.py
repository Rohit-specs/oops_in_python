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
    super().__init(make,model,year)
    display_info(self)



    
