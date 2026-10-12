
class Number:
    def __init__(self, value):
        self.value= value

    def __add__(self, other):
        return self.value + other.value

n1 = Number(10)
n2 = Number(20)

print(n1 + n2)


class Price:
    def __init__(self,amount):
        self.amount=amount
    def __add__(self, other):
        return self.amount + other.amount

p1=Price(100)
p2=Price(250)

print(p1+p2)



class Price:
    def __init__(self,amount):
        self.amount=amount
    def __add__(self, other):
        return self.amount + other.amount

p1=Price(500)
p2=Price(2300)

print(p1+p2)                            
