import sys
sys.stdin = open("2042.txt", "r")
input = sys.stdin.readline
n, m, k = map(int, input().split())
tree = [0] * n + [int(input()) for _ in range(n)]
for i in reversed(range(1, n)):
    tree[i] = tree[2 * i] + tree[2 * i ^ 1]


def update(i, x):
    tree[i] = x
    while i > 1:
        tree[i // 2] = tree[i] + tree[i ^ 1]
        i //= 2

# i % 2 = 1일 때 우측 자식, i % 2 = 0일때 좌측 자식


def query(l, r):
    res = 0
    while l < r:
        # 왼쪽의 우측자식은 더해줌
        if l % 2:
            res += tree[l]
            l += 1
        # 오른쪽의 좌측자식은 더해줌
        if not (r % 2):
            res += tree[r]
            r -= 1
        l >>= 1
        r >>= 1
    # 같으면 다 올라왔으므로 한번 더해줌
    if l == r:
        res += tree[l]
    return res


for _ in range(m + k):
    a, b, c = map(int, input().split())
    b += n - 1
    if a == 1:
        update(b, c)
    else:
        c += n - 1
        print(query(b, c))
