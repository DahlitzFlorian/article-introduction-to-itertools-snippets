from itertools import filterfalse


def is_negative(number):
    return number < 0


numbers = [-1, 0, 4, 1, -3]
positive_numbers = list(filterfalse(is_negative, numbers))

print(positive_numbers)
