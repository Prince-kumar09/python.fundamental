word="prince"
word="kumar"
print(word)

text = "banana"
print(text.replace("a", "e", 1))

text = "apple apple apple"
print(text.replace("apple", "mango", 2))

text = "I love Python"
print(text.find("love"))

text = "Python python PYTHON"

print(text.lower().count("python"))

#boolean string type
text = "Python Programming"
text.startswith("Python")       # True
text.startswith("Programming")  # False

text.endswith("Programming")    # True
text.endswith("Python")         # False 
print(text.startswith("Python"))
print(text.endswith("Python"))

#imp concept split method
text = "Python is easy"

words = text.split()

print(words)

print(type(words))

text = "I love Python"
text.find("Python")     # 7
text.count("Python")    # 1
text.split()            # ['I', 'love', 'Python']

words = "I love Python".split()

print(words[1])


words = ["I", "love", "Python"]

result = " ".join(words)

print(result)


fruits = ["apple", "banana", "mango"]

result = ",".join(fruits)

print(result)
#some boolean string concept
#isalpha
text = "Python"

print(text.isalpha())  #true
text = "Python Programming"

print(text.isalpha()) #false beacause space doesnot allowed 
text = "Python123"

print(text.isalpha()) #false

#isdigit
text = "12345"

print(text.isdigit()) #true otherwise false same as isalpha

#isalnum  allowed numand alphabets but does not allowed space and special character like @$% and so same as isalpha and isdigit also

text = "12345"

print(text.isalnum()) #true
text="prince"
print(text.isalnum()) #true
text = "Python123"

print(text.isalnum()) #true

#isspace it allow omly space
text = "   "

print(text.isspace()) #true

text = "Python"

print(text.isspace()) #false

text="prince kumar"
print(text.isspace()) #false

text = "PyThOn"

print(text.swapcase())# change upper letter to lower letter and and lower letter to upper letter

#string travellsing using for loop
word = input("Enter string:").lower()
count = 0

for char in word:
    if char in "aeiou":
        count += 1

print("Vowels =", count)