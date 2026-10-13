
class Student:
    def __init__(self, marks):
        self.marks = marks

    def __eq__(self, other):
        return self.marks == other.marks

s1 = Student(80)
s2 = Student(80)
s3 = Student(90)

print(s1 == s2)
print(s1 == s3)






class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def __eq__(self, other):
        return self.marks == other.marks

s1 = Student("Prince", 80)
s2 = Student("Rahul", 80)
s3 = Student("Aman", 90)

print(s1 == s2)
print(s1 == s3)
