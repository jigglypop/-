import sys
sys.stdin = open("1978.txt", "r")
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))


# def is_prime(a):
#     if a < 2:
#         return False
#     i = 2
#     while i*i <= a:
#         if a % i == 0:
#             return False
#         i += 1
#     return True

def is_prime(a):
    N = int(a ** 0.5)
    if a < 2:
        return False
    for i in range(2, N+1):
        if a % i == 0:
            return False
    return True


count = 0
for num in nums:
    if is_prime(num):
        count += 1
print(count)
