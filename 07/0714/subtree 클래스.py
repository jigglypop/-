import sys
from copy import deepcopy
sys.stdin = open("subtree.txt", 'r')


class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data


class Tree:
    def __init__(self, cnt):
        self.list = [None]
        for i in range(E + 1):
            self.list.append(Node(i))

    def put(self, parent, child):
        # 왼쪽부터 넣음
        if self.list[parent].left == None:
            self.list[parent].left = self.list[child]
        else:
            self.list[parent].right = self.list[child]

    def count(self, node):
        self.cnt += 1
        if node.left:
            self.count(node.left)
        if node.right:
            self.count(node.right)

    def result(self, num):
        self.cnt = 0
        self.count(self.list[num])
        return self.cnt


T = int(input())
for tc in range(1, 1 + T):
    E, N = map(int, input().split())
    data = list(map(int, input().split()))
    tree = Tree(E)
    for i in range(E):
        tree.put(data[2 * i], data[2 * i + 1])
    print('#{} {}'.format(tc, tree.result(N)))
