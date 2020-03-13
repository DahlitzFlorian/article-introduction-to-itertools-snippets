from itertools import chain

class1 = ["Alice", "Bob", "Chris"]
class2 = ["Larry", "Margaret", "Naomi", "Sarah"]
all_people = list(chain(class1, class2))

print(f"All people: {all_people}")
