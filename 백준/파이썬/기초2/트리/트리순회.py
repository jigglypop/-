import sys
sys.stdin = open('1991.txt', 'r')
input = sys.stdin.readline


class Tree:
    def __init__(self, node, left, right):
        self.node = node
        self.left = left
        self.right = right


N = int(input())
tree = {}
for _ in range(N):
    a, b, c = map(str, input().split())
    a, b, c = ord(a)-65, ord(b)-65, ord(c)-65
    tree[a] = Tree(a, b, c)


def preorder(x):
    if x == -19:
        return
    print(chr(x + 65), end='')
    preorder(tree[x].left)
    preorder(tree[x].right)


def inorder(x):
    if x == -19:
        return
    inorder(tree[x].left)
    print(chr(x + 65), end='')
    inorder(tree[x].right)


def postorder(x):
    if x == -19:
        return
    postorder(tree[x].left)
    postorder(tree[x].right)
    print(chr(x + 65), end='')


preorder(0)
print()
inorder(0)
print()
postorder(0)
print()
