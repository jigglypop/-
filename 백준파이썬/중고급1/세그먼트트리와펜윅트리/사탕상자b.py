import sys
sys.stdin = open("2243.txt", "r")
input = sys.stdin.readline
MAX = 10000000
tree = [0] * (2 * MAX)


def update(i, x):
    while i > 0:
        tree[i] += x
        i //= 2


def query(n):
    i = 1
    while i <= MAX:
        l = 2 * i
        r = 2 * i + 1
        if n <= tree[l]:
            i = l
        else:
            i = r
            n -= tree[l]
    print(i - MAX)
    update(i, -1)


N = int(input())
for _ in range(N):
    temp = list(map(int, input().split()))
    if temp[0] == 1:
        query(temp[1])
    else:
        update(temp[1] + MAX, temp[2])
