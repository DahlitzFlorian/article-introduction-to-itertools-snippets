from itertools import groupby
from operator import itemgetter

data = [
    (0, 0),
    (0, 1),
    (1, 4),
    (0, 9),
    (1, 2),
    (2, 5),
    (1, 6),
]

data.sort()

for k, v in groupby(data, itemgetter(0)):
    print(k, list(v))
