import sys
import math
from shapely import Polygon
from shapely.geometry import Point
import matplotlib.pyplot as plt
gettrace = getattr(sys, 'gettrace', None)
with open("input9.txt" if gettrace() is None else "./2025/input9.txt", "r") as f:
    data = f.read().splitlines()

def get_area(p1,p2):
    x,y = [int(a) for a in p1.split(",")]
    x2,y2 = [int(a) for a in p2.split(",")]
    
    return (abs(x-x2)+1) * (abs(y-y2)+1)

def get_distance(p1,p2):
    x,y = [int(a) for a in p1.split(",")]
    x2,y2 = [int(a) for a in p2.split(",")]

    return math.sqrt(((x2-x)**2) + ((y2-y)**2))

def get_angles(p1,p2):
    x,y = [int(a) for a in p1.split(",")]
    x2,y2 = [int(a) for a in p2.split(",")]

    return ((x,-y),(x,-y2),(x2,-y2),(x2,-y))

def check_inside_polygon(p: tuple[int,int]):
    x,y = p
    for i in range(x-1):
        if (i,y) in spoints:
            return True

cnt = 0
max_a = 0
aa = dict()
aa2 = []
points = []
for p1 in data:
    x,y = [int(a) for a in p1.split(",")]
    points.append((x,-y))
    for p2 in data:
        if p1 == p2:
            continue
        a = get_area(p1,p2)
        if a > max_a:
            max_a = a
        aa2.append(str(a) + "_" + str(cnt))
        aa[str(a) + "_" + str(cnt)] = (p1,p2)
        cnt += 1
print("part 1", max_a)
aa2.sort(reverse=True)
spoints = set(points)

p = Polygon(points)
print(p)
max_a = 0
it = 0
for d in aa2: # 245k iterations
    it += 1
    if int(d.split("_")[0]) <= max_a:
        continue
    angles = get_angles(*aa[d])
    pol2 = Polygon(list(angles))
    # plt.plot(*p.exterior.xy)
    # plt.plot(*pol2.exterior.xy)
    # plt.show()
    if pol2.within(p):
        max_a = int(d.split("_")[0])
print("part 2", max_a)

# BROOOOOOO... that was SOOOOOO sick