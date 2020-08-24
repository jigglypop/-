from typing import *


class Solution:
    def isValid(self, s: str) -> bool:
        table = {")": "(", "}": "{", "]": "["}
        stack = []
        for char in s:
            if char not in table:
                stack.append(char)
            elif not stack or table[char] != stack.pop():
                return False
        return len(stack) == 0


solution = Solution()
print(solution.isValid("([)]"))
