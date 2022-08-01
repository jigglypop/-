import sys
sys.stdin = open('./text/1395.txt', 'r')
def Split():return map(int, input().strip().split())
def List():return list(map(int, input().strip().split()))
def Int():return int(input().strip())
def Str():return input().strip()
input = sys.stdin.readline

N, M = Split()
tree = [0] * (4 * N)
lazy = [0] * (4 * N)

def query(n, s, e, diff):
    if lazy[n] != 0:
        if lazy[n] & 1:
            tree[n] = abs(tree[n] - (e - s + 1))
            if s != e:
                lazy[2 * n ] += lazy[n]
                lazy[2 * n + 1] += lazy[n]
        lazy[n] = 0
    if s > E or S > e:
        return 0
    elif s >= S and e <= E:
        tree[n] = abs(tree[n] - (e - s + 1) * diff)
        if s != e:
            lazy[2 * n] += diff
            lazy[2 * n + 1] += diff
        return tree[n]
    else:
        m = (s + e) // 2
        temp = query(2 * n , s, m, diff) + query(2 * n + 1, m + 1, e, diff)
        tree[n] = tree[2 * n] + tree[2 * n + 1]
        return temp
    
for _ in range(M):
    a, b, c = Split()
    S, E = b, c
    if a == 0:
        query(1, 1, N, 1)
    else:
        print(query(1, 1, N, 0))