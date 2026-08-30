numbers = [10, 20, 20, 30, 40, 40, 50, 50, 50]

seen = set()
duplicates = set()

for x in numbers:
    if x in seen:
        duplicates.add(x)
    else:
        seen.add(x)

print(duplicates)