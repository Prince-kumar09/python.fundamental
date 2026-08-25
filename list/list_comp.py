numbers=[1,2,3,4,5]
sqr=[x*x for x in numbers]
print(sqr)

number2=[10,20,30,40,50]
num=[x*5 for x in number2]
print(num)

numbers3=[10,15,20,25,30,35]
even=[]
for x in numbers3:
    if x%2==0:
        even.append(x)
print(even)

numbers4=[5,10,15,20,25,30]
new=[]
for x in numbers4:
    if x>20:
        new.append(x)
print(new)        

num2=[1,2,3,4,5]
result=[]
for x in num2:
    result.append(x+10)
print(result)    