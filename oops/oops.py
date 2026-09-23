class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
student1=Student("prince",21)
print(student1.name)
print(student1.age)


class Employee:
    def __init__(self,name,salary,department):
        self.name=name
        self.salary=salary
        self.department=department
employee1=Employee("prince",50000,"ai/ml")
print(employee1.name)
print(employee1.salary)
print(employee1.department)        



class Student:
    def __init__(self,name,age,branch):
        self.name=name
        self.age=age
        self.branch=branch
student1=Student("prince",21,"ai/ml")
student2=Student("rahul",20,"cse")
print(student1.name)
print(student1.age)
print(student1.branch)
print(student2.name)
print(student2.age)
print(student2.branch)



class mobile:
    def __init__(self,brand,model,price):
        self.brand=brand
        self.model=model
        self.price=price
mobile1=mobile("samsung","s24",70000)
mobile2=mobile("apple","iphone16",80000)
print(mobile1.brand)
print(mobile1.model)
print(mobile1.price)
print(mobile2.brand)
print(mobile2.model)
print(mobile2.price)

    