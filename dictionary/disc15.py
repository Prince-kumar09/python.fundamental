student = {
    "name": "Prince",
    "marks": 90
}

print(student.get("city", "Not Available"))

student.setdefault("city", "Lucknow")

print(student)