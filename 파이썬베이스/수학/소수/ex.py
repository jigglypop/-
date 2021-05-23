import sys
sys.stdin = open("1929.txt", "r")
input = sys.stdin.readline

N, M = map(int, input().split())
MAX = 1000001
check = [False] * MAX
check[0] = check[1] = True

for i in range(2, MAX):
    if not check[i]:
        j = 2 * i
        while j < MAX:
            check[j] = True
            j += i

for i in range(N, M + 1):
    if not check[i]:
        print(i)
