word=input("enter word:")
string=""
for char in word:
    if char not in string:
        string=string+char
print("afterremoving the duplicate:",string)