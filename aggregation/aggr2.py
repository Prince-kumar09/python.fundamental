#aggregation without class
class Student:
    def __init__(self, name):
        self.name = name


s1 = Student("Aman")

print(s1.name)

#another example of aggregation

class Student:
    def __init__(self, name):
        self.name = name


class School:
    def __init__(self, student):
        self.student = student

    def show_student(self):
        print("Student name:", self.student.name)


s1 = Student("Aman")

school1 = School(s1)

school1.show_student()


