file = open("my_intro.txt", "r")

print("First reading:")
print(file.readline())

print("Remaining data:")
print(file.read())

file.close()


