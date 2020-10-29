import sys
sys.stdin = open("1644.txt","r")
input = sys.stdin.readline

N = int(input())
check = [False, False] + [True] * (N-1)
primes = []
for i in range(2, N + 1):
    if check[i]:
        primes.append(i)
        for j in range(2 * i, N + 1, i):
            check[j] = False
print(check)