import sys
from collections import defaultdict
sys.stdin = open("2015.txt", "r")
input = sys.stdin.readline

n, m = map(int, input().split())
board = [0] + list(map(int, input().split()))
for i in range(n):
    board[i+1] += board[i]
count = defaultdict(int)
count[0] = 1  # s[0] = 0
ans = 0
for i in range(1, n+1):
    print(count)
    ans += count[board[i]-m]
    count[board[i]] += 1
print(ans)
