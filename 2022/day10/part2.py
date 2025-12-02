with open("input.txt", "r") as f:
    lines = f.read().splitlines()


def twenth_cycle(c):
    return any([c == x for x in range(0, 230, 40)])


def increment(c, i):
    c += 1
    if twenth_cycle(c):
        return c, i+1
    return c, i


def render(line, s, c):
    line[c % 40] = s[c % 40]


CRT = [["" for _ in range(41)] for _ in range(6)]
SPRITE = "###....................................."
cycles = 0
index = 0
register = 1
for line in lines:
    if line == "noop":
        render(CRT[index], SPRITE, cycles)
        cycles, index = increment(cycles, index)
    else:
        render(CRT[index], SPRITE, cycles)
        cycles, index = increment(cycles, index)
        render(CRT[index], SPRITE, cycles)
        cycles, index = increment(cycles, index)

        register += int(line.split()[1])
        SPRITE = '........................................'
        SPRITE = SPRITE[:register-1] + '###' + SPRITE[register+2:]

for line in CRT:
    print(line)
