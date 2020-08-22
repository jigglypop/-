import sys
from copy import deepcopy
sys.stdin = open("로또.txt",'r')


M = []
while True:
    l = list(map(int,input().split()))
    if l[-1] == 0:
        break
    M.append(l)

def comb(k, start):
    if k == R:
        print(*chosen)
        return
    for i in range(start,N):
        chosen.append(number[i])
        comb(k + 1, i + 1)
        chosen.pop()

for m in M:
    N = m[0]
    number = m[1:]
    R = 6
    chosen = []
    comb(0,0)
    print()