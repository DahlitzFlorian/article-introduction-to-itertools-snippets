from itertools import permutations

l = [1, 2, 3]
result1 = list(permutations(l))
result2 = list(permutations(l, 2))

print(result1)
print(result2)
