import sys
from math import ceil
input = sys.stdin.readline
room_num = list(map(int, str(input())))
counts = [0] * 9
for i in room_num:
    if i == 6 or i == 9:
        counts[5] += 0.5
    else:
        counts[i] += 1
print(ceil(max(counts)))
