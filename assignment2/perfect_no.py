

num=int(input("Enter number:"))
i=1
total=0
while  i<num:
    if num%i==0:
        total=total+i
    i+=1
if total==num:
        print("perfect number:")
else:
        print("not a perfect number:")    