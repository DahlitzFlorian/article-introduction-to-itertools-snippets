from itertools import zip_longest

a = [1, 2, 3]
b = ["One", "Two"]

result1 = list(zip(a, b))
result2 = list(zip_longest(a, b))

print(result1)
print(result2)
