import sys
sys.stdin = open('1427.txt', 'r')

N = list(map(int, input()))
N = sorted(N, reverse=True)
for i in N:
    print(i, end='')
