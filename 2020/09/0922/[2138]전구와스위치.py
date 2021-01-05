import sys
import math
sys.stdin = open('2138.txt', 'r')

N = int(input())
before = list(input())
after = list(input())
_before = []
for i in range(2):
    _before.append(before[::])


def change(y, x, _before):
    return '1' if _before[y][x] == '0' else '0'


_before[1][0] = change(1, 0, _before)
_before[1][1] = change(1, 1, _before)

Min = sys.maxsize
for j in range(2):
    count = j
    for i in range(1, N-1):
        if _before[j][i-1] != after[i-1]:
            _before[j][i-1] = change(j, i-1, _before)
            _before[j][i] = change(j, i, _before)
            _before[j][i+1] = change(j, i+1, _before)
            count += 1
    if _before[j][-2] != after[-2]:
        _before[j][-2] = change(j, N-2, _before)
        _before[j][-1] = change(j, N-1, _before)
        count += 1
    if _before[j][-1] == after[-1]:
        Min = min(Min, count)
if Min == sys.maxsize:
    print(-1)
else:
    print(Min)
