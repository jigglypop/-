import sys
sys.stdin = open('연습.txt', 'r')

A, B = map(int, input().split())
M = list(map(int, input().split()))
result = ''
for m in M:
    if m < B:
        result += str(m) + ' '

print(result)
