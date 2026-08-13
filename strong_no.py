num=int(input("Enter number:"))
original=num
total=0
while num>0:
    digit=num%10
    factorial=1
    i=1
    while i<=digit:
        factorial=factorial*i
        i+=1
    total=total+factorial
    num=num//10

if total == original:
    print("strong number:")
else:
   print("not a strong number:")
