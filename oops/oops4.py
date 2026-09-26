class Student:
    school = "ABC School"

    def __init__(self, name):
        self.name = name


student1 = Student("Prince")
student2 = Student("Rahul")

student1.school = "XYZ School"

print(student1.school)
print(student2.school)
print(Student.school)