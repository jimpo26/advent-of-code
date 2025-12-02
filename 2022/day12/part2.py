from collections import deque

with open("input.txt", "r") as f:
    data = f.read().splitlines()

grid: list[list[str]] = []
start, end = None, None
for line in data:
    if "S" in line:
        start = (line.index("S"), len(grid))
    if "E" in line:
        end = (line.index("E"), len(grid))
    grid.append(list(line.replace("S", "a").replace("E", "z")))


for i in range(len(grid)):
    for j in range(len(grid[i])):
        if grid[i][j] == "S":
            start = (i, j)
        elif grid[i][j] == "E":
            end = (i, j)


queue = deque()
queue.append((0, end[1], end[0]))
vis = {end[1], end[0]}
count = 0

while queue:
    steps, row, col = queue.popleft()

    for nrow, ncol in [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]:

        if nrow < 0 or ncol < 0 or nrow >= len(grid) or ncol >= len(grid[0]) or \
                (nrow, ncol) in vis or ord(grid[nrow][ncol]) - ord(grid[row][col]) < -1:
            continue

        if grid[nrow][ncol] == "a":
            count = steps + 1
            queue.clear()
            break

        vis.add((nrow, ncol))
        queue.append((steps + 1, nrow, ncol))
print(count)