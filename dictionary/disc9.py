student = {
    "name": "Prince",
    "age": 20
}

value1 = student.get("marks", 90)

print("Using get():", value1)
print("After get():", student)

value2 = student.setdefault("marks", 90)

print("Using setdefault():", value2)
print("After setdefault():", student)