num=int(input("Enter number:"))
original=num
total=0
while num>0:
    digit=num%10
    total=total+digit
    num=num//10
if original%total==0:
    print("Harshad number:")
else:
    print("Not a Harshad number:")