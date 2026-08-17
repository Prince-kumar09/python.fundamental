words=input("enter words:").lower()
count=0
for char in words:
    if char.isalpha() and char not in "aeiou":
        count+=1
print("consonant:",count)        
