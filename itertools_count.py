from itertools import count

names = ["Alice", "Bob", "Larry", "Margaret"]
names_with_index = [name for name in zip(count(1), names)]
print(names_with_index)
