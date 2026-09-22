numbers = [1, 2, 3, 4, 5, 6]

result = filter(lambda x: x % 2 == 0, numbers)

print(list(result))


numbers = [10, 15, 20, 25, 30, 35]

result = filter(lambda x: x % 2 == 0, numbers)

print(list(result))





def count_characters(name):
    return len(name)

print(count_characters("Prince"))




def count_vowels(text):
    count = 0

    for x in text:
        if x in "aeiou":
            count += 1

    return count

print(count_vowels("education"))