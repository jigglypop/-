import sys
sys.stdin = open('14427.txt', 'r')

input = sys.stdin.readline
N = int(input())
A = list(map(int, input().split()))
M = int(input())
tree = [0] * (4*N)


def init(x, start, end):
    if start == end:
        tree[x] = A[end]
        return
    mid = (start + end) // 2
    init(2 * x, start, mid)
    init(2 * x + 1, mid + 1, end)
    tree[x] = min(tree[2 * x], tree[2 * x + 1])


init(1, 0, N-1)
