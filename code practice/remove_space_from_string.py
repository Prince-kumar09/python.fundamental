#Remove Spaces from String
word=input("enter word:")
new_word=""
for char in word:
    if not char.isspace():
        new_word=new_word+char
print("after removing the string:",new_word)