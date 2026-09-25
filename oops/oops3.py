class Student:
    school="abc school"
    def __init__(self,name,age):
        self.name=name
        self.age=age
student1=Student("prince",21)
student2=Student("rahul",20)

print(student1.name)
print(student1.age)
print(student1.school)



print(student2.name)
print(student2.age)
print(student2.school)