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

print(show(10, 20, 30, 40))# it retun only 10


def show(*args):
    return args

print(show(10, 20, 30, 40))