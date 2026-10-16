def score_analyzer(name, score, bonus=0):
    final_score = score + bonus

    print("\n--- Gaming Report ---")
    print("Player:", name)
    print("Final Score:", final_score)

    if final_score >= 1000:
        print("Rank: Legend 🏆")
    elif final_score >= 500:
        print("Rank: Pro ⭐")
    else:
        print("Rank: Beginner 🎮")


score_analyzer("Prince", 800)
score_analyzer("Aman", 450, 100)
score_analyzer("Rahul", 300, 50)