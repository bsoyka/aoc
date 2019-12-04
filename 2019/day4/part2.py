from string import digits
import re

with open("input.txt") as f:
    start, stop = map(int, f.readlines()[0].strip().split("-"))
valid = 0
for check in range(start, stop + 1):
    check = str(check)
    repeats = 0
    if len(check) != 6:
        continue
    if not re.match(r"^1*2*3*4*5*6*7*8*9*$", check):
        continue
    for x in digits:
        check = check.replace(x*5, "")
        check = check.replace(x*4, "")
        check = check.replace(x*3, "")
        repeats += check.count(x * 2)
    if not repeats > 0:
        continue
    valid += 1
print(valid)  # 316