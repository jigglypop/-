from typing import *
from collections import defaultdict


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
    result: int = 0

    def longestUnivaluePath(self, root: TreeNode) -> int:
        node = deserialize(root)
        root = node[0]

        def DFS(node: TreeNode):
            if node is None:
                return 0
            left = DFS(node.left)
            right = DFS(node.right)

            left = left + 1 if node.left and node.left.val == node.val else 0
            right = right + 1 if node.right and node.right.val == node.val else 0
            self.result = max(self.result, left + right)
            return max(left, right)
        DFS(root)
        return self.result


solution = Solution()
print(solution.longestUnivaluePath('[3,9,20,null,null,15,7]'))
