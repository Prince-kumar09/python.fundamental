def habit_tracker(name, habit, completed=False):
    print("\n--- Daily Habit Tracker ---")
    print("Name:", name)
    print("Habit:", habit)

    if completed:
        print("Status: Completed! 🎉")
    else:
        print("Status: Pending. Keep going!")


habit_tracker("Prince", "Python Practice", True)
habit_tracker("Prince", "Exercise")
habit_tracker("Prince", "English Speaking", True)