from typing import *
from pprint import pprint


class Solution:
    def DFS(self, grid: List[List[str]], sy: int, sx: int):
        di = ((-1, 0), (1, 0), (0, 1), (0, -1))
        S = []
        S.append((sy, sx))
        while S:
            y, x = S.pop()
            for dy, dx in di:
                ny, nx = y+dy, x+dx
                if 0 <= ny < len(grid) and 0 <= nx < len(grid[0]) and grid[ny][nx] == '1':
                    S.append((ny, nx))
                    grid[ny][nx] = '0'

    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        count = 0
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == '1':
                    self.DFS(grid, y, x)
                    count += 1
        return count


solution = Solution()
print(solution.numIslands([
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]))
print(solution.numIslands([]))
