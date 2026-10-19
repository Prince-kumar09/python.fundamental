def weather_advisor(city, temperature, unit="C"):
    print("\n--- Weather Report ---")
    print("City:", city)
    print("Temperature:", temperature, unit)

    if temperature >= 35:
        print("Advice: Stay hydrated!")
    elif temperature >= 20:
        print("Advice: Enjoy the pleasant weather!")
    else:
        print("Advice: Wear warm clothes!")


weather_advisor("Gorakhpur", 38)
weather_advisor("Lucknow", 28)
weather_advisor("Delhi", 12)
weather_advisor("Mumbai", 32, "C")