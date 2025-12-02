with open('input.txt', 'r') as f:
    data = f.read().splitlines()

PRIORITIES = '-abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
# there is an - in front of the letters to have the correct priority number without sum 1 each time

priorities_sum = 0

for rucksack in data:

    compartments = [rucksack[:len(rucksack)//2], rucksack[len(rucksack)//2:]]

    for i in range(len(compartments[0])):
        if compartments[0][i] in compartments[1]:
            priorities_sum += PRIORITIES.index(compartments[0][i])
            break

print(priorities_sum)
