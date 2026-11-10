file = open("my_intro.txt", "r")

data = file.readlines()

print(data)

file.close()


file = open("my_intro.txt", "r")

data = file.readlines()

for line in data:
    print(line.strip())

file.close()



file = open("my_intro.txt", "r")

data = file.readlines()

print(type(data))
print(len(data))

file.close()



file = open("my_intro.txt", "r")

data = file.readlines()

print(data[0])
print(data[1])
print(data[2])

file.close()