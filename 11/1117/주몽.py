import sys
sys.stdin = open('1940.txt', 'r')

input = sys.stdin.readline
N = int(input())
M = int(input())
board = list(map(int, input().split()))
board.sort()
result = left = 0
right = N - 1
while left != right:
    Sum = board[left] + board[right]
    if Sum > M:
        right -= 1
    elif Sum < M:
        left += 1
    else:
        right -= 1
        result += 1
print(result)
