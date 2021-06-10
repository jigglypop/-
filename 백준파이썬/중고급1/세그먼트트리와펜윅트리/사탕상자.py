import sys
sys.stdin = open("2243.txt", "r")
input = sys.stdin.readline
N = int(input())
tree = [0] * (4 * N)


def update(x, s, e, i, diff):
    if i < s or i > e:
        return
    tree[x] += diff
    if s != e:
        m = (s + e) // 2
        update(2 * x, s, m, i, diff)
        update(2 * x, m + 1, e, i, diff)


for _ in range(N):
    temp = list(map(int, input().split()))
    if temp[0] == 2:
        i, diff = temp[1], temp[2]
        update(1, 1, N + 1, i, diff)
        print(tree)
    else:
        n = temp[1]
print(tree)
