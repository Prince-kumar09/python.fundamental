word=input("Enter words:")
count=0
for char in word:
    if char.isdigit():
        count+=1
print("Digit=",count)        