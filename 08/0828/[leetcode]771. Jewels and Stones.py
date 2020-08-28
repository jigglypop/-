from collections import Counter


class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        stone = Counter(S)
        result = 0
        for j in J:
            result += stone[j]
        return result


solution = Solution()
print(solution.numJewelsInStones(J="aA", S="aAAbbbb"))
