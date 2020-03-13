from itertools import islice
from itertools import tee

s = islice(range(100), 3)
s1, s2 = tee(s)

print(f"First list: {list(s1)}")
print(f"Second list: {list(s2)}")
