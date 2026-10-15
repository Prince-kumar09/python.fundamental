def cube(number):
    square=number*number*number
    return square
result=cube(4)
print(result)   



def pocket_money(name, money, expense=0):
    remaining = money - expense

    print("Name:", name)
    print("Pocket Money:", money)
    print("Expense:", expense)
    print("Remaining Money:", remaining)


pocket_money("Prince", 500)
pocket_money("Aman", 1000, 300)
pocket_money("Rahul", 800, 200)