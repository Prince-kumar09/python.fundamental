word=input("Enter words:")
reverse=""
for char in word:
    reverse=char+reverse
print("the given reverse word=",reverse)# uf we write reverse = reverse + char it cant be reverse the word 