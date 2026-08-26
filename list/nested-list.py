#Nested List Comprehension use karke isko flat list mein convert karo.
numbers = [
    [10, 20],
    [30, 40],
    [50, 60]
]
new=[x for row in numbers for x in row ]
print(new)

#Har number ka square new list mein banao.
numbers = [
    [1, 2, 3],
    [4, 5, 6]
]
new=[x*x for row  in numbers for x in row ]
print(new)

#Sirf even numbers nikalo.
numbers = [
    [10, 15, 20],
    [25, 30, 35],
    [40, 45, 50]
]
even=[x for row in numbers for x in row if x%2==0   ]
print(even)

#Sirf 30 se greater numbers nikalo.
numbers = [
    [10, 20],
    [30, 40],
    [50, 60]
]
newlist=[x for row in numbers for x in row if x>30]
print(newlist)

#Har number ko double karo, lekin sirf even numbers ko.
numbers = [
    [1, 2],
    [3, 4],
    [5, 6]
]
double=[x*2 for row in numbers for x in row if x%2==0]
print(double)