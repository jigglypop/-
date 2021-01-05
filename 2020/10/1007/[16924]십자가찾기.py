import sys
from pprint import pprint
sys.stdin = open('16924.txt', 'r')

Y, X = map(int, input().split())
board = [list(str(input())) for _ in range(Y)]
di = ((-1, 0), (1, 0), (0, 1), (0, -1))
stars_set = set()
for y in range(Y):
    for x in range(X):
        if board[y][x] == '*':
            stars_set.add((y, x))
making_star = set()
stars = list(stars_set)
flag = False
results = []
for y, x in stars:
    i = 1
    temp = set()
    while True:
        temp_set = set({(y, x)})
        for dy, dx in di:
            ny = y + dy * i
            nx = x + dx * i
            temp_set.add((ny, nx))
        merge = temp_set | temp
        if not merge.issubset(stars_set):
            break
        temp.update(merge)
        i += 1
    if len(temp) != 0:
        making_star.update(temp)
        results.append((y+1, x+1, i-1))
if making_star == stars_set:
    print(len(results))
    for result in results:
        print(*result)
else:
    print(-1)
