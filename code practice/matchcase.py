color=input("Enter the color:")
match color:
    case "red":
        print("stop")
    case "green":
        print("go")
    case "yellow":
        print("look")
    case _:
        print("wrong color for traffic light:")
    