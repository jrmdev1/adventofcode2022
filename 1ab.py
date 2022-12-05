#Advent of code 2022
# 12/03/21 day 1a and 1b
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
#print(a_list)

cals = []
elf = 0
for calstr in a_list:
    if calstr == "":
        cals.append(elf)
        elf = 0
    else:
        elf += int(calstr)
#print(cals)
cals.sort(reverse=True)

max = cals[0]

#print(f"1a: elfnum={maxelf}, cals={max}")
print(f"1a: cals={max}")

#print(f"sorted cals={cals}")

cnt = 0
sum = 0
for elfcal in cals:
    sum += elfcal
    cnt += 1
    if cnt >= 3:
        break

print(f"1b: sum={sum}")