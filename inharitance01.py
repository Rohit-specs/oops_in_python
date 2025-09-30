
class Course:
    def show_course(self):
        print("Course:", self.course_name)


class BTech(Course):
    def __init__(self, student_name):
        course_name="btech"
        self.student_name = student_name
        self.course_name = course_name

    def register(self):
        print(self.student_name, "has registered for BTech in", self.course_name)

class BSc(Course):
    def __init__(self, student_name):
        course_name="Bsc"
        self.student_name = student_name
        self.course_name = course_name

    def register(self):
        print(self.student_name, "has registered for BSc in", self.course_name)

class BCA(Course):
    def __init__(self, student_name):
        course_name="BCA"
        self.student_name = student_name
        self.course_name = course_name

    def register(self):
        print(self.student_name, "has registered for BCA in", self.course_name)

class BA(Course):
    def __init__(self, student_name):
        course_name="BA"
        self.student_name = student_name
        self.course_name = course_name

    def register(self):
        print(self.student_name, "has registered for BA in", self.course_name)

student1 = BTech("Ravi")
student2 = BSc("Meena")
student3 = BCA("Aman")
student4 = BA("Sara")

student1.register()
student1.show_course()

print()

student2.register()
student2.show_course()

print()
student3.register()
student3.show_course()

print()

student4.register()
student4.show_course()