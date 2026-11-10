file=open("my_intro.txt","r")
data=file.readline()
data=file.readline()
data=file.readline()
print(data)
file.close()
#readline it means it read the first line


#another code

file = open("my_intro.txt", "r")
print(file.readline())
print(file.readline())
print(file.readline())
file.close()


#another one 
file = open("my_intro.txt", "r")

line1 = file.readline()
line2 = file.readline()

print("First line:", line1)
print("Second line:", line2)

file.close()
