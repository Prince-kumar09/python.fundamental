#store result in the list
numbers=[1,2,3,4,5]
even=[]
for x in numbers:
    if x%2==0:
        even.append("even")
    else:
        even.append("odd")
print(even)    
# [x if condition else y for x in numbers]
# by using list comprehension
numbers = [1, 2, 3, 4, 5]

result = ["Even" if x % 2 == 0 else "Odd" for x in numbers]

print(result)    