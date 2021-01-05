from typing import *
from collections import defaultdict, deque
from pprint import pprint


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return 'TreeNode({} : {},{})'.format(self.val, self.left, self.right)


def deserialize(string):
    if string == '{}':
        return None
    nodes = [None if val == 'null' else TreeNode(int(val))
             for val in string.strip('[]{}').split(',')]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids:
                node.left = kids.pop()
            if kids:
                node.right = kids.pop()
    return nodes


class Solution:

    def invertTree(self, root: TreeNode) -> int:
        nodes = deserialize(root)
        root = nodes[0]

        Q = deque([root])
        while Q:
            node = Q.popleft()
            if node:
                node.left, node.right = node.right, node.left
                Q.append(node.left)
                Q.append(node.right)
        return root


solution = Solution()
print(solution.invertTree('[4,2,7,1,3,6,9]'))
