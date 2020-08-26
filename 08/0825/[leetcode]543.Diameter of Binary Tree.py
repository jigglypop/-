from typing import *
from collections import defaultdict, deque


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return 'TreeNode({})'.format(self.val)


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
    longest: int = 0

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        node = deserialize(root)
        root = node[0]

        def DFS(node: TreeNode) -> int:
            if not node:
                return -1
            left = DFS(node.left)
            right = DFS(node.right)

            self.longest = max(self.longest, left + right + 2)
            print(node)
            print(left + right + 2)
            return max(left, right) + 1

        DFS(root)
        return self.longest


solution = Solution()
print(solution.diameterOfBinaryTree('[1,2,3,4,5]'))
