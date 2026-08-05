#sum of digits
num=int(input("Enter number:"))
sum_digits=0
while num>0:
    digit=num%10
    sum_digits+=digit
    num=num//10
    print("sum=",sum_digits)
