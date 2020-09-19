import sys
sys.stdin = open('1300.txt', 'r')

N = int(input())
K = int(input())
start, end = 1, K


temp = 0
for i in range(1, N+1):
    temp += min(5 // i, N)
    print(i)
print(temp)
