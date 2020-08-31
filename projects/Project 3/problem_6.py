import random
import math


def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """

    if len(ints) == 0:
        return (None, None)

    min_num = math.inf
    max_num = -math.inf

    for num in ints:
        max_num = max(num, max_num)
        min_num = min(num, min_num)

    return (min_num, max_num)


# Example Test Case of Ten Integers

ls = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(ls)
print("Pass" if ((0, 9) == get_min_max(ls)) else "Fail")

ls = [i for i in range(-9, 1)]  # a list containing -9 to 0
random.shuffle(ls)
print("Pass" if ((-9, 0) == get_min_max(ls)) else "Fail")

ls = [i for i in range(-12, 13)]  # a list spanning zero
random.shuffle(ls)
print("Pass" if ((-12, 12) == get_min_max(ls)) else "Fail")

ls = [42]  # a list with a single value
random.shuffle(ls)
print("Pass" if ((42, 42) == get_min_max(ls)) else "Fail")

ls = []  # an empty list
random.shuffle(ls)
print("Pass" if ((None, None) == get_min_max(ls)) else "Fail")
