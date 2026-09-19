def outer():
    def inner():
        print("hellow prince")
    inner()
outer()



def calculator(a, b):

    def add():
        return a + b
      

    
    def subtract():
        return a - b
    def multiply():
        return a * b
    def sqr():
        return a*a
    return add() , subtract() ,multiply(),sqr()
print(calculator(10, 20))



