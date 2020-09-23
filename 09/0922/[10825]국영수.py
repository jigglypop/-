import sys
sys.stdin = open('10825.txt', 'r')

N = int(input())
names = []
for _ in range(N):
    a, b, c, d = input().split()
    names.append((a, int(b), int(c), int(d)))
names = sorted(names, key=lambda x: (-x[1], x[2], -x[3], x[0]))
for name in names:
    print(name[0])
