students= [
    ["prince",20],
    ["aman",21],
    ["rahul",19]
]
print(students[1][0])
print(students[2][1])

#task3
numbers=[
    [10,20,30],
    [40,50,60],
    [70,80,90]
]
print(numbers[1][2])
print(numbers[2][0])
# how to modify nested list 

students= [
    ["prince",20],
    ["aman",21],
    ["rahul",19]
]
students[1][1]=22
print(students)
students.append(["rahul",19])
print(students)

# print all the value in different row
numbers = [
    [10, 20],
    [30, 40],
    [50, 60]
]
for x in numbers:
    for y in x:
        print(y)

#print sum of all the element or numbers
numbers = [
    [10, 20],
    [30, 40],
    [50, 60]
]
total=0
for x in numbers:
    for y in x:
        total=total+y
print(total)

# print even number of the given list

numbers = [
    [10, 20],
    [30, 40],
    [50, 60]
]

for x in numbers:
    for y in x:
        if y%2==0:
            print(y)
