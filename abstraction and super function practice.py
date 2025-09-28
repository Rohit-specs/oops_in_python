from abc import ABC,abstractmethod
class vehicle:
    def type(self,vehicletype):
        self.vehicletype=vehicletype
        print(f"Vehicle Type: {vehicletype}")
        pass
        
    def company(self,carcompany):
        print(f"{self.vehicletype} company is: {carcompany}")
        pass
        
    def modelyear(self,modelyear):
        print(f"{self.vehicletype} Model year is: {modelyear}")
        pass
    
class viewvehicledetails(vehicle):
    def cardetails(self):
        cartype=input("Enter your car type (car/bike/etc): ")
        carcompany=input(f"Enter your {cartype} company name: ")
        modelyear=int(input(f"Enter your {cartype} model year: "))
        self.type(cartype)
        self.company(carcompany)
        self.modelyear(modelyear)
    
class farestructure(ABC):
    @abstractmethod
    def __init__(self):
        self.basefare=25
        self.costperkm=11
        self.costpermin=1.5
        self.tripdistance=0
        self.triptime=0
class faredetails(farestructure):
    def __init__(self,tripdistance,triptime):
        super().__init__()
        self.tripdistance=tripdistance
        self.triptime=triptime
        print("Base Fare: ",self.basefare)
        print("Per kilometer Cost : ",self.costperkm)
        print("Per min Cost: ",self.costpermin)
        print("Distance travelled: ",self.tripdistance)
        print("Time travelled: ",self.triptime)
        print("Estimated fare = Base fare+(Cost Per Km X Trip Distance)+(Cost Per Min X Trip Time)")
        print(f"Estimated fare = {self.basefare} + ({self.costperkm} x {self.tripdistance}) + ({self.costpermin} x {self.triptime})")
class totalfare(farestructure):
    def __init__(self, tripdistance, triptime):
        super().__init__()
        self.tripdistance = tripdistance
        self.triptime = triptime

    def estimatedfare(self):
        print("Total Fare: ",end="")
        return self.basefare + (self.costperkm * self.tripdistance) + (self.costpermin * self.triptime) 


obj=viewvehicledetails()
obj.cardetails()
print()#for spacing
obj=faredetails(2,8)
print()#For proper spacing
obj1=totalfare(2,8)
print(obj1.estimatedfare())

