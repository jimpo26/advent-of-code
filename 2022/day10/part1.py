with open("input.txt", "r") as f:
    lines = f.read().splitlines()


def twenth_cycle(c):
    return any([c == x for x in range(20, 240, 40)])


def increment(c, r, s):
    c += 1
    if twenth_cycle(c):
        s += r * c
    return c, s


signal_strength = 0
register = 1
cycles = 0
for line in lines:
    if line == "noop":
        cycles, signal_strength = increment(cycles, register, signal_strength)
    else:
        cycles, signal_strength = increment(cycles, register, signal_strength)
        cycles, signal_strength = increment(cycles, register, signal_strength)
        register += int(line.split()[1])
print(signal_strength)
