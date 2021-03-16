import sys
from pprint import pprint
sys.stdin = open("3495.txt", "r")
H, W = map(int, input().split())
M = [list(input()) for _ in range(H)]
result = 0
for i in range(H):
    line = 0
    for j in M[i]:
        if j == '/' or j == '\\':
            line += 1
        if line % 2 == 1 and j == '.':
            result += 1
    result += (line // 2)
print(result)
