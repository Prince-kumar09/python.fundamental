def calculate_price(price, tax=18):
    tax_amount = price * tax / 100
    final_price = price + tax_amount

    print("price:", price)
    print("final price:", final_price)

calculate_price(1000)
calculate_price(1000, 10)