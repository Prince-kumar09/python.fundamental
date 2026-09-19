#sum of n number based on recusion
def sum_n(n):
    if n == 0:
        return 0

    return n + sum_n(n - 1)

print(sum_n(5))



#sum based question on recursion  in decressing order
def sum_n(n):
    if n == 0:
        return 0

    return n + sum_n(n - 1)

print(sum_n(5))

#factorial based question

def factorial(n):
    if n == 0:
        return 1

    return n * factorial(n - 1)

print(factorial(5))

#power based question

def power(a,n):
    if n == 0:
        return 1

    return a * power(a,n-1)

print(power(2,5))