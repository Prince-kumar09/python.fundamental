fruits=["apple","mango","banana","orange","grapes"]
print(len(fruits))#total element of the list


#sum of the list
numbers=[5,10,15,20,25]
total=0
for x in numbers:
    total=total+x
print(total)

#count even number in the list
numbers=[10,15,20,25,30,40]
count=0
for x in numbers:
    if x%2==0:
        count+=1
print(count)