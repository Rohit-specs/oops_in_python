class Person:
    name=str
    age=int
    def greet(self,name):
        self.name=name
        # self.age=age
        print("Hello",self.name,"it's good to see you")
obj=Person()
obj.greet("Rohit")
