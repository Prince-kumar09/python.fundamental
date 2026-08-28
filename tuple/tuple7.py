# tuple comprehensdion 
numbers = (1, 2, 3, 4, 5)

result = (x * 2 for x in numbers)

print(type(result)) #output <class 'generator'>
#Python mein normal Tuple Comprehension nahi hota.
#Agar actual Tuple chahiye:

result = tuple(x * 2 for x in numbers)

print(result)