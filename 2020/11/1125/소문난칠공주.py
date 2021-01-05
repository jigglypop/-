from itertools import combinations
import sys
sys.stdin = open('1941.txt', 'r')


def check(y, x):
    di = ((-1, 0), (1, 0), (0, 1), (0, -1))
    visited[5 * y + x] = 1
    result = 1
    for dy, dx in di:
        ny, nx = y + dy, x + dx
        if 0 <= ny < 5 and 0 <= nx < 5:
            if not visited[5 * ny + nx]:
                result += check(ny, nx)
    return result


board = [input() for i in range(5)]
result = 0
comb = combinations(range(25), 7)
for c in comb:
    Sum = 0
    visited = [1] * 25
    for k in c:
        Sum += (board[k//5][k % 5] == 'S')
        visited[k] = 0
    if Sum >= 4 and check(c[0]//5, c[0] % 5) == 7:
        result += 1
print(result)
