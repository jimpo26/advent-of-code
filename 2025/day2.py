print("I have paid for the entire pc, and I'm gonna use the entire pc ")

with open("input2.txt", "r") as f:
    data = f.read()

tot = 0
for r in data.split(","):
    low,up = r.split("-")
    for n in range(int(low),int(up)+1):
        str_n = str(n)
        if len(str_n) % 2 != 0:
            continue
        first, second = str_n[:len(str_n)//2], str_n[len(str_n)//2:]
        if first == second:
            tot += int(str_n)
print("part 1: ", tot)

tot = 0
num = 0
for r in data.split(","):
    #print(num, "of", len(data.split(",")))
    num+=1
    low,up = r.split("-")
    for n in range(int(low),int(up)+1):
        str_n = str(n)
        for i in range(len(str_n)):
            s = set()
            for j in range(0,len(str_n),i+1):
                if str_n[j:j+i+1] != str_n:
                    s.add(str_n[j:j+i+1])
            if len(s) == 1 :
                tot += int(str_n)
                break
print("part 2: ", tot)


