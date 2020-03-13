from itertools import dropwhile

result = list(dropwhile(lambda x: x < 5, [1, 4, 6, 4, 1]))
print(result)
