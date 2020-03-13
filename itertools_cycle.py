from itertools import cycle

names = ["Alice", "Bob", "Chris", "Larry", "Margaret", "Naomi", "Sarah"]
groups = cycle([1, 2, 3])
names_with_groups = [name for name in zip(names, groups)]

print(names_with_groups)
