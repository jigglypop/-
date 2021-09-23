import sys
sys.stdin = open("./text/2104.txt", 'r')
input = sys.stdin.readline

N = int(input())
sumTree = [0] * N + list(map(int, input().split()))
minTree = sumTree[::]

for i in reversed(range(1, N)):
    sumTree[i] = sumTree[i * 2] + sumTree[i * 2 ^ 1]
    minTree[i] = min(minTree[i * 2] , minTree[i * 2 ^ 1])
print(sumTree)
print(minTree)