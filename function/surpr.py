def surprise_message(name, mood="happy"):
    print("\n--- Surprise Message ---")
    print("For:", name)

    if mood == "happy":
        print("Keep smiling! You make the world brighter.")
    elif mood == "sad":
        print("Bad days don't last forever. Stay strong!")
    elif mood == "tired":
        print("Take a break. You deserve some rest.")
    else:
        print("You are special. Keep moving forward!")


surprise_message("Prince")
surprise_message("Aman", "sad")
surprise_message("Rahul", "tired")
surprise_message("Priya", "excited")