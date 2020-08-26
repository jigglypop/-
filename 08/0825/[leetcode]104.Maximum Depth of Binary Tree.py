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
    result: int = 0

    def maxDepth(self, root: TreeNode) -> int:
        node = deserialize(root)
        root = node[0]

        if root is None:
            return 0
        Q = deque([root])
        depth = 0
        while Q:
            depth += 1
            for _ in range(len(Q)):
                cur_root = Q.popleft()
                if cur_root.left:
                    Q.append(cur_root.left)
                if cur_root.right:
                    Q.append(cur_root.right)
        return depth


solution = Solution()
print(solution.maxDepth('[3,9,20,null,null,15,7]'))
