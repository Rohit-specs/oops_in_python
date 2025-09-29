from abc import ABC,abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        print("This will print area of different shapes")
class Rectangle(Shape):
    def area(self,l,b):
        print("Area of Rectangle: ",l*b)
class Circle(Shape):
    def area(self,r):
        print("Area of circle: ",(22/7)*r**2)

obj=Rectangle()
obj.area(8,5)

print()

obj1=Circle()
obj1.area(7)