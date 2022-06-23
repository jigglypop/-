import sys
sys.stdin = open("./text/9426.txt", "r")
input = sys.stdin.readline
N, K = map(int, input().split())
nums = [int(input()) for _ in range(N)]
tree = [[] for _ in range(4 * N)]

def update(n, s, e, diff):
    if s == e:
        tree[n] = nums[s]
        return tree[n]
    m = (s + e) // 2
    tree[n] = update(2 * n, s, m), update(2 * n + 1, m + 1, e)
    return tree[n]

# init(1, 0, N - 1)


# def query(n, s, e, S, E):
#     if S > e or s > E:
#         return []
#     if S <= s and e <= E:
#         return tree[n]
#     m = (s + e) // 2
#     return query(2 * n, s, m, S, E) + query(2 * n + 1, m + 1, e, S, E)

# result = 0
# for i in range(N - K + 1):
#     M = K // 2
#     result += query(1, 0, N - 1, i, i + K - 1)[M]
# print(result)