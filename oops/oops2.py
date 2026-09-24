class Student:

    college = "ITM"

    def __init__(self, name, age):
        self.name = name
        self.age = age


student1 = Student("Prince", 21)
student2 = Student("Rahul", 20)

print(student1.name)
print(student1.age)
print(student1.college)

print(student2.name)
print(student2.age)
print(student2.college)