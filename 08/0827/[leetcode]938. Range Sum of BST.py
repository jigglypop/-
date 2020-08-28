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
    val: int = 0

    def __init__(self, nums, L, R):
        self.L = L
        self.R = R
        self.nums = deserialize(nums)
        self.node = self.rangeSumBST(self.nums[0], self.L, self.R)

    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        if root:
            if root.val >= L and root.val <= R:
                self.val += root.val
            self.rangeSumBST(root.left, L, R)
            self.rangeSumBST(root.right, L, R)
        return self.val


solution = Solution('[10,5,15,3,7,null,18]', 7, 15)
pprint(solution.val)
