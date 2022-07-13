import sys
input = sys.stdin.readline
def Split():return map(int, input().strip().split())
def Int():return int(input().strip())
N = Int()
for _ in range(N):
    board = list(Split())
    temp = sum(board[1:]) / board[0] 
    count = 0
    for b in board[1:]:
        if b > temp:count += 1 
    print(f'{count / board[0] * 100:.3f}%')