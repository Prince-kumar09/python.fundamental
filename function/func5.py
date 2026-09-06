def discount(price,discount):
    discount_amount=price*discount/100
    final_price=price-discount_amount
    
    return final_price
result=discount(1000,20)
result1=discount(2500,10)
result2=discount(5000,30)
print(result)
print(result1)
print(result2)
