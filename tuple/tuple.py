numbers = (10, 20, 30, 40)

print(numbers)
'''numbers = (10, 20, 30)

numbers[0] = 100  #error aayega
'''
# in list 
numbers = [10, 20, 30]

numbers[0] = 100

print(numbers)
#LIST = Change allowed 🔄
#TUPLE = Change NOT allowed 🔒

a = (10)
b = (10,)
print(type(a))#<class 'int'>
print(type(b))#<class 'tuple'>