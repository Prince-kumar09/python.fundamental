# delete the element from the list
'''remove → VALUE 🏷️
pop    → INDEX + value return 📤
del    → INDEX / slice ❌
clear  → EVERYTHING → [] 🧹'''
numbers = [10, 20, 30, 40, 50]
del numbers[2] 
print(numbers)

numbers = [10, 20, 30, 40, 50]
del numbers[-1]
print(numbers)

numbers = [10, 20, 30, 40, 50, 60]
del numbers[1:4]
print(numbers)

'''numbers = [10, 20, 30, 40]
numbers.remove(30)
print(numbers)
numbers.pop(2)
print(numbers)
del numbers[2]
print(numbers)

remove(value)  → value delete
pop(index)     → index delete + deleted value return
del list[index] → index delete
clear()        → saare elements delete → []
del list       → poori list/variable delete

# remove()
numbers = [10, 20, 30, 40]
numbers.remove(30)
print(numbers)


# pop()
numbers = [10, 20, 30, 40]
numbers.pop(2)
print(numbers)


# del
numbers = [10, 20, 30, 40]
del numbers[2]
print(numbers)


'''