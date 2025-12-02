with open("input1.txt", "r") as f:
    data = f.read().splitlines()

def part1():
    pos, times = 50, 0
    for d in data:
        n = int(d[1:]) % 100
        if d[0] == "L":
            pos -= n
        else:
            pos += n
        
        if pos < 0:
            pos += 100
        if pos > 99:
            pos -= 100
        if pos == 0:
            times += 1
    print(pos, times)

def part2():
    pos, times = 50, 0
    for d in data:
        dr, n = d[0], int(d[1:])
        for _ in range(n):
            pos += 1 if dr == "R" else -1
            pos %= 100
            times += pos == 0
    print(pos, times)
    

part2()
