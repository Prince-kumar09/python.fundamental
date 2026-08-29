def add(a, b):
    return a + b

numbers = (10, 20)

result = add(*numbers)

print(result)


#tuple unpacke

def multiply(a, b):
    return a * b

numbers = (5, 4)

print(multiply(*numbers))