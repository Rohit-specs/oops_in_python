class Course:
    def show_course(self):
        print("Course:", self.course_name)


class Student(Course):
    def __init__(self, student_name, course_name):
        self.student_name = student_name
        self.course_name = course_name  

    def register(self):
        print(self.student_name, "has registered for", self.course_name)
        
        
student1 = Student("Mukesh", "Math")
student2 = Student("Ayesha", "Physics")

student1.register()
student1.show_course()

print("")
student2.register()
student2.show_course()