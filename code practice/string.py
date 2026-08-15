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