import sys
from collections import deque
sys.stdin = open('2250.txt', 'r')
input = sys.stdin.readline


class Tree:
    def __init__(self, node, left, right):
        self.parent = -1
        self.node = node
        self.left = left
        self.right = right


def in_order(node, level):
    global level_depth, x
    level_depth = max(level, level_depth)

    if node.left != -1:
        in_order(tree[node.left], level + 1)

    level_max[level] = max(level_max[level], x)
    level_min[level] = min(level_min[level], x)
    x += 1

    if node.right != -1:
        in_order(tree[node.right], level + 1)


n = int(input())
tree = {}
level_max = [0] * (n + 1)
level_min = [n] * (n + 1)
root = -1
level_depth = 1
x = 1

for i in range(n + 1):
    tree[i] = Tree(i, -1, -1)

for _ in range(n):
    a, b, c = map(int, input().split())
    tree[a].left = b
    tree[a].right = c
    if b != -1:
        tree[b].parent = a
    if c != -1:
        tree[c].parent = a

for i in range(1, n + 1):
    if tree[i].parent == -1:
        root = i

in_order(tree[root], 1)

level = 1
Max = level_max[1] - level_min[1] + 1

for i in range(2, level_depth + 1):
    width = level_max[i] - level_min[i] + 1
    if Max < width:
        level = i
        Max = width

print(level, Max)
