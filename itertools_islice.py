from itertools import islice

list1 = list(islice(range(50), 2))
list2 = list(islice(range(50), 40, 44))
list3 = list(islice(range(50), 5, 45, 10))

print(f"islice with stop parameter only: {list1}")
print(f"islice with start and stop: {list2}")
print(f"islice with start, stop, and step: {list3}")
