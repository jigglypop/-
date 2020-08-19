import sys
sys.stdin = open('5565.txt', 'r')

N = int(input())
for _ in range(9):
    N -= int(input())
print(N)
