#global and local variable

def intro():
    name="prince"
    print(name)
intro()


x = 10

def change():
   global x
   x = 50

change()

print(x)


x = 10

def test():
    x = 20
    print(x)

test()
print(x)