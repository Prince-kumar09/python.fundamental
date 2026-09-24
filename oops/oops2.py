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





class Employee:

    company = "Google"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
employee1 = Employee("Prince", 50000)
employee2 = Employee("Rahul", 60000)
print(employee1.name)
print(employee1.salary)
print(employee2.name)
print(employee2.salary)



class Student:

    college = "ITM"

    def __init__(self, name):
        self.name = name


student1 = Student("Prince")
student2 = Student("Rahul")

Student.college = "ABC"

print(student1.college)
print(student2.college)