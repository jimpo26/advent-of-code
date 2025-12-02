with open("input.txt", "r") as f:
    line = f.readline()

for i in range(len(line) - 14):
    if len(set(line[i:i+14])) == 14:
        print(i + 14)
        break
