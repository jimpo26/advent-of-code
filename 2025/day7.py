import sys
from functools import cache
gettrace = getattr(sys, 'gettrace', None)
with open("input7.txt" if gettrace() is None else "./2025/input7.txt", "r") as f:
    data = f.read().splitlines()

start = data[0].find("S")
n = [start]
s = 0
for i in range(1, len(data) - 1):
    to_pop_at = set()
    to_add = set()
    for j in range(len(n)):
        if data[i+1][n[j]] != ".":
            to_pop_at.add(j)
            to_add.add(n[j]-1)
            to_add.add(n[j]+1)
            s += 1

    for v in sorted(list(to_pop_at), reverse=True):
        n.pop(v)
    n += list(to_add)
    n = list(set(n))

print("part 1", s)

start = data[0].find("S")
@cache
def go(row, col):
    if row == len(data):
        return 1
    if data[row][col] != ".":
        return go(row+1, col-1)+go(row+1,col+1)
    return go(row+1,col)

print("part 2", go(0, start))