word=input("Enter string:")
reverse=""
for char in word:
    reverse=char+reverse
if word==reverse:
    print("palindrome")
else:
    print("not a palindrome: ")