import sys
sys.stdin = open('./text/3006.txt', 'r')
input = sys.stdin.readline
def Split():return map(int, input().strip().split())
def List():return list(map(int, input().strip().split()))
def Int():return int(input().strip())
def Str():return input().strip()

N = Int()
B = [Int() for _ in range(N)]
tree = [0] * (N + 1)

def sum(i):
    res = 0
    while i > 0:
        res += tree[i]
        i -= (i & -i)
    return res

def update(i, x):
    while i < len(tree):
        tree[i] += x
        i += (i & -i)

maps = {}
for i in range(1, N+1):
    update(i, 1)
    maps[B[i - 1]] = i

l, r = 1, N
for i in range(1, N + 1):
    if i % 2 == 1:
        a = maps[l]
        update(a, -1)
        print(sum(a))
        l += 1
    else:
        a = maps[r]
        update(a, -1)
        print(sum(N) - sum(a))
        r -= 1

