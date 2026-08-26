#zip() do ya multiple lists ke corresponding elements ko pair karta hai.
names = ["Prince", "Aman", "Rahul"]
marks = [90, 85, 80]

result = zip(names, marks)

print(list(result))

#zip() + for loop
names = ["Prince", "Aman", "Rahul"]
marks = [90, 85, 80]

for name, mark in zip(names, marks):
    print(name, mark)



names = ["Prince", "Aman", "Rahul"]
marks = [90, 85, 80]
cities = ["Gorakhpur", "Lucknow", "Delhi"]

for name, mark, city in zip(names, marks, cities):
    print(name, mark, city)


names = ["Prince", "Aman", "Rahul"]
marks = [90, 85]

print(list(zip(names, marks)))
'''result = zip(names, marks)

print(result)
toh output kuch aisa ho sakta hai:

<zip object ...>
Kyunki zip() ek zip object return karta hai.
   '''


a = [1, 2, 3]
b = [10, 20, 30]

for x, y in zip(a, b):
    print(x + y)

names = ["Prince", "Aman", "Rahul"]
age = [20, 21, 19]

for name, age in zip(names, age):
    print(name, age)
#print(list(zip(names, age))) recall the concept 


        