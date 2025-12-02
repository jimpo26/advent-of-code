with open("input.txt", "r") as f:
    data = f.read().splitlines()


total_points = 0
for line in data:
    tmp = line.split(" ")
    points = 0
    if tmp[0] == 'A':
        if tmp[1] == 'X':
            points = 4
        elif tmp[1] == 'Y':
            points = 8
        else:
            points = 3
    elif tmp[0] == 'B':
        if tmp[1] == 'Y':
            points = 3 + 2
        elif tmp[1] == 'Z':
            points = 6 + 3
        else:
            points = 0 + 1
    elif tmp[0] == 'C':
        if tmp[1] == 'Z':
            points = 3 + 3
        elif tmp[1] == 'X':
            points = 6 + 1
        else:
            points = 0 + 2
    total_points += points
print(total_points)
# i know that this is so terrible, i will improve it later cause now i'm a little bit hurry
