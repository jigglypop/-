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
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        node1 = deserialize(t1)
        t1 = node1[0]
        node2 = deserialize(t2)
        t2 = node2[0]
        pprint(node1)
        pprint(node2)


solution = Solution()
print(solution.mergeTrees('[1,3,2,5]', '[2,1,3,null,4,null,7]'))
