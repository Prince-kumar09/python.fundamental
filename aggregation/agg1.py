class Student:
    def __init__(self, name):
        self.name = name


class School:
    def __init__(self, student):
        self.student = student

    def show_student(self):
        print("Student name:", self.student.name)


# Pehle Student object banaya
t1 = Student("Aman")

# Existing Student object School ko pass kiya
d1 = School(t1)

# School ke through student ka naam print kiya
d1.show_student()