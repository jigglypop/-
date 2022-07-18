import sys
input = sys.stdin.readline
dp = [i for i in range(10000)]
def Split():return map(int, input().strip().split())
def List():return list(map(int, input().strip().split()))
def Int():return int(input().strip())
def Str():return input().strip()
MAX = 10000000
tree = [0] * (2 * MAX)

def update(i, x):
    while i > 0:
        tree[i] += x
        i //= 2

def query(order):
    i = 1
    while i <= MAX:
        l = 2 * i
        r = 2 * i + 1
        if order <= tree[l]:
            i = l
        else:
            i = r
            order -= tree[l]
    print(i - MAX)
    update(i, -1)

N = int(input())
for _ in range(N):
    temp = List()
    if temp[0] == 1: query(temp[1])
    else: update(temp[1] + MAX, temp[2])