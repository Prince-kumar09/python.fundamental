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