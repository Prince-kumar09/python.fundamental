students = {
    "student1": {
        "name": "Prince",
        "marks": 90
    },
    "student2": {
        "name": "Aman",
        "marks": 75
    },
    "student3": {
        "name": "Rahul",
        "marks": 85
    }
}

for student, data in students.items():
    if data["marks"] >= 80:
        print(data["name"], data["marks"])