def check_password(password):
    if len(password) < 6:
        print("Weak Password")
    elif len(password) < 10:
        print("Medium Password")
    else:
        print("Strong Password")


check_password("abc")
check_password("prince123")
check_password("python12345")