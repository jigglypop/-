import sys
from math import floor
from copy import deepcopy
sys.stdin = open("20057.txt", "r")
n = int(input())
grid = [list(map(int, input().split())) for i in range(n)]
tot = sum(map(sum, grid))
di = [0, -1, 0, 1]
dj = [-1, 0, 1, 0]
L, U, R, D = 0, 1, 2, 3
moves = [
    [U, U, 2], [U, 7], [U, R, 1], [U, L, 10], [L, L, 5],
    [D, D, 2], [D, 7], [D, R, 1], [D, L, 10]]


def blow(i, j, leftdir, movedir, x):
    grid[i][j] -= x
    for d in movedir:
        d = (leftdir + d) % 4
        i += di[d]
        j += dj[d]
    if 0 <= i < n and 0 <= j < n:
        grid[i][j] += x


step = []
for STEP in range(n):
    if STEP % 2 == 0:
        step.extend([(L, STEP+1), (D, STEP+1)])
    else:
        step.extend([(R, STEP+1), (U, STEP+1)])

i = j = n//2
for d, am in step:
    for STEP in range(am):
        i += di[d]
        j += dj[d]
        if j < 0:
            break
        sand = grid[i][j]
        rest = sand
        for *movdir, percentage in moves:
            blow(i, j, d, movdir, sand*percentage//100)
            rest -= sand*percentage//100
        blow(i, j, d, [L], rest)
    else:
        continue
    break

print(tot - sum(map(sum, grid)))
