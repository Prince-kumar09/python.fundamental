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

