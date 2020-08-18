from typing import *


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        def DFS(index, path):
            if len(path) == len(digits):
                result.append(path)
                return
            for y in range(index, len(digits)):
                for x in dic[digits[y]]:
                    DFS(y+1, path+x)

        dic = {"2": "abc", "3": "def", "4": "ghi", "5": "jki",
               "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        result = []
        DFS(0, "")
        return result


solution = Solution()
print(solution.letterCombinations("23"))
