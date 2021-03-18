import sys
sys.stdin = open("17470.txt", "r")
input = sys.stdin.readline
n, m, r = map(int, input().split())
A = [list(map(int, input().split())) for i in range(n)]
B = [row[:] for row in A]
original = list(map(int, input().split()))

rot = 0
flip = False
subrot = 0
for x in original:
    if x == 1:
        flip = not flip
        rot = (rot+2) % 4
    elif x == 2:
        flip = not flip
    elif x == 3:
        rot = (rot+1) % 4 if not flip else (rot-1) % 4
    elif x == 4:
        rot = (rot-1) % 4 if not flip else (rot+1) % 4
    elif x == 5:
        subrot = (subrot+1) % 4 if not flip else (subrot-1) % 4
    elif x == 6:
        subrot = (subrot-1) % 4 if not flip else (subrot+1) % 4

comm = [3]*rot + [5]*subrot + [2]*flip
for x in comm:
    if x == 1:
        A = A[::-1]
    elif x == 2:
        A = [row[::-1] for row in A]
    elif x == 3:
        A = [[A[~i][j] for i in range(n)] for j in range(m)]
        n, m = m, n
    elif x == 4:
        A = [[A[i][~j] for i in range(n)] for j in range(m)]
        n, m = m, n
    elif x == 5:
        hn, hm = n//2, m//2
        for i in range(hn):
            for j in range(hm):
                A[i][j], A[i+hn][j], A[i][j+hm], A[i+hn][j+hm] =\
                    A[i+hn][j], A[i+hn][j+hm], A[i][j], A[i][j+hm]
    elif x == 6:
        hn, hm = n//2, m//2
        for i in range(hn):
            for j in range(hm):
                A[i][j], A[i+hn][j], A[i][j+hm], A[i+hn][j+hm] =\
                    A[i][j+hm], A[i][j], A[i+hn][j+hm], A[i+hn][j]

for row in A:
    print(*row)
