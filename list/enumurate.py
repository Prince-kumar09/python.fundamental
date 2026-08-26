'''➡️ enumerate()

Isme hum list ke element ke saath uska index bhi easily nikal sakte hain.'''
'''fruits = ["apple", "mango", "banana"]

for index, fruit in enumerate(fruits):
    print(index, fruit)
    
    o/p 
0 apple
1 mango
2 banana'''
numbers = [10, 20, 30]

for index, value in enumerate(numbers):
    print(index, value)

fruits = ["apple", "mango", "banana"]

for index, fruit in enumerate(fruits, start=1):
    print(index, fruit)    


numbers = [10, 20, 30, 40, 50]

for index, value in enumerate(numbers):
    if value > 25: #enumerate() original index change nahi karta.
        print(index, value)


fruits = ["apple", "mango", "banana", "orange"]

for index, value in enumerate(numbers):
    if fruits=="banana":
        print(index)