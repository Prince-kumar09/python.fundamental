#Positive or Negative Until User Writes Quit
while True:

    value = input("Enter number or Quit: ")

    if value.lower() == "quit":
        break

    n = int(value)

    if n > 0:
        print("Positive")
    elif n < 0:
        print("Negative")
    else:
        print("Zero")