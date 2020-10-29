import sys
sys.stdin = open("1644.txt","r")
input = sys.stdin.readline

N = int(input())
check = [False, False] + [True] * (N-1)
primes = [0]
for i in range(2, N + 1):
    if check[i]:
        primes.append(i)
        for j in range(2 * i, N + 1, i):
            check[j] = False
left = 0
right = 0
Sum = 0 if len(primes) == 0 else primes[0]
result = 0

while left <= right and right < len(primes):
    if Sum <= N:
        if Sum == N:
            result += 1
        right += 1
        if right < len(primes):
            Sum += primes[right]
    else:
        Sum -= primes[left]
        left += 1
print(result)
