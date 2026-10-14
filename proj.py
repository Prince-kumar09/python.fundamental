def study_advisor(name, available_hours, energy, goal="Python"):
    print("\n--- SMART STUDY ADVISOR ---")
    print("Student:", name)
    print("Study Goal:", goal)
    print("Available Hours:", available_hours)

    if energy == "high":
        study_hours = available_hours
        print("Advice: Learn a new concept")

    elif energy == "medium":
        study_hours = available_hours * 0.75
        print("Advice: Practice and revise")

    else:
        study_hours = available_hours * 0.5
        print("Advice: Light revision")

    break_minutes = int(study_hours * 10)

    print("Suggested Study:", study_hours, "hours")
    print("Break Time:", break_minutes, "minutes")


study_advisor("Prince", 3, "high")
study_advisor("Aman", 4, "low", "AI/ML")