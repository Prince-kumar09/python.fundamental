#instance methods

class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def introduce(self):
        print("my name is",self.name)
        print("my age is ",self.age)
student1=Student("prince",21)
student1.introduce()


#qwestion based on rectangle

class Rectangle:
    def __init__(self,lenght,width):
        self.length=lenght
        self.width=width
    def area(self):
        return self.length*self.width
r1=Rectangle(10,5)
print(r1.area())



#perimeter of rectangle
class Rectangle:

    def __init__(self, length, width):
        self.length=length
        self.width=width

    def area(self):
        return self.length*self.width

    def perimeter(self):
        return 2 *(self.length+self.width)


r1 = Rectangle(10, 5)
print(r1.area())
print(r1.perimeter())





class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def result(self):
        if self.marks>=40:
            print("pass")
        else:
            print("fail")
student1=Student("prince ",75)
student2=Student("rahul",35)

student1.result()
student2.result()
