from itertools import takewhile

result = list(takewhile(lambda x: x < 5, [1, 4, 6, 4, 1]))
print(result)
