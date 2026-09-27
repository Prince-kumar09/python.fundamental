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



class employee:
    company="google"
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
employee1=employee("prince",50000)
employee2=employee("rahul",60000)
employee1.company="microsoft"
print(employee1.name)
print(employee1.salary)
print(employee1.company)
print(employee2.name)
print(employee2.salary)
print(employee2.company)