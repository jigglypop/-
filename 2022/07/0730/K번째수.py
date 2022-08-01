from bisect import bisect_left
import sys
sys.stdin = open('./text/7469.txt', 'r')
input = sys.stdin.readline
def Split():return map(int, input().strip().split())
def List():return list(map(int, input().strip().split()))
def Int():return int(input().strip())
def Str():return input().strip()

def merge(A, B):
    a = b = 0
    nums = []
    while a < len(A) and b < len(B):
        if A[a] < B[b]:
            nums.append(A[a])
            a += 1
        else:
            nums.append(B[b])
            b += 1
    nums += A[a:]
    nums += B[b:]
    return nums

def upper_bound(left, right, a, x):
    while left < right:
        mid = (left + right) // 2
        if a[mid] <= x:
            left = mid + 1
        else:
            right = mid
    return right


def init(n, s, e):
    if s == e:
        tree[n] = [board[s]]
        return tree[n]
    m = (s + e) // 2
    tree[n] = merge(init(2 * n, s, m) , init(2 * n + 1, m + 1, e))
    return tree[n]

def query(n, s, e, S, E, k):
    if s > E or S > e:
        return 0
    if S <= s and e <= E:
        return bisect_left(tree[n], k)
    m = (s + e) // 2
    return query(2 * n, s, m, S, E, k) + query(2 * n + 1, m + 1, e, S, E, k)

N, M = Split()
board = List()

tree = [0] * (4 * N)
init(1, 0, N - 1)
for _ in range(M):
    a, b, c = Split()
    l = -sys.maxsize
    r = sys.maxsize
    result = -sys.maxsize
    while l <= r:
        m = (l + r) /2
        if query(1, 0, N -1, a - 1, b - 1, m) < c:
            result = max(result, m)
            l = m + 1
        else: 
            r = m - 1
    print(int(result))