x=float(input("enter first no:"))
op=input("choose operator(+.-,*,/,//,%,**):")
y=float(input("enter second no:"))
if op == "+":
    print("addition:",x+y)
elif op=="-":
    print("substraction:",x-y)
elif op=="*":
    print("multiplication:",x*y)
elif op=="/":
    print("division:",x/y)
elif op=="//":
    print("floor division:",x//y)
elif op=="%":
    print("modulo:",x%y)
elif op=="**":
    print("square:",x**y)
else:
    print("invalid the operator:")
  
