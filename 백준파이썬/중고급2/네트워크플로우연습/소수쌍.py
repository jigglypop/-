import sys
sys.stdin = open('1017.txt')
N = int(input())
nums = list(map(int, input().split()))


# def isPrime(x):
#     if x < 2:
#         return False
#     for i in range(2, int(x ** 0.5) + 1):
#         if x % 2 == 0:
#             return False
#     return True


# graph = [[] for _ in range(N)]
# for i in range(N):
#     for j in range(N):
#         if i == j:
#             continue
#         if isPrime(nums[i] + nums[j]):
#             graph[i].append(j)


# def dfs(u):
#     if not check[u]:
#         check[u] = True
#         for v in graph[u]:
#             if parent[v] == -1 or dfs(parent[v]):
#                 parent[v] = u
#                 return True
#         return False


# for i in graph[0]:
#     parent = [-1 for _ in range(N)]
#     for j in range(1, N):
#         if i == j:
#             continue
#         if dfs(i):
