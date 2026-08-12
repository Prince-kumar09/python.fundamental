num=int(input("Enter number:"))
original=num
total=0
while num>0:
    digit=num%10
    total=total+digit*digit*digit
    num=num//10
if total==original:
        print("armstrong number:")
else:
        print("not a armstrong number:")