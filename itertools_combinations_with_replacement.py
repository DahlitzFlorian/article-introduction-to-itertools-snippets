from itertools import combinations_with_replacement

l = [1, 2, 3]
result1 = list(combinations_with_replacement(l, 3))
result2 = list(combinations_with_replacement(l, 2))

print(result1)
print(result2)
