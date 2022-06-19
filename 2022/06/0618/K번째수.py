import sys
from bisect import bisect_left, bisect_right
sys.stdin = open("./text/7469.txt", "r")
input = sys.stdin.readline

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

N, M = map(int, input().split())
nums = list(map(int, input().split()))
tree = [[]] * (4 * N)

def init(n, s, e):
  if s == e:
    tree[n] = [nums[s]]
    return tree[n]
  m = (s + e) // 2
  tree[n] = merge(init(2 * n, s, m), init(2 * n + 1, m + 1, e))
  return tree[n]

def query(n, s, e, S, E, num):
  if s > E or S > e:
    return 0
  if S <= s and e <= E:
    return bisect_left(tree[n], num)
  m = (s + e) // 2
  return query(2 * n, s, m, S, E, num) + query(2 * n + 1, m + 1, e, S, E, num)

init(1, 0, N - 1)
for _ in range(1):
  a, b, num = map(int, input().split())
  l = -sys.maxsize
  r = sys.maxsize
  ans = -sys.maxsize
  while l <= r:
      m = (l+r) /2
      q = query(1, 0, N-1, a - 1, b - 1, m)
      if q < num:
        ans = max(ans, m)
        l = m + 1
      else: r = m - 1
  print(ans)