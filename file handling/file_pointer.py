file = open("my_intro.txt", "r")

print("First reading:")
print(file.readline())

print("Remaining data:")
print(file.read())

file.close()


file=open("demo.txt","r")
print("position:",file.tell())
print(file.read(5))
print("position:",file.tell())
file.seek(0)
print("after seek:",file.tell())
print(file.read())
file.close()