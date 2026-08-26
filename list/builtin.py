'''len()


sum()#sum() normally numeric values ke liye use hota hai.
numbers = [10, 20, 30, 40]
print(sum(numbers))

min()
max()
any()#List mein kam se kam ek value True hai kya?
numbers = [0, 0, 5, 0]

print(any(numbers))
numbers = [0, 0, 0, 0]

print(any(numbers))


all()'''#Kya list ki saari values True hain?
'''| Function | Meaning           |
| -------- | ----------------- |
| `len()`  | Total elements    |
| `sum()`  | Total/sum         |
| `min()`  | Smallest          |
| `max()`  | Largest           |
| `any()`  | At least one True |
| `all()`  | Every value True  |
'''
numbers = [10, 20, 30, 40, 50]

print(len(numbers))
print(sum(numbers))
print(min(numbers))
print(max(numbers))

numbers = [0, 0, 10, 0]

print(any(numbers))

numbers = [2, 4, 6, 7, 8]

print(all(x % 2 == 0 for x in numbers))


numbers = [1, 3, 5, 9, 11]

print(any(x % 2 == 0 for x in numbers))