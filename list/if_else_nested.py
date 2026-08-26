

#[expression_if_true if condition else expression_if_false
 #for row in numbers
 #for x in row]

numbers = [
    [10, 20],
    [30, 40],
    [50, 60]
]
next=[ x*2 if x%2==0 else x for row in numbers for x in row]
print(next)

#Number 20 se greater/equal ho → "Big" Otherwise → "Small"
numbers = [
    [5, 10],
    [15, 20],
    [25, 30]
]
new=["big" if x>=20 else "small" for row in numbers for x in row]
print(new)

# even odd
numbers = [
    [1, 2, 3],
    [4, 5, 6]
]
even=["e" if x%2==0 else"o" for row in numbers for x in row]
print(even)

#1️⃣ Sirf if ho → IF ko LAST mein rakho
# 2️⃣ if-else ho → IF ko START mein rakho 
# "Kya dena hai → IF → ELSE → FOR"
#ONLY IF:
'''[WHAT for x in LIST if CONDITION]
              ↑
            LAST


IF + ELSE:
[TRUE_VALUE if CONDITION else FALSE_VALUE for x in LIST]
 ↑
START


NESTED:
[WHAT for row in LIST for x in row]
       ↑              ↑
     OUTER          INNER '''