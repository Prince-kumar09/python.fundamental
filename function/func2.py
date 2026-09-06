def calculate_bill(item,price,quantity):
    print("item:",item)
    total=price*quantity
    print("total:",total)
    if total >=1000:
        print("free delhivery")
    else:
        print("delhivery charge applicable")
calculate_bill('shoes',500,2)