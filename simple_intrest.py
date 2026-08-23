principal = int(input("Enter principal: "))
rate = float(input("Enter rate %: "))
time = int(input("Enter time (years): "))

si = (principal * rate * time) / 100
print(f"Simple Interest = {si}")