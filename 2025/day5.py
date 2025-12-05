import sys
gettrace = getattr(sys, 'gettrace', None)

with open("input5.txt" if gettrace() is None else "./2025/input5.txt", "r") as f:
    ranges, ids = f.read().split("\n\n")

ranges = ranges.split("\n")
ids = ids.split("\n")

for i in range(len(ranges)):
    t = ranges[i].split("-")
    ranges[i] = (int(t[0]), int(t[1]))

s = set()
f = 0
for iid in ids:
    for r in ranges:
        if int(iid) >= r[0] and int(iid) <= r[1] and iid not in s:
            f += 1
            s.add(iid)
print("part 1", f)

f = 0
m = False
ws = []
skip = []
t = 0
while t < 100:
    for j in range(len(ranges)):
        m = False
        l,h = ranges[j]
        for s in skip:
            if s == j:
                continue
        for i in range(len(ws)):
            wl,wh = ws[i]
            if l <= wl and wl <= h <= wh:
                ws[i] = (l,wh)
                m = True
            elif l >= wl and l <= wh <= h:
                ws[i] = (wl,h)
                m = True
            elif l <= wl and h >= wh:
                ws[i] = (l,h)
                m = True
            elif l >= wl and h <= wh:
                m = True
                skip.append(j)
        if not m:
            ws.append(ranges[j])
    ranges = ws.copy()
    ws = []
    skip = []
    m = False
    t += 1

for g in ranges:
    f += g[1]-g[0]+1
print("part 2", f)