class Student:
    name=str
    age=int
    grade=str
    def display_info(self,name,age,grade):
        Student.name=name
        Student.age=age
        Student.grade=grade
        # print(f"Name: {name}\nAge: {age}\nGrade: {grade}")
        # print("Name:",name,"Age:",age,"Grade:",grade)
        print("Name:",Student.name,"Age:",Student.age,"Grade:",Student.grade)

obj=Student()
obj.display_info("Rohit",18,"A")

obj2=Student()
obj2.display_info("Ruchita",18,"B")

    