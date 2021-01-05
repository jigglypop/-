from typing import *
from collections import deque
from pprint import pprint


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
    val = 0

    def __init__(self, nums):
        self.nums = deserialize(nums)
        # self.root = nums[0]
        self.node = self.bstToGst(self.nums[0])

    def view(self):
        return self.nums

    def bstToGst(self, root: TreeNode) -> TreeNode:
        if root:
            self.bstToGst(root.right)
            self.val += root.val
            root.val = self.val
            self.bstToGst(root.left)
        return root


solution = Solution('[4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]')
pprint(solution.nums)
