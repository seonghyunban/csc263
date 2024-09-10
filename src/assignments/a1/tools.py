import random

def generate_random_list(size: int, lb: int, ub: int):

    random_arr = []
    for i in range(size):
        random_arr.append(random.randint(lb, ub))

    return random_arr


def generate_reverse_list(size: int):
    arr = []
    for i in range(size):
        arr.append(size - i)
    return arr
