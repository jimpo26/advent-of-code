import math
import sys
from scipy.cluster.hierarchy import DisjointSet 
gettrace = getattr(sys, 'gettrace', None)
with open("input8.txt" if gettrace() is None else "./2025/input8.txt", "r") as f:
    data = f.read().splitlines()

def get_distance(p1,p2):
    x,y,z = [int(a) for a in p1.split(",")]
    x2,y2,z2 = [int(a) for a in p2.split(",")]

    return math.sqrt(((x2-x)**2) + ((y2-y)**2) + ((z2-z)**2))

circuits = []
n = 0
m = dict() # dist -> points
d = [] # dist. This is needed to be sorted
for p1 in data:
    min_dist = 100_000_000
    for p2 in data:
        if p1 == p2: # if i have the same point distance is 0. not interesting
            continue
        ds = get_distance(p1,p2)
        if ds not in m:
            d.append(ds)
            m[ds] = (p1,p2)

d = sorted(d)[:1000]
x = []
for c in d:
    p1,p2 = m[c]
    x.append(p1)
    x.append(p2)

dis_set = DisjointSet(x)
for c in d:
    dis_set.merge(m[c][0], m[c][1])
tot = 1
for l in sorted(dis_set.subsets(), key=len, reverse=True)[:3]:
    tot *= len(l)
print("part 1", tot)


circuits = []
n = 0
m = dict() # dist -> points
d = [] # dist. This is needed to be sorted
for p1 in data:
    min_dist = 100_000_000
    for p2 in data:
        if p1 == p2: # if i have the same point distance is 0. not interesting
            continue
        ds = get_distance(p1,p2)
        if ds not in m:
            d.append(ds)
            m[ds] = (p1,p2)

dis_len = 0
idx = 6_350
print(len(d))
while dis_len < 1000:
    tmpd = sorted(d)[:idx]
    x = []
    for c in d:
        p1,p2 = m[c]
        x.append(p1)
        x.append(p2)

    dis_set = DisjointSet(x)
    for c in tmpd:
        dis_set.merge(m[c][0], m[c][1])
    dis_len = len(dis_set.subsets()[0])
    idx += 1
    print(idx, dis_len)
p1,p2 = m[tmpd[-1]]
print("part 2", int(p1.split(",")[0]) * int(p2.split(",")[0]))
