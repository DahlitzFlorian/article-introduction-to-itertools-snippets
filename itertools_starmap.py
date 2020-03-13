from itertools import starmap


def pow_with_input(base, exponent):
    return base, exponent, pow(base, exponent)


values = [(4, 9), (1, 6), (0, 5), (3, 8), (2, 7)]

for i in starmap(pow_with_input, values):
    print("pow({}, {}) = {}".format(*i))
