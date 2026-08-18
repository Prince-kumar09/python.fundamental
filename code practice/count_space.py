word=input("Enter string:")
count=0
for char in word:
    if char.isspace():
        count+=1
print("space=",count)    