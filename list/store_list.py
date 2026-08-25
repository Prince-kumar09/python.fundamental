#store result in the list
numbers=[1,2,3,4,5]
even=[]
for x in numbers:
    if x%2==0:
        even.append("even")
    else:
        even.append("odd")
print(even)        