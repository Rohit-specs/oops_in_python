class vehicle:
    def type(self,vehicletype):
        self.vehicletype=vehicletype
        print(f"Vehicle Type: {vehicletype}")
        
    def company(self,carcompany):
        print(f"{self.vehicletype} company is: {carcompany}")
        
    def modelyear(self,modelyear):
        print(f"{self.vehicletype} Model year is: {modelyear}")
    
class viewvehicledetails(vehicle):
    def cardetails(self):
        cartype=input("Enter your car type (car/bike/etc): ")
        carcompany=input(f"Enter your {cartype} company name: ")
        modelyear=int(input(f"Enter your {cartype} model year: "))
        self.type(cartype)
        self.company(carcompany)
        self.modelyear(modelyear)
    
class fare:
    def __init__(self):
        self.basefare=25
        self.costperkm=11
        self.costpermin=1.5
        self.tripdistance=0
        self.triptime=0

class faredetails(fare):
    def estimatedfare(self,tripdistance,triptime):
        self.tripdistance=tripdistance
        self.triptime=triptime
        self.estimatedfare=self.basefare+(self.costperkm*self.tripdistance)+(self.costpermin*self.triptime)
    def faredetails(self,tripdistance,triptime):
        
        print("Base Fare: ",self.basefare)
        print("Per kilometer Cost : ",self.costperkm)
        print("Per min Cost: ",self.costpermin)
        print("Distance travelled: ",self.tripdistance)
        print("Time travelled: ",self.triptime)
        print("Estimated fare = Base fare+(Cost Per Km X Trip Distance)+(Cost Per Min X Trip Time)")
        print(f"Estimated fare = {self.basefare} + ({self.costperkm} x {tripdistance}) + ({self.costpermin} x {triptime})")
        
obj= viewvehicledetails()
obj.cardetails()