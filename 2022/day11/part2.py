import math

with open("input.txt", "r") as f:
    lines = f.read().split("\n\n")

monkeys_item = []
for monkey in lines:
    monkeys_item.append([x.strip() for x in monkey.split("\n")[1].replace("Starting items: ", "").split(", ")])

items_inspected = [0] * len(monkeys_item)
lcm = 1
for m in lines:
    actions = m.split("\n")
    condition = int(actions[3].strip().replace("Test: divisible by ", ""))
    lcm *= condition
for i in range(10000):
    for monkey in lines:
        actions = monkey.split("\n")
        monkey_number = int(actions[0].replace("Monkey ", "").replace(":", ""))
        items = monkeys_item[monkey_number]
        operating, operator = actions[2].strip().replace("Operation: new = old ", "").split(" ")
        condition = int(actions[3].strip().replace("Test: divisible by ", ""))
        true, false = int(actions[4].strip().replace("If true: throw to monkey ", "")), \
                      int(actions[5].strip().replace("If false: throw to monkey ", ""))
        tmp = items.copy()
        for item in tmp:

            try:
                tmp_operator = int(operator)
            except:
                tmp_operator = item
            worry_level = int(eval(item + operating + str(tmp_operator)))
            worry_level %= lcm
            if int(worry_level) % condition == 0:
                monkeys_item[true].append(str(worry_level))
            else:
                monkeys_item[false].append(str(worry_level))
            items.remove(item)
            items_inspected[monkey_number] += 1
    print(i)
print(items_inspected)
first_max = max(items_inspected)
items_inspected.remove(first_max)
second_max = max(items_inspected)
print(first_max * second_max)
