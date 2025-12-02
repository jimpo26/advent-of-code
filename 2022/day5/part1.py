with open("input.txt", "r") as f:
    data = f.read()

containers = data.split("\n\n")[0]
movements = data.split("\n\n")[1].split("\n")
stacks = []
blocks = containers.split("\n")[:-1]
blocks = [f" {block}" for block in blocks]

for i in range(len(blocks)):
    for j in range(len(blocks[i])):
        if j % 4 == 0:
            blocks[i] = blocks[i][:j] + "|" + blocks[i][j+1:]
    blocks[i] = blocks[i][1:]
    blocks[i] = blocks[i].split("|")
stacks = []

for i in range(len(blocks[0])):
    stacks.append([block[i] for block in blocks if block[i].replace(" ", "") != ""])
# dividing the container to have a list of stacks like this: [['[X]','[Y]',...],['[X]','[Y]',...],...]

info = []
for line in movements:
    info = tuple(int(x) for x in line.replace("move ", "").replace("from ", "").replace("to ", "").split(" "))
    for i in range(info[0]):
        stacks[info[2]-1].insert(0, stacks[info[1]-1].pop(0))

final_crate = ""
for stack in stacks:
    # take the first letter of each stack
    final_crate += stack[0][1]

print(final_crate)
