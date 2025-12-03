import sys
gettrace = getattr(sys, 'gettrace', None)

with open("input3.txt" if gettrace() is None else "./2025/input3.txt", "r") as f:
    data = f.read().splitlines()
tot = 0
for line in data:
    f, s = 0, 0
    pos = 0
    for i in range(len(line)-1):
        if int(line[i]) > f:
            f = int(line[i])
            pos = i
    for i in range(pos+1, len(line)):
        if int(line[i]) > s:
            s = int(line[i])

    tot += int(str(f)+str(s))

print("part 1", tot) 
        

tot = 0
for line in data:
    vals = [0] * 12
    pos = 0
    cnt = 0
    while cnt < 12:
        for i in range(pos,len(line)-11+cnt):
            if int(line[i]) > vals[cnt]:
                vals[cnt] = int(line[i])
                pos = i+1
        cnt += 1

    tot += int(''.join(str(x) for x in vals))

print("part 2", tot)