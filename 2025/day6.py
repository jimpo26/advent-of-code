import sys
gettrace = getattr(sys, 'gettrace', None)
with open("input6.txt" if gettrace() is None else "./2025/input6.txt", "r") as f:
    data = f.read().splitlines()

ops = [x for x in data.pop().split(" ") if x != ""]
nums = []
for i in range(len(data)):
    nums.append([x for x in data[i].split(" ") if x != ""])


tot = 0
for j in range(len(nums[0])):
    n = 0 if ops[j] == "+" else 1
    for i in range(len(nums)):
        if ops[j] == "+":
            n += int(nums[i][j])
        else:
            n *= int(nums[i][j])
    tot += n

print("part 1", tot)

tot = 0
nums = []
nums2 = []
for i in range(len(data)):
    tmp = data[i].split(" ")
    a = []
    for t in tmp:
        if t == '':
            a.append('')
        else:
            a += (list(t))
    nums.append(a)

for i in range(len(data)):
    nums2.append([x for x in data[i].split(" ") if x != ""])
for j in range(len(nums2[0])): # range 0-5
    final = []
    n = 0 if ops[j] == "+" else 1
    l = 0
    for i in range(len(nums2)): # range 0-3
        if len(nums2[i][j]) > l:
            l = len(nums2[i][j])
    
    for i in range(len(nums2)): # range 0-3
        final.append(nums[i][0:l])
        for k in range(l):
            nums[i].pop(0)

    for i in range(len(final[i])):
        str_n = ''
        for k in range(len(final)):
            if final[k][i] != '':
                str_n += final[k][i]
        if ops[j] == "+":
            n += int(str_n)
        else:
            n *= int(str_n)
    tot += n
print("part 2", tot)

