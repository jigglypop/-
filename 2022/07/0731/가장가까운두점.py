from collections import defaultdict, deque
import sys
sys.stdin = open('./text/2261.txt', 'r')
input = sys.stdin.readline
def Split():return map(int, input().strip().split())
def List():return list(map(int, input().strip().split()))
def Int():return int(input().strip())
def Str():return input().strip()

points = []
for _ in range(Int()):
    x, y = Split()
    points.append(x + y * 1j)
points = sorted(points, key=lambda x: x.real)

Min = min(abs(points[i + 1] - points[i]) for i in range(len(points) - 1))
if Min in [0, 1]:
    print(round(Min ** 2))
    exit(0)

group = [int(p.imag // Min) for p in points]
dict = defaultdict(deque)
s = 0
for idx, p1 in enumerate(points):
    while Min <= p1.real - points[s].real:
        i = dict[group[s]].popleft()
        assert s == i, (s, i)
        s += 1

    for k in range(group[idx] - 1, group[idx] + 2):
        if k not in dict:
            continue
        for i in dict[k]:
            Min = min(Min, abs(points[i] - p1))
    dict[group[idx]].append(idx)
print(round(Min ** 2))