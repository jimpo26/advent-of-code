with open("input.txt", "r") as f:
    data = f.read().splitlines()

overlap = 0
for line in data:
    couple = line.split(",")
    couple = [[int(y) for y in x.split('-')] for x in couple]
    couple = [list(range(x[0], x[1]+1)) for x in couple]
    if any(x in couple[0] for x in couple[1]):
        overlap += 1

print(overlap)
