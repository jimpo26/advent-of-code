import os
from functools import reduce
import operator
with open("input.txt", "r") as f:
    lines = f.readlines()


def get_from_dict(data_dict, map_list):
    return reduce(operator.getitem, map_list, data_dict)


def set_in_dict(data_dict, map_list, value):
    get_from_dict(data_dict, map_list[:-1])[map_list[-1]] = value


tree = {}
key = ""
files = dict()
actual_key = []
for line in lines:
    if "$ cd" in line:
        if files != {}:
            set_in_dict(tree, actual_key, files)
            files = dict()
        if ".." in line:
            actual_key.pop()
        else:
            actual_key.append(line.split("$ cd ")[1].strip() + str(os.urandom(8).hex()))
            # i added some random bytes to the end of the key to avoid problems if there are folders with the same name
            set_in_dict(tree, actual_key, dict())

    elif "$ ls" in line:
        pass
    else:
        if "dir" not in line:
            files[line.split(" ")[-1].strip()] = line.split(" ")[0].strip()
        else:
            files[line.split(" ")[-1].strip()] = {}

set_in_dict(tree, actual_key, files)

sizes = dict()


def get_size(tree):
    size = 0
    for key, value in tree.items():
        tmp_size = 0
        if type(value) == dict:
            size += get_size(value)
            tmp_size += get_size(value)
            sizes[key] = tmp_size
        else:
            size += int(value)
    return size


(get_size(tree))
size_to_remove = 0
for d in sizes:
    if sizes[d] < 100000:
        size_to_remove += sizes[d]

print(size_to_remove)
