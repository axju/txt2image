from random import randrange

def random_color():
    return tuple([randrange(0,255) for i in range(3)])
