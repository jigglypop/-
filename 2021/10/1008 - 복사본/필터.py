import sys
sys.stdin = open("./text/1895.txt", "r")
input = sys.stdin.readline
Y, X = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(Y)]
T = int(input())

def middle(sy, sx, ey, ex):
    nums = []
    for y in range(sy, ey + 1):
        for x in range(sx, ex + 1):
            nums.append(board[y][x])
    nums.sort()
    return nums[4]

count = 0
for y in range(2, Y):
    for x in range(2, X):
        sy, sx, ey, ex = y - 2, x - 2, y, x
        if middle(sy, sx, ey, ex) >= T:
            count += 1
print(count)

