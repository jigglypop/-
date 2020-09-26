import sys
sys.stdin = open('10610.txt', 'r')

input = sys.stdin.readline
n = list(input())
N = sorted(n, reverse=True)
sums = sum([int(i) for i in N])
num = int(''.join(N))
if sums % 3 != 0 or '0' not in n:
    print(-1)
else:
    print(num)
