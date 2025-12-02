with open("input.txt", "r") as f:
    data = f.read().splitlines()


def sublist(lst1, lst2):
    return set(lst1).issubset(set(lst2))


already_cleaned = 0
for line in data:
    couple = line.split(",")
    couple = [[int(y) for y in x.split('-')] for x in couple]
    couple = [list(range(x[0], x[1]+1)) for x in couple]
    if sublist(couple[0], couple[1]) or sublist(couple[1], couple[0]):
        already_cleaned += 1

print(already_cleaned)
