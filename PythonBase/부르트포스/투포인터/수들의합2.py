import sys
sys.stdin = open('2003.txt', 'r')
input = sys.stdin.readline
N, M = map(int, input().split())
board = list(map(int, input().split()))
result = Sum = left = right = 0
while True:
    if Sum >= M:
        Sum -= board[left]
        left += 1
    elif right == N:
        break
    elif Sum < M:
        Sum += board[right]
        right += 1
    if Sum == M:
        result += 1
print(result)
