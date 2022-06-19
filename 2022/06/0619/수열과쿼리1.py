import sys
from bisect import *
sys.stdin = open("./text/13537.txt", "r")
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))
tree = [[]] * (4 * N)
M = int(input())

def merge(L, H):
    l = h = 0
    result = []
    while l < len(L) and h < len(H):
        if L[l] < H[h]:
            result.append(L[l])
            l += 1
        else:
            result.append(H[h])
            h += 1
    return result + L[l:] + H[h:]
    
def init(n, s, e):
    if s == e:
        tree[n] = [nums[s]]
        return tree[n]
    m = (s + e) // 2
    tree[n] = merge(init(2 * n, s, m), init(2 * n + 1, m + 1, e))
    return tree[n]

def query(n, s, e, S, E, num):
    if S > e or s > E:
        return 0
    if S <= s and e <= E:
        return len(tree[n]) - bisect_right(tree[n], num)
    m = (s + e) // 2
    return query(2 * n, s, m, S, E, num) + query(2 * n + 1, m + 1, e, S, E, num)
    

init(1, 0, N - 1)
for _ in range(M):
    a, b, c = map(int, input().split())
    print(query(1, 0, N - 1, a - 1, b - 1, c))