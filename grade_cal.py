def student_result(name, marks, passing_marks=40):
    print("Student:", name)
    print("Marks:", marks)

    if marks >= passing_marks:
        print("Result: Pass")
    else:
        print("Result: Fail")


student_result("Prince", 75)
student_result("Aman", 35)
student_result("Rahul", 45, 50)