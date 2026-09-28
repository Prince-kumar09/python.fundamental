class Student:

    school = "ABC School"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print("My name is", self.name)
        print("My age is", self.age)

    @classmethod
    def change_school(cls, new_school):
        cls.school = new_school

student1 = Student("Prince", 21)
student2 = Student("Rahul", 20)
student1.introduce()
Student.change_school("XYZ School")