class Calculator:
    @staticmethod
    def add(a,b):
        return a+b

print(Calculator.add(10,20))



class Calculator:
    @staticmethod
    def square(n):
        return n*n

print(Calculator.square(5))




class Number:
    @staticmethod
    def is_even(n):
        if n%2==0:
            return True
        else:
            return False

print(Number.is_even(5))




class Math:
    @staticmethod
    def is_positive(n):
        if n<=0:
            return False
        else:
            return True

print(Math.is_positive(10))
print(Math.is_positive(-5))
print(Math.is_positive(0))
    