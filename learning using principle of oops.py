from abc import ABC,abstractmethod
class Vehicle(ABC):
    @abstractmethod
    def calculate_rent(self,days):
        pass
    @staticmethod
    def vehicle_type():
        return "Generic vehicle"
class Car(Vehicle):
    brand=None
    daily_rate=2500
    def calculate_rent(self,days):
        super().calculate_rent(days)
        print(days,"Days rent of Car is",self.daily_rate*days)
    @staticmethod
    def vehicle_type():
        return "Vehicle type Car"
class Bike(Vehicle):
    brand=None
    daily_rate=1200
    def calculate_rent(self,days):
        super().calculate_rent(days)
        print(days,"Days rent of Bike is",self.daily_rate*days)
    @staticmethod
    def vehicle_type():
        return "Vehicle type Bike"
    
        
obj=Car()
obj.calculate_rent(5)
print(obj.vehicle_type())
print()
obj=Bike()
obj.calculate_rent(4)
print(obj.vehicle_type())
