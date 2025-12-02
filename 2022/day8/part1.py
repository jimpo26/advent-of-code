with open("input.txt", "r") as f:
    lines = f.read().splitlines()

grid = []
for line in lines:
    grid.append([int(x) for x in line])


count = 0
visible_tree = 0
for i in range(1, len(grid) - 1):
    for j in range(1, len(grid[i]) - 1):
        if grid[i][j] > max(grid[i][:j]) or grid[i][j] > max(grid[i][j+1:]) or \
            grid[i][j] > max([grid[x][j] for x in range(len(grid))][:i]) or \
                grid[i][j] > max([grid[x][j] for x in range(len(grid))][i+1:]):
            visible_tree += 1

        count += 1

total = sum([len(x) for x in grid])
print(visible_tree + (total - count))
