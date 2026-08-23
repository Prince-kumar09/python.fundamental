principal = int(input("Enter principal: "))
rate = float(input("Enter rate %: "))
time = int(input("Enter time (years): "))

amount = principal * (1 + rate/100) ** time
ci = amount - principal
print(f"Compound Interest = {ci:.2f}")