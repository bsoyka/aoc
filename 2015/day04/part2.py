import hashlib
import re

with open("input.txt") as f:
    start = f.readlines()[0].strip()


def md5(obj):
    return hashlib.md5(obj.encode("utf-8")).hexdigest()


number = 0
while True:
    number += 1
    hash = md5(f"{start}{number}")
    print(f"{start}{number}", hash)
    if re.match(r"^0{6,}", hash):
        break
# 9958218