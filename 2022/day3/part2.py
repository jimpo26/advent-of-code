with open('input.txt', 'r') as f:
    data = f.read().splitlines()

PRIORITIES = '-abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
# there is an - in front of the letters to have the correct priority number without sum 1 each time

priorities_sum = 0
data = [data[i:i+3] for i in range(0, len(data), 3)]  # group data by 3 (elves group)

for rucksack in data:

    for i in range(len(rucksack[0])):

        if rucksack[0][i] in rucksack[1] and rucksack[0][i] in rucksack[2]:
            priorities_sum += PRIORITIES.index(rucksack[0][i])
            break

print(priorities_sum)
