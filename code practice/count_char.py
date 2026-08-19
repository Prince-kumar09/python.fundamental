word = input("Enter word: ")
target = input("Enter the character which you want to find: ")

count = 0

for char in word:
    if char == target:
        count += 1

if len(target) == 1:
    print("Frequency =", count)
else:
    print("Enter single character only")