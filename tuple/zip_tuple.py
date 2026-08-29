#** generally Dictionary ko unpack karta hai.
def student(name, age):
    print(name, age)

data = {
    "name": "Prince",
    "age": 20
}

student(**data)