with open("input.txt", "r") as f:
    data = f.read().split("\n\n")

total = []
for line in data:
    tmp = line.split("\n")
    total.append(sum([int(x) for x in tmp]))

total.sort(reverse=True)
print(sum(total[0:3]))
