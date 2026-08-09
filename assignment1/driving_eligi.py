age=int(input("enter your age:"))
license=input("license available(yes/no):")
if age>=18 and license=="yes":
    print("eligible to drive:")
else:
    print("not eligible to drive:")