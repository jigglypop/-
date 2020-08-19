from typing import *

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# class Solution:
#     longest: int = 0

#     def diameterOfBinaryTree(self, root: TreeNode) -> int:
#         def DFS(node: TreeNode) -> int:
#             if not node:
#                 return -1
#             left = DFS(node.left)
#             right = DFS(node.right)
#             self.longest = max(self.longest, left + right + 2)
#             return max(left, right) + 1
#         DFS(root)
#         return self.longest


solution = Solution()
print(solution.diameterOfBinaryTree([1, 2, 3, 4, 5]))
