word=input("Enter string:")
count=0
for char in word:
    if not char.isalnum() and not char.isspace():
        count+=1
print("special character=",count)        