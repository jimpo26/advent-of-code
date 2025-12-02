with open("input.txt", "r") as f:
    data = f.read().split("\n\n")

total = []
for line in data:
    tmp = line.split("\n")
    total.append(sum([int(x) for x in tmp]))

print(max(total))