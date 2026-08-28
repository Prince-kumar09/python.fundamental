data = ([10, 20], 30)

data[0].append(40)

print(data)



def calculate(a, b):
    return a + b, a - b

result = calculate(10, 5)

print(result)
#Python ne automatically Tuple return kiya.

#@Aur hum unpack kar sakte hain:

sum_value, difference = calculate(10, 5)

print(sum_value)
print(difference)

#Tuple aur *args ⭐

#Functions mein:

def add(*numbers):
    print(numbers)

add(10, 20, 30, 40)


#👉 *args ke andar arguments Tuple ke form mein store hote hain.

#Isliye:

def add(*numbers):
    total = 0

    for x in numbers:
        total += x

    return total

print(add(10, 20, 30))

def add(*numbers):
    print(type(numbers))
    print(numbers)

add(10, 20, 30)
#✅ Correct output:
#<class 'tuple'>
#(10, 20, 30)