#Parameters & Arguments

#addition
def add(number1,number2):
    print(number1+number2)

add(20,10)

#multiplication

def multiply(number1,number2):
    print(number1*number2)

multiply(6,7)

#price and all 

def calculate_total(price,quantity):
    print("total",price*quantity)
calculate_total(50,4)

#multiple parameters plus calculation
def student_result(name,marks1,marks2):
    print("name:",name)
    marks=marks1+marks2
    print("total:",marks)
    if marks>=80:
        print("good")
    else:
        print("need improvement")
student_result("prince",45,40)

#same function multiple calls
def student_result(name, marks1, marks2):
    marks = marks1 + marks2

    print("name:", name)
    print("total:", marks)

    if marks >= 80:
        print("good")
    else:
        print("need improvement")

student_result("prince", 45, 40)
student_result("aman", 30, 35)
student_result("rahul", 50, 45)