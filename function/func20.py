def student(**kwargs):
    for key,value in kwargs.items():
        print(key,":",value)
student(name="prince",age=19,branch="ai/ml",college="itm")





def student(*args, **kwargs):
    for x in args:
        print(x)
    for key , value in kwargs.items():
        print(key,":", value)   

student("python","ai","ml",name="prince",age=19) 





def profile(*args, **kwargs):

    total = 0

    for x in args:
        total = total + x

    for key, value in kwargs.items():
        print(key, ":", value)

    print("Total:", total)

profile(10, 20, 30, name="prince", branch="ai/ml")