students = {
    "Prince": 90,
    "Aman": 75,
    "Rahul": 85,
    "Ravi": 60
}

result = {
    name: "Pass" if marks >= 80 else "Fail"
    for name, marks in students.items()
}

print(result)