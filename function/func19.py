def show(*args):
    print(args)

show(10, 20, 30)


def show(*args):
    for x in args:
        print(x)

show(10, 20, 30)




def show(*args):
    for x in args:
        print(x)
show(10,20,30,40)


def show(*args):
    for x in args:
        return x

print(show(10, 20, 30, 40))# it return only 10


def show(*args):
    return args

print(show(10, 20, 30, 40))


def sum(*args):
    total=0
    for x in args:
        total=total+x
    return total
print(sum(10,20,30))



def count_number(*args):
    count=0
    for x in args:
        
        count+=1
    print(count)
count_number(10,20,30,40)

# same result with retun keyword

def count_numbers(*args):
    count = 0

    for x in args:
        count += 1

    return count

print(count_numbers(10, 20, 30, 40))