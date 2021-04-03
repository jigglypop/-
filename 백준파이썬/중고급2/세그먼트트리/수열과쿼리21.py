import sys
sys.stdin = open('16975.txt', 'r')
input = sys.stdin.readline
N = int(input())
tree = [0] * (N + 1)
A = list(map(int, input().split()))


def update(tree, i, x):
    while i < len(tree):
        tree[i] += x
        i += (i & -i)


for i in range(1, len(A)):
    update(tree, i, A[i])
M = int(input())
print(A)
# for _ in range(M):
#     temp = list(map(int, input().split()))
#     if temp[0] == 1:
#         update(tree, )

# print(tree)
