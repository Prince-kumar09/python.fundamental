numbers=[1,2,3,4,5]
result=["even" if x%2==0 else "odd"  for x in numbers ]
print(result)



num=[10,20,30,40,50]
new=["greater" if x>30 else "smaller" for x in num]
print(new)


numbers = [1, 2, 3, 4, 5]
new=[x*2 if x%2==0 else x for x in numbers]
print(new)


numbers = [-10, 20, -30, 40]
new=["positive" if x>0 else "negative" for x in numbers]
print(new)