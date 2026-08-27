# tuple inside list
a = [(10, 20), (30, 40), (50, 60)]

print(a[1])
print(a[1][0])


# nested tuple

a = ((10, 20), (30, 40))

print(a[0][1])
print(a[1][0])

#Tuple with * Unpacking
a = (10, 20, 30, 40, 50)

x, y, *z = a

print(x)
print(y)
print(z)