import sys
sys.stdin = open("1929.txt", "r")
input = sys.stdin.readline

N, M = map(int, input().split())
MAX = 1000001
check = [True, True] + [False] * (MAX-2)
for i in range(2, MAX):
    if not check[i]:
        j = i * 2
        while j < MAX:
            check[j] = True
            j += i
for i in range(N, M+1):
    if check[i] == False:
        print(i)
