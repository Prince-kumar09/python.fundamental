num=int(input("Enter number:"))
square=num*num
temp=num
count=0
while temp>0:
    temp=temp//10
    count+=1
last_digit=square%(10**count)

if last_digit==num:

    print("Automorphic number:")
else:
     print("Not a automorphic number:")

