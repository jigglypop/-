import sys
sys.stdin = open("./text/1037.txt", "r")
input = sys.stdin.readline

N = int(input())
peoples = list(map(int, input().split()))
M = int(input())
tree = [0] * (4 * N)
lazy = [0] * (4 * N)

def init(n, s, e):
  if s == e:
    tree[n] = peoples[s]
    return tree[n]
  m = (s + e) // 2
  tree[n] = init(2 * n, s, m) + init(2 * n + 1, m + 1, e)
  return tree[n]

def query(n, s, e, S, E):
  if s > E or S > e:
    return 0
  if S <= s and e <= E:
    return tree[n]
  m = (s + e) // 2
  return query(2 * n, s, m, S, E) + query(2 * n + 1, m + 1, e, S, E)

init(1, 0, N - 1)
print(query(1, 0, N - 1, 1, 2))



