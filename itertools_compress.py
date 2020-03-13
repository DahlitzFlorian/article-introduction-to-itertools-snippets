from itertools import compress


def name_selection(names):
    name_selectors = []

    for name in names:
        if name.startswith("A"):
            name_selectors.append(1)
        else:
            name_selectors.append(0)

    return name_selectors


names = ["Albert", "Alexandra", "Miriam", "Sascha"]
filtered_names = list(compress(names, name_selection(names)))

print(f"Filtered names: {filtered_names}")
