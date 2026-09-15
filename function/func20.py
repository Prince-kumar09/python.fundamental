def student(**kwargs):
    for key,value in kwargs.items():
        print(key,":",value)
student(name="prince",age=19,branch="ai/ml",college="itm")