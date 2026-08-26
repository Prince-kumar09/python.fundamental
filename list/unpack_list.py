# unpack the list
'''✅ List Unpacking — COMPLETE

Ab tum ye concepts samajh chuke ho:

a, b, c = list
* unpacking
a, *b = list
a, *b, c = list
a, b, *c = list
Variable/value count mismatch ka ValueError
Python mein direct variable swapping
🧠 Golden Rule

Normal variables = exact values
*variable = remaining values ko list mein collect karta hai'''
numbers = [10, 20, 30]

a, b, c = numbers# normal packing

print(a)
print(b)
print(c)

numbers = [10, 20, 30, 40, 50]

a, *b = numbers

print(a)
print(b)

numbers = [10, 20, 30, 40, 50]

a, *b, c = numbers

print(a)
print(b)
print(c)


#swaping of two number
a = 10
b = 20

a, b = b, a

print(a)
print(b)
