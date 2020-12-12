import sys
sys.stdin = open('6603.txt', 'r')
M = []
while True:
    l = list(map(int, input().split()))
    if l[-1] == 0:
        break
    M.append(l)


def comb(k, start):
    if k == R:
        print(*chosen)
        return
    for i in range(start, N):
        chosen.append(m[i])
        comb(k + 1, i + 1)
        chosen.pop()


for h in M:
    N = h[0]
    m = h[1:]
    R = 6
    chosen = []
    comb(0, 0)
    print()
