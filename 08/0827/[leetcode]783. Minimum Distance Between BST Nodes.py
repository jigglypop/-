from typing import *
from collections import deque
from pprint import pprint
import sys


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        # return f"TreeNode({self.val} : ({self.left} , {self.right}))\n"
        return f"TreeNode({self.val})"


def deserialize(string):
    if string == "{}":
        return None
    nodes = [None if val == "null" else TreeNode(
        int(val)) for val in string.strip('[]{}').split(',')]
    childNodes = deque(nodes[1:])
    for node in nodes:
        if node:
            if childNodes:
                node.left = childNodes.popleft()
            if childNodes:
                node.right = childNodes.popleft()
    return nodes


class Solution:
    def __init__(self, nums):
        self.nums = deserialize(nums)
        self.node = self.minDiffInBST(self.nums[0])

    prev = -sys.maxsize
    result = sys.maxsize

    def minDiffInBST(self, root: TreeNode) -> int:
        if root.left:
            self.minDiffInBST(root.left)

        self.result = min(self.result, root.val - self.prev)
        self.prev = root.val

        if root.right:
            self.minDiffInBST(root.right)
        return self.result


solution = Solution('[4,2,6,1,3,null,null]')
pprint(solution.result)
