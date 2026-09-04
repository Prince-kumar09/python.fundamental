# Dictionary + List Combination 🔥
names = ["Prince", "Aman", "Rahul"]
marks = [90, 75, 85]

result = {
    name: mark
    for name, mark in zip(names, marks)
    if mark >= 80
}

print(result)

# Dictionary + List + Condition 🧠
names = ["Prince", "Aman", "Rahul", "Ravi"]
marks = [90, 75, 85, 60]

result = {
    name: mark
    for name, mark in zip(names, marks)
    if mark < 80
}

print(result)