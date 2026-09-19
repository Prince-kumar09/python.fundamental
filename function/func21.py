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
    return add() , subtract()
print(calculator(10, 20))



