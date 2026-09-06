def discount(price, discount):
    discount_amount = price * discount / 100

    final_price = price - discount_amount

    return final_price

result = discount(1000, 20)
print(result)
    

