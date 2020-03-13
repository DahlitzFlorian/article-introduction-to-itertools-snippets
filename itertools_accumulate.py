from itertools import accumulate
from operator import mul

numbers = [1, 2, 3, 4, 5]
result1 = accumulate(numbers)
result2 = accumulate(numbers, mul)
result3 = accumulate(numbers, initial=100)

print(f"Result 1: {list(result1)}")
print(f"Result 2: {list(result2)}")
print(f"Result 3: {list(result3)}")
