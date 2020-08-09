import sys
sys.stdin = open('[백준1991]트리순회.txt', 'r')
input = sys.stdin.readline


def change(m):
    if m == '.':
        return 0
    else:
        return ord(m)-64


def preorder(node):
    if node == 0:
        return
    print(chr(node+64), end="")
    preorder(tree[node][0])
    preorder(tree[node][1])


def inorder(node):
    if node == 0:
        return
    inorder(tree[node][0])
    print(chr(node+64), end="")
    inorder(tree[node][1])


def postorder(node):
    if node == 0:
        return
    postorder(tree[node][0])
    postorder(tree[node][1])
    print(chr(node+64), end="")


N = int(input())
tree = [[0, 0] for _ in range(N+1)]
for _ in range(N):
    a, b, c = map(str, input().split())
    tree[change(a)][0] = change(b)
    tree[change(a)][1] = change(c)
preorder(1)
print()
inorder(1)
print()
postorder(1)
