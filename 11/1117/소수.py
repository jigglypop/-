import sys
sys.stdin = open('2581.txt', 'r')
input = sys.stdin.readline
N = int(input())
M = int(input())


def is_prime(x):
    N = int(x ** 0.5) + 1
    if x < 2:
        return False
    for i in range(2, N):
        if x % i == 0:
            return False
    return True


flag = False
Min = 0
Sum = 0
for i in range(N, M+1):
    if is_prime(i):
        if flag == False:
            flag = True
            Min = i
        Sum += i
if Min != 0 and Sum != 0:
    print(Sum)
    print(Min)
else:
    print(-1)
