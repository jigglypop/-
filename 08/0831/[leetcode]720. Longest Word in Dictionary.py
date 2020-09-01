from typing import *
from collections import defaultdict


class Solution(object):
    def longestWord(self, words):
        words.sort()
        res = set([''])
        longestWord = ''
        for word in words:
            if word[:-1] in res:
                res.add(word)
                if len(word) > len(longestWord):
                    longestWord = word
        return longestWord


solution = Solution()
# print(solution.longestWord(["w", "wo", "wor", "worl", "world"]))
print(solution.longestWord(
    ["a", "banana", "app", "appl", "ap", "apply", "apple"]))
