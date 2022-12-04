#Advent of code 2022
# 12/03/21 day 1a
# Joe McFarland
# import sys
# import re

filename = "data1.txt"

file = open(filename)
filestr = file.read()
a_list = filestr.split("\n")
# tack a final delimiter on end
a_list.append("")
maxrows = len(a_list)
print(a_list)

cals = []
elf = 0
for calstr in a_list:
    if calstr == "":
        cals.append(elf)
        elf = 0
    else:
        elf += int(calstr)
print(cals)

max = 0
maxelf = 1
cnt = 1
for elfcal in cals:
    if elfcal > max:
        max = elfcal
        maxelf = cnt
    cnt += 1

print(f"{maxelf}, {max}")

# prev = cals[0]
# count_incr = 0
# for depth in cals:
#     #print(f"{depth}, {prev}, {count_incr}")
#     if depth > prev:
#         count_incr += 1
#     prev = depth

# print(f"count_incr={count_incr}")
