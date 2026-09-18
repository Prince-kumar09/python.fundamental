def outer():
    def inner():
        print("hellow prince")
    inner()
outer()



def calculator(a, b):

    def add():
        return a + b

    return add()

print(calculator(10, 20))