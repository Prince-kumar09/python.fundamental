
class Teacher:
    def __init__(self, name):
        self.name = name

    def teach(self):
        print(self.name, "is teaching")


class Department:
    def __init__(self, teacher):
        # Pehle se bana Teacher object receive karna
        self.teacher = teacher

    def show_teacher(self):
        self.teacher.teach()


# Teacher object independently create hua
t1 = Teacher("Rahul")

# Existing Teacher object Department ko diya
d1 = Department(t1)

d1.show_teacher()

# Teacher object Department ke bina bhi use ho sakta hai
t1.teach()
