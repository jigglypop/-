import sys
sys.stdin = open('17608.txt', 'r')
input = sys.stdin.readline
N = int(input())
S = [int(input()) for _ in range(N)]
result = []
Max = 0
while S:
    s = S.pop()
    if s > Max:
        result.append(s)
        Max = s
print(len(result))
