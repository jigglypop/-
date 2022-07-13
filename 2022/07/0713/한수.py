import sys
sys.stdin = open('./text/8958.txt', 'r')
input = sys.stdin.readline
def Split():return map(int, input().strip().split())
def Int():return int(input().strip())
def L(n, arr):
    if len(arr) == 1:return [n for _ in range(arr[0])]
    return [L(n, arr[1:]) for _ in range(arr[0])]
result = 0
for i in range(1, Int() + 1):
    board = list(map(int, str(i)))
    if i < 100:result += 1  
    elif board[0] - board[1] == board[1] - board[2]:result += 1  
print(result)