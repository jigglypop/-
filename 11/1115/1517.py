import sys
sys.stdin = open('1517.txt', 'r')
input = sys.stdin.readline


def fenwick_update(tree, idx, d):
    while idx <= n:
        tree[idx] += d
        idx += (idx & -idx)


def fenwick_find(tree, start, end):
    if end < start:
        return 0
    res = 0
    idx = end
    while idx > 0:
        res += tree[idx]
        idx -= (idx & -idx)
    idx = start - 1
    while idx > 0:
        res -= tree[idx]
        idx -= (idx & -idx)
    return res


def relation_convert(arr):
    sort_arr = sorted(arr)
    mid = dict().fromkeys(sort_arr, 0)
    res = []
    visited = [False] * (len(arr) + 1)
    for idx, temp in enumerate(mid):
        mid[temp] = idx + 1
    for i in arr:
        if visited[mid[i]] == False:
            res.append(mid[i])
            visited[mid[i]] = True
    return res


n = int(sys.stdin.readline())
before = list(map(int, sys.stdin.readline().split()))
after = relation_convert(before)
ftr = [0] * (n + 1)
ans = 0
for i in range(len(after)):
    ans += (fenwick_find(ftr, after[i], len(after)))
    fenwick_update(ftr, after[i], 1)
print(ans)
