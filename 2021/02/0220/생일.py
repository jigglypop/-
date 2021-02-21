import sys
sys.stdin = open('5635.txt', 'r')

N = int(input())
n = [list(input().split())[::-1] for _ in range(N)]
n = sorted(n, key=lambda x: (-int(x[0]), -int(x[1]), -int(x[2])))
print(n[0][-1])
print(n[-1][-1])
