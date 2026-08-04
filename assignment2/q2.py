#write the function that takes two integers a and b and prints all evenn numbers between them (inclusive)
def even_num(a,b):
    for i in range(a,b+1):
        if i%2==0:
            print(i)
a=int(input("enter first number:"))
b=int(input("enters econd number: "))
even_num(a,b)