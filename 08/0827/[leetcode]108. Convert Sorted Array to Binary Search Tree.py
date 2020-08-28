from typing import *
from collections import deque
from pprint import pprint


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return f"TreeNode({self.val} : ({self.left} , {self.right}))"


def deserialize(string):
    if string == "{}":
        return None
    nodes = [None if val == "null" else TreeNode(
        int(val)) for val in string.strip('[]{}').split(',')]
    childNodes = deque(nodes)
    root = childNodes.popleft()
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
        self.root = nums[0]
        self.node = self.sortedArrayToBST(self.nums)

    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        mid = len(nums) // 2
        node = TreeNode(nums[mid])
        node.left = self.sortedArrayToBST(nums[:mid])
        node.right = self.sortedArrayToBST(nums[mid+1:])
        return node


solution = Solution('[-10, -3, 0, 5, 9]')
pprint(solution.node)
