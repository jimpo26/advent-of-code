with open("input.txt", "r") as f:
    lines = f.read().splitlines()

grid = []
for line in lines:
    grid.append([int(x) for x in line])


count = 0
visible_tree = 0
total_scenic_scores = []
for i in range(1, len(grid) - 1):
    for j in range(1, len(grid[i]) - 1):

        left = 0
        for k in range(j-1, -1, -1):
            left += 1
            if grid[i][k] >= grid[i][j]:
                break

        right = 0
        for k in range(j+1, len(grid[i])):
            right += 1
            if grid[i][k] >= grid[i][j]:
                break

        up = 0
        for k in range(i-1, -1, -1):
            up += 1
            if grid[k][j] >= grid[i][j]:
                break

        down = 0
        for k in range(i+1, len(grid)):
            down += 1
            if grid[k][j] >= grid[i][j]:
                break

        total_scenic_scores.append(left*right*up*down)

print(max(total_scenic_scores))
