import sys
sys.stdin = open("1978.txt", "r")
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))

def isPrime(a):
    if a < 2:
        return False
    for i in range(2, int(a ** 0.5) + 1):
        if a % i == 0:
            return False
    return True

count = 0
for num in nums:
    if isPrime(num):
        count += 1
print(count)
